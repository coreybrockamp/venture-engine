import json
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from shadow_controller import REQUIRED_MANIFEST_FIELDS, ShadowController, StageResult, utc_run_id


def result(stage, decision="", **kwargs):
    next_transition = kwargs.pop("next_transition", "cluster" if stage == "scout" and decision != "INSUFFICIENT_EVIDENCE" else "scout" if stage == "persona_resolution" else "stop")
    return StageResult(stage=stage, completed=True, decision=decision, reason=kwargs.pop("reason", decision), expected_files=kwargs.pop("expected_files", []), evidence=kwargs.pop("evidence", {}), entities=kwargs.pop("entities", {}), source_exception=kwargs.pop("source_exception", None), safety_exception=kwargs.pop("safety_exception", None), next_transition=next_transition)


class ShadowControllerTests(unittest.TestCase):
    def setUp(self):
        self.controller = ShadowController(ROOT)
        self.run_id = "SHADOW-20260909T030000Z-0001"

    def test_run_id_is_auditable_and_utc(self):
        self.assertEqual(utc_run_id(7, datetime(2026, 9, 9, 3, 0, tzinfo=timezone.utc)), "SHADOW-20260909T030000Z-0007")

    def test_dirty_baseline_is_rejected(self):
        def command(args, cwd):
            output = "main\n" if args[1:3] == ["branch", "--show-current"] else " M SYSTEM_STATUS.md\0"
            return subprocess.CompletedProcess(args, 0, output, "")
        outcome = ShadowController(ROOT, command=command).preflight("discovery")
        self.assertEqual(outcome.code, "DIRTY_BASELINE")

    def test_cfd_terminal_mappings_stop_before_persona_or_scout(self):
        for decision, code in {"REJECT": "CFD_REJECT", "HOLD": "CFD_HOLD", "AUTHORIZE_SCOUT": "CFD_AUTHORIZE_SCOUT_REVIEW"}.items():
            with self.subTest(decision=decision):
                outcome = self.controller.evaluate("discovery", [result("cfd", decision)], self.run_id, changed={"cfd": set()})
                self.assertEqual(outcome.code, code)
                self.assertEqual(outcome.stages_completed, ["cfd"])

    def test_bundle_two_requires_approval_reference(self):
        def clean_command(args, cwd):
            return subprocess.CompletedProcess(args, 0, "main\n" if args[1:3] == ["branch", "--show-current"] else "", "")
        outcome = ShadowController(ROOT, command=clean_command).preflight("approved_candidate", None)
        self.assertEqual(outcome.code, "POLICY_VIOLATION")
        # The direct evaluator still rejects a graph lacking approved target scope.
        outcome = self.controller.evaluate("approved_candidate", [result("persona_resolution")], self.run_id)
        self.assertEqual(outcome.code, "RUNNER_FAILED")

    def test_scout_insufficient_stops_before_cluster(self):
        approval = {"persona_id": "PER-013", "persona_slug": "outpatient-referral-operations-manager", "card": "x"}
        outcome = self.controller.evaluate("approved_candidate", [result("persona_resolution"), result("scout", "INSUFFICIENT_EVIDENCE", reason="insufficient")], self.run_id, approval, changed={"persona_resolution": set(), "scout": set()})
        self.assertEqual(outcome.code, "SCOUT_INSUFFICIENT_EVIDENCE")
        self.assertNotIn("cluster", outcome.stages_attempted)

    def test_cluster_zero_and_problem_promotion_stop_before_market(self):
        approval = {"persona_id": "PER-013", "persona_slug": "outpatient-referral-operations-manager", "card": "x"}
        prefix = [result("persona_resolution"), result("scout", "SUFFICIENT")]
        for decision, code in {"ZERO_PROMOTED": "CLUSTER_ZERO_PROMOTED", "PROBLEM_PROMOTED": "PROBLEM_PROMOTED_REVIEW"}.items():
            with self.subTest(decision=decision):
                outcome = self.controller.evaluate("approved_candidate", prefix + [result("cluster", decision)], self.run_id, approval, changed={"persona_resolution": set(), "scout": set(), "cluster": set()})
                self.assertEqual(outcome.code, code)
                self.assertNotIn("market_analysis", outcome.stages_attempted)

    def test_validation_and_test_failures_stop(self):
        validation = self.controller.evaluate("discovery", [result("cfd", "REJECT")], self.run_id, checks={"cfd": (False, True)}, changed={"cfd": set()})
        tests = self.controller.evaluate("discovery", [result("cfd", "REJECT")], self.run_id, checks={"cfd": (True, False)}, changed={"cfd": set()})
        self.assertEqual(validation.code, "VALIDATION_FAILED")
        self.assertEqual(tests.code, "TESTS_FAILED")

    def test_forbidden_and_unexpected_writes_are_detected(self):
        forbidden = self.controller.evaluate("discovery", [result("cfd", "REJECT", expected_files=["data/observations.jsonl"])], self.run_id, changed={"cfd": {"data/observations.jsonl"}})
        unexpected = self.controller.evaluate("discovery", [result("cfd", "REJECT")], self.run_id, changed={"cfd": {"SYSTEM_STATUS.md"}})
        self.assertEqual(forbidden.code, "FORBIDDEN_WRITE")
        self.assertEqual(unexpected.code, "UNEXPECTED_DIFF")

    def test_source_safety_and_policy_boundaries_stop(self):
        self.assertEqual(self.controller.evaluate("discovery", [result("cfd", source_exception="gated")], self.run_id).code, "SOURCE_EXCEPTION")
        self.assertEqual(self.controller.evaluate("discovery", [result("cfd", safety_exception="clinical")], self.run_id).code, "SAFETY_BOUNDARY")
        self.assertEqual(self.controller.evaluate("discovery", [result("market_analysis")], self.run_id).code, "POLICY_VIOLATION")
        policy = json.loads(json.dumps(self.controller.policy)); policy["bundles"]["discovery"]["stages"] = ["market_analysis"]
        self.assertFalse(ShadowController(ROOT, policy=policy).policy_valid("discovery"))

    def test_stage_result_cannot_request_an_unapproved_transition(self):
        outcome = self.controller.evaluate("discovery", [result("cfd", "REJECT", next_transition="scout")], self.run_id)
        self.assertEqual(outcome.code, "POLICY_VIOLATION")

    def test_manifest_and_report_are_complete_and_remote_is_false(self):
        outcome = self.controller.evaluate("discovery", [result("cfd", "REJECT")], self.run_id, changed={"cfd": set()})
        manifest = self.controller.manifest(self.run_id, "discovery", outcome, start="abc", branch="codex/shadow/x", worktree="/tmp/x")
        self.assertEqual(set(manifest), REQUIRED_MANIFEST_FIELDS)
        self.assertIn(manifest["terminal_stop_code"], self.controller.policy["terminal_stop_codes"])
        self.assertFalse(manifest["remote_mutated"])
        self.assertIn("remote mutation false", self.controller.report(manifest))

    def test_controller_has_no_remote_mutation_commands(self):
        source = (ROOT / "scripts" / "shadow_controller.py").read_text()
        self.assertNotIn('"git", "push"', source)
        self.assertNotIn('"git", "merge"', source)

    def temporary_nested_repo(self):
        temp_dir = tempfile.TemporaryDirectory()
        repository = Path(temp_dir.name) / "checkout"
        engine = repository / "venture-engine"
        (engine / "config").mkdir(parents=True)
        shutil.copy(ROOT / "config" / "shadow-autonomy.yaml", engine / "config" / "shadow-autonomy.yaml")
        (repository / "README.md").write_text("fixture\n")
        for command in (["git", "init"], ["git", "config", "user.email", "test@example.com"], ["git", "config", "user.name", "Test"], ["git", "add", "."], ["git", "commit", "-m", "fixture"]):
            subprocess.run(command, cwd=repository, check=True, capture_output=True, text=True)
        return temp_dir, repository, engine

    def test_worktree_is_outside_top_level_for_nested_engine_root(self):
        temp_dir, repository, engine = self.temporary_nested_repo()
        with temp_dir:
            controller = ShadowController(engine)
            branch, worktree = controller.create_isolated_worktree("SHADOW-20260908T230000Z-0001")
            self.assertFalse(worktree.is_relative_to(repository))
            self.assertEqual(subprocess.run(["git", "status", "--porcelain"], cwd=repository, capture_output=True, text=True, check=True).stdout, "")
            subprocess.run(["git", "worktree", "remove", "--force", str(worktree)], cwd=repository, check=True, capture_output=True, text=True)
            self.assertEqual(branch, "codex/shadow/SHADOW-20260908T230000Z-0001")
            with self.assertRaisesRegex(ValueError, "cannot be reused"):
                controller.create_isolated_worktree("SHADOW-20260908T230000Z-0001")

    def test_unsafe_or_reused_destination_is_rejected_without_dirtying_baseline(self):
        temp_dir, repository, engine = self.temporary_nested_repo()
        with temp_dir:
            controller = ShadowController(engine)
            controller._worktree_parent = lambda _root: repository / "unsafe"  # type: ignore[method-assign]
            with self.assertRaisesRegex(ValueError, "outside the Git top-level"):
                controller.create_isolated_worktree("SHADOW-20260908T230000Z-0002")
            clean = subprocess.run(["git", "status", "--porcelain"], cwd=repository, capture_output=True, text=True, check=True).stdout
            self.assertEqual(clean, "")
            external = repository.parent / ".checkout-shadow-worktrees" / "SHADOW-20260908T230000Z-0003"
            external.mkdir(parents=True)
            with self.assertRaisesRegex(ValueError, "never reused"):
                ShadowController(engine).create_isolated_worktree("SHADOW-20260908T230000Z-0003")
            self.assertEqual(subprocess.run(["git", "status", "--porcelain"], cwd=repository, capture_output=True, text=True, check=True).stdout, "")

    def test_failed_worktree_add_leaves_baseline_clean(self):
        temp_dir, repository, engine = self.temporary_nested_repo()
        with temp_dir:
            def fail_add(args, cwd):
                if args[:3] == ["git", "worktree", "add"]:
                    return subprocess.CompletedProcess(args, 1, "", "simulated failure")
                return subprocess.run(args, cwd=cwd, capture_output=True, text=True, check=False)
            with self.assertRaisesRegex(RuntimeError, "simulated failure"):
                ShadowController(engine, command=fail_add).create_isolated_worktree("SHADOW-20260908T230000Z-0004")
            self.assertEqual(subprocess.run(["git", "status", "--porcelain"], cwd=repository, capture_output=True, text=True, check=True).stdout, "")
