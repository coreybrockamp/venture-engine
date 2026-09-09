import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from accept_shadow_run import AcceptanceError, ShadowRunAcceptor


class ShadowRunAcceptanceTests(unittest.TestCase):
    def fixture(self, code="CFD_REJECT"):
        temp = tempfile.TemporaryDirectory()
        repository = Path(temp.name) / "checkout"
        engine = repository / "venture-engine"
        (engine / "config").mkdir(parents=True)
        shutil.copy(ROOT / "config" / "shadow-autonomy.yaml", engine / "config" / "shadow-autonomy.yaml")
        (engine / "SYSTEM_STATUS.md").write_text("baseline\n")
        (engine / "CHANGELOG.md").write_text("baseline\n")
        (engine / "reports" / "shadow-runs").mkdir(parents=True)
        (engine / "reports" / "shadow-runs" / "historical.md").write_text("preserve\n")
        for command in (["git", "init", "-b", "main"], ["git", "config", "user.email", "test@example.com"], ["git", "config", "user.name", "Test"], ["git", "add", "."], ["git", "commit", "-m", "baseline"]):
            subprocess.run(command, cwd=repository, check=True, capture_output=True, text=True)
        start = subprocess.run(["git", "rev-parse", "HEAD"], cwd=repository, check=True, capture_output=True, text=True).stdout.strip()
        run_id = "SHADOW-20260909T230000Z-0001"
        branch = f"codex/shadow/{run_id}"
        worktree = repository.parent / "external-shadow"
        subprocess.run(["git", "worktree", "add", "-b", branch, str(worktree), "main"], cwd=repository, check=True, capture_output=True, text=True)
        shadow = worktree / "venture-engine"
        card = "research/commercial-friction-discovery/2026-09-09-test.md"
        for relative, text in (("SYSTEM_STATUS.md", "shadow status\n"), ("CHANGELOG.md", "shadow changelog\n"), (card, "# card\n")):
            target = shadow / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(text)
        files = ["SYSTEM_STATUS.md", "CHANGELOG.md", card, f"reports/shadow-runs/{run_id}.json", f"reports/shadow-runs/{run_id}.md"]
        manifest = {"run_id": run_id, "started_at": "2026-09-09T23:00:00Z", "policy_version": "shadow-pilot-v1", "bundle": "discovery", "starting_commit": start, "branch": branch, "worktree": str(worktree), "approved_candidate_ref": None, "stages_attempted": ["cfd"], "stages_completed": ["cfd"], "terminal_stop_code": code, "terminal_reason": "normal result", "evidence": {}, "entities_created": {"personas": [], "observations": [], "problems": []}, "files_changed": files, "validator_result": "passed", "tests_result": "passed", "local_commit": None, "remote_mutated": False, "next_human_decision": "review"}
        report_dir = shadow / "reports" / "shadow-runs"
        (report_dir / f"{run_id}.json").write_text(json.dumps(manifest))
        (report_dir / f"{run_id}.md").write_text(f"{code}\nnormal result\n")
        return temp, repository, engine, worktree, run_id, branch, manifest

    def accept(self, code="CFD_REJECT"):
        temp, repository, engine, worktree, run_id, branch, manifest = self.fixture(code)
        self.addCleanup(temp.cleanup)
        return repository, engine, worktree, run_id, branch, manifest

    def test_successful_reject_accepts_preserves_and_cleans_up(self):
        repository, engine, worktree, run_id, branch, _ = self.accept()
        commit = ShadowRunAcceptor(engine).accept(worktree, run_id, push=False)
        self.assertTrue(commit)
        self.assertFalse(worktree.exists())
        self.assertTrue((engine / f"reports/shadow-runs/{run_id}.json").is_file())
        self.assertTrue((engine / "research/commercial-friction-discovery/2026-09-09-test.md").is_file())
        self.assertNotIn(branch, subprocess.run(["git", "branch", "--list", branch], cwd=repository, capture_output=True, text=True, check=True).stdout)

    def test_successful_hold_accepts(self):
        _, engine, worktree, run_id, _, _ = self.accept("CFD_HOLD")
        ShadowRunAcceptor(engine).accept(worktree, run_id, push=False)
        self.assertTrue((engine / f"reports/shadow-runs/{run_id}.md").is_file())

    def test_escalation_is_refused(self):
        _, engine, worktree, run_id, branch, manifest = self.accept("CFD_AUTHORIZE_SCOUT_REVIEW")
        (worktree / "venture-engine" / "reports/shadow-runs" / f"{run_id}.json").write_text(json.dumps(manifest))
        with self.assertRaisesRegex(AcceptanceError, "only normal"):
            ShadowRunAcceptor(engine).accept(worktree, run_id, push=False)
        self.assertTrue(worktree.exists())
        self.assertEqual(branch, manifest["branch"])

    def test_canonical_entity_or_path_is_refused(self):
        _, engine, worktree, run_id, _, manifest = self.accept()
        manifest["entities_created"]["observations"] = ["OBS-000001"]
        (worktree / "venture-engine" / "reports/shadow-runs" / f"{run_id}.json").write_text(json.dumps(manifest))
        with self.assertRaisesRegex(AcceptanceError, "canonical entities"):
            ShadowRunAcceptor(engine).load_and_validate(worktree, run_id)
        _, engine, worktree, run_id, _, manifest = self.accept()
        manifest["files_changed"].append("data/observations.jsonl")
        (worktree / "venture-engine" / "data").mkdir(exist_ok=True)
        (worktree / "venture-engine" / "data" / "observations.jsonl").write_text("{}\n")
        (worktree / "venture-engine" / "reports/shadow-runs" / f"{run_id}.json").write_text(json.dumps(manifest))
        with self.assertRaisesRegex(AcceptanceError, "canonical changes"):
            ShadowRunAcceptor(engine).load_and_validate(worktree, run_id)

    def test_manifest_diff_disagreement_is_refused(self):
        _, engine, worktree, run_id, _, _ = self.accept()
        (worktree / "venture-engine" / "unexpected.md").write_text("nope\n")
        with self.assertRaisesRegex(AcceptanceError, "does not match"):
            ShadowRunAcceptor(engine).load_and_validate(worktree, run_id)

    def test_failed_checks_and_remote_mutation_are_refused(self):
        for key, value, message in (("validator_result", "failed", "validator"), ("tests_result", "failed", "validator"), ("remote_mutated", True, "remote mutation")):
            with self.subTest(key=key):
                _, engine, worktree, run_id, _, manifest = self.accept()
                manifest[key] = value
                (worktree / "venture-engine" / "reports/shadow-runs" / f"{run_id}.json").write_text(json.dumps(manifest))
                with self.assertRaisesRegex(AcceptanceError, message):
                    ShadowRunAcceptor(engine).load_and_validate(worktree, run_id)

    def test_incompatible_main_baseline_is_refused(self):
        _, engine, worktree, run_id, _, manifest = self.accept()
        manifest["starting_commit"] = "0" * 40
        (worktree / "venture-engine" / "reports/shadow-runs" / f"{run_id}.json").write_text(json.dumps(manifest))
        with self.assertRaises(AcceptanceError):
            ShadowRunAcceptor(engine).accept(worktree, run_id, push=False)

    def test_historical_audit_artifacts_are_not_deleted(self):
        _, engine, worktree, run_id, _, _ = self.accept()
        ShadowRunAcceptor(engine).accept(worktree, run_id, push=False)
        self.assertEqual((engine / "reports/shadow-runs/historical.md").read_text(), "preserve\n")

    def test_batch_audit_uses_the_existing_safe_git_path(self):
        _, engine, _, _, _, _ = self.accept()
        commit = ShadowRunAcceptor(engine).record_batch_audit("BATCH-20260909T230000Z", {"status": "BATCH_COMPLETE"}, "# batch\n", push=False)
        self.assertTrue(commit)
        self.assertTrue((engine / "reports/shadow-runs/batches/BATCH-20260909T230000Z.json").is_file())
        with self.assertRaisesRegex(AcceptanceError, "cannot be reused"):
            ShadowRunAcceptor(engine).record_batch_audit("BATCH-20260909T230000Z", {}, "# duplicate\n", push=False)


if __name__ == "__main__":
    unittest.main()
