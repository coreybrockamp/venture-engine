import json
import shlex
import shutil
import sys
import tempfile
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from run_shadow_batch import (
    BatchError,
    BatchOutcome,
    CommandStageRunner,
    DEFAULT_RUNS,
    MAX_RUNS,
    MIN_RUNS,
    ShadowBatchRunner,
)
from shadow_controller import Outcome, StageResult


BASE_FILES = {"SYSTEM_STATUS.md", "CHANGELOG.md", "research/commercial-friction-discovery/2026-09-09-test.md"}


class FakeController:
    def __init__(self, root, holder):
        self.root, self.holder = root, holder

    def preflight(self, bundle, check_runner=None):
        return self.holder.preflight

    def create_isolated_worktree(self, run_id):
        worktree = self.holder.temp / run_id
        (worktree / "venture-engine" / "reports" / "shadow-runs").mkdir(parents=True)
        self.holder.worktrees.append(worktree)
        return f"codex/shadow/{run_id}", worktree

    def evaluate(self, bundle, results, run_id, checks=None, changed=None):
        result = results[0]
        code = {"REJECT": "CFD_REJECT", "HOLD": "CFD_HOLD", "AUTHORIZE_SCOUT": "CFD_AUTHORIZE_SCOUT_REVIEW"}.get(result.decision, result.decision)
        return Outcome(code, result.reason, ["cfd"], ["cfd"], files_changed=sorted(changed["cfd"]), validator_result="passed", tests_result="passed")

    def manifest(self, run_id, bundle, outcome, **kwargs):
        return {"run_id": run_id, "bundle": bundle, "terminal_stop_code": outcome.code, "terminal_reason": outcome.reason}

    def write_artifacts(self, engine, manifest):
        directory = engine / "reports" / "shadow-runs"
        json_path = directory / f"{manifest['run_id']}.json"
        report_path = directory / f"{manifest['run_id']}.md"
        json_path.write_text(json.dumps(manifest))
        report_path.write_text(f"{manifest['terminal_stop_code']}\n")
        return json_path, report_path


class FakeAcceptor:
    def __init__(self, root, holder):
        self.holder = holder

    def accept(self, worktree, run_id):
        if self.holder.accept_failure:
            raise BatchError("simulated acceptance failure")
        if self.holder.cleanup_failure:
            raise BatchError("simulated cleanup failure")
        self.holder.accepted.append(run_id)
        self.holder.retained.append(run_id)
        self.holder.head += 1
        shutil.rmtree(worktree)
        return f"commit-{self.holder.head}"


class FakeAuditStore:
    def __init__(self, root, holder):
        self.holder = holder

    def write(self, outcome):
        self.holder.audits.append(outcome.report())
        outcome.audit_paths = ["reports/shadow-runs/batches/test.json", "reports/shadow-runs/batches/test.md"]
        return outcome.audit_paths


class Holder:
    def __init__(self, decisions):
        self.temp = Path(tempfile.mkdtemp())
        self.decisions = iter(decisions)
        self.head = 0
        self.worktrees, self.accepted, self.audits = [], [], []
        self.retained = []
        self.preflight = None
        self.accept_failure = False
        self.cleanup_failure = False
        self.dirty_after = None
        self.unsynchronized_after = None

    def cleanup(self):
        shutil.rmtree(self.temp, ignore_errors=True)


class TestBatchRunner(ShadowBatchRunner):
    def __init__(self, holder):
        self.holder = holder
        super().__init__(Path("/fixture/venture-engine"), self.stage_runner,
                         controller_factory=lambda root: FakeController(root, holder),
                         acceptor_factory=lambda root: FakeAcceptor(root, holder),
                         audit_store_factory=lambda root: FakeAuditStore(root, holder))

    def baseline(self):
        if self.holder.dirty_after is not None and len(self.holder.accepted) >= self.holder.dirty_after:
            raise BatchError("baseline is dirty")
        if self.holder.unsynchronized_after is not None and len(self.holder.accepted) >= self.holder.unsynchronized_after:
            raise BatchError("local main is not synchronized with origin/main")
        return f"main-{self.holder.head}"

    def checks(self, engine):
        return True, True

    def changed_paths(self, worktree):
        audit = {f"reports/shadow-runs/{worktree.name}.json", f"reports/shadow-runs/{worktree.name}.md"}
        return BASE_FILES | (audit if (worktree / "venture-engine" / "reports" / "shadow-runs" / f"{worktree.name}.json").exists() else set())

    def allocate_run_id(self, first_sequence):
        return f"SHADOW-20260909T230000Z-{first_sequence:04d}"

    def stage_runner(self, run_id, worktree):
        decision = next(self.holder.decisions)
        return StageResult("cfd", True, decision=decision, reason=f"{decision} reason", expected_files=sorted(BASE_FILES), next_transition="stop")


class ShadowBatchRunnerTests(unittest.TestCase):
    def make(self, decisions):
        holder = Holder(decisions)
        self.addCleanup(holder.cleanup)
        return holder, TestBatchRunner(holder)

    def test_five_routine_runs_accept_clean_and_use_fresh_updated_baselines(self):
        holder, runner = self.make(["REJECT", "HOLD", "REJECT", "HOLD", "REJECT"])
        outcome = runner.run(5, "BATCH-test")
        self.assertEqual(outcome.status, "BATCH_COMPLETE")
        self.assertEqual([run.terminal_code for run in outcome.runs], ["CFD_REJECT", "CFD_HOLD", "CFD_REJECT", "CFD_HOLD", "CFD_REJECT"])
        self.assertEqual([run.starting_commit for run in outcome.runs], [f"main-{n}" for n in range(5)])
        self.assertEqual(len(set(run.run_id for run in outcome.runs)), 5)
        self.assertEqual(len(set(run.worktree for run in outcome.runs)), 5)
        self.assertEqual(holder.accepted, [run.run_id for run in outcome.runs])
        self.assertEqual(holder.retained, [run.run_id for run in outcome.runs])
        self.assertTrue(all(not Path(run.worktree).exists() for run in outcome.runs))
        self.assertEqual(holder.audits[-1]["reject_count"], 3)
        self.assertEqual(holder.audits[-1]["hold_count"], 2)

    def test_authorize_scout_stops_without_acceptance_or_next_run(self):
        holder, runner = self.make(["REJECT", "AUTHORIZE_SCOUT", "REJECT"])
        outcome = runner.run(3, "BATCH-test")
        self.assertEqual(outcome.status, "BATCH_ESCALATED")
        self.assertTrue(outcome.authorize_scout_occurred)
        self.assertEqual(len(outcome.runs), 2)
        self.assertEqual(holder.accepted, [outcome.runs[0].run_id])
        self.assertEqual(outcome.runs[1].acceptance, "NOT_ACCEPTED")
        self.assertTrue(Path(outcome.runs[1].worktree).exists())

    def test_controller_failure_stops_immediately(self):
        holder, runner = self.make(["REJECT"])
        holder.preflight = Outcome("POLICY_VIOLATION", "bad policy", [], [])
        outcome = runner.run(2, "BATCH-test")
        self.assertEqual(outcome.status, "BATCH_FAILED")
        self.assertIn("POLICY_VIOLATION", outcome.reason)
        self.assertEqual(outcome.runs, [])

    def test_acceptance_cleanup_and_dirty_baseline_failures_stop(self):
        for attribute, message in (("accept_failure", "acceptance"), ("cleanup_failure", "cleanup")):
            with self.subTest(attribute=attribute):
                holder, runner = self.make(["REJECT", "REJECT"])
                setattr(holder, attribute, True)
                outcome = runner.run(2, "BATCH-test")
                self.assertEqual(outcome.status, "BATCH_FAILED")
                self.assertIn(message, outcome.reason)
                self.assertEqual(len(outcome.runs), 0)
        holder, runner = self.make(["REJECT", "REJECT"])
        holder.dirty_after = 1
        outcome = runner.run(2, "BATCH-test")
        self.assertEqual(outcome.status, "BATCH_FAILED")
        self.assertIn("dirty", outcome.reason)
        self.assertEqual(len(holder.accepted), 1)
        holder, runner = self.make(["REJECT", "REJECT"])
        holder.unsynchronized_after = 1
        outcome = runner.run(2, "BATCH-test")
        self.assertEqual(outcome.status, "BATCH_FAILED")
        self.assertIn("synchronized", outcome.reason)
        self.assertEqual(len(holder.accepted), 1)

    def test_bounds_reports_and_no_scheduler_or_bundle_two_path(self):
        _, runner = self.make(["REJECT"])
        for value in (MIN_RUNS - 1, MAX_RUNS + 1):
            with self.subTest(value=value):
                with self.assertRaisesRegex(ValueError, "max-runs"):
                    runner.run(value, "BATCH-test")
        source = (ROOT / "scripts" / "run_shadow_batch.py").read_text()
        self.assertEqual(DEFAULT_RUNS, 5)
        self.assertNotIn("import schedule", source)
        self.assertNotIn("threading", source)
        self.assertNotIn("asyncio", source)
        self.assertNotIn('"push", "origin", "main"', source)
        self.assertNotIn("approved_candidate", source)
        self.assertNotIn("market_analysis", source)

    def test_non_normal_controller_codes_are_never_routine_accepted(self):
        holder, runner = self.make(["VALIDATION_FAILED", "REJECT"])
        outcome = runner.run(2, "BATCH-test")
        self.assertEqual(outcome.status, "BATCH_FAILED")
        self.assertEqual(len(outcome.runs), 1)
        self.assertEqual(outcome.runs[0].acceptance, "NOT_ACCEPTED")
        self.assertEqual(holder.accepted, [])

    def test_command_stage_runner_preserves_special_paths_as_single_arguments(self):
        with tempfile.TemporaryDirectory(prefix="shadow worktree (spaces) '") as directory:
            worktree = Path(directory) / "New project (runner)"
            engine = worktree / "venture-engine"
            engine.mkdir(parents=True)
            runner_script = Path(directory) / "capture runner.py"
            runner_script.write_text(
                "import argparse, json\n"
                "from pathlib import Path\n"
                "p = argparse.ArgumentParser()\n"
                "p.add_argument('--run-id'); p.add_argument('--worktree'); p.add_argument('--result-path')\n"
                "a = p.parse_args()\n"
                "result = Path(a.result_path); result.parent.mkdir(parents=True, exist_ok=True)\n"
                "result.with_suffix('.args.json').write_text(json.dumps(vars(a)))\n"
                "result.write_text(json.dumps({'stage':'cfd','completed':True,'decision':'REJECT','reason':'test','expected_files':[], 'evidence':{}, 'entities':{}, 'source_exception':None, 'safety_exception':None, 'next_transition':'stop'}))\n"
            )
            template = f"{shlex.quote(sys.executable)} {shlex.quote(str(runner_script))} --run-id={{run_id}} --worktree={{worktree}} --result-path={{result_path}}"
            run_id = "SHADOW-20260909T235000Z-0001"
            CommandStageRunner(template)(run_id, worktree)
            result_path = engine / "reports" / "shadow-runs" / f"{run_id}.stage-result.json"
            captured = json.loads(result_path.with_suffix(".args.json").read_text())
            self.assertEqual(captured["run_id"], run_id)
            self.assertEqual(captured["worktree"], str(worktree))
            self.assertEqual(captured["result_path"], str(result_path))
            self.assertFalse(result_path.exists())

    def test_command_stage_runner_fails_closed_for_malformed_and_failed_commands(self):
        with self.assertRaisesRegex(ValueError, "invalid --stage-runner"):
            CommandStageRunner("python3 '{run_id}")
        with self.assertRaisesRegex(ValueError, "must include"):
            CommandStageRunner("python3 {run_id}")
        with tempfile.TemporaryDirectory(prefix="runner failure ") as directory:
            worktree = Path(directory) / "worktree with spaces"
            (worktree / "venture-engine").mkdir(parents=True)
            failing = Path(directory) / "fails.py"
            failing.write_text("raise SystemExit(7)\n")
            command = f"{shlex.quote(sys.executable)} {shlex.quote(str(failing))} --run-id={{run_id}} --worktree={{worktree}} --result-path={{result_path}}"
            with self.assertRaisesRegex(BatchError, "stage runner failed"):
                CommandStageRunner(command)("SHADOW-20260909T235001Z-0001", worktree)

    def test_command_stage_runner_supports_normal_paths(self):
        with tempfile.TemporaryDirectory() as directory:
            worktree = Path(directory) / "worktree"
            engine = worktree / "venture-engine"
            engine.mkdir(parents=True)
            runner_script = Path(directory) / "runner.py"
            runner_script.write_text(
                "import argparse, json\nfrom pathlib import Path\n"
                "p=argparse.ArgumentParser(); p.add_argument('--run-id'); p.add_argument('--worktree'); p.add_argument('--result-path'); a=p.parse_args()\n"
                "r=Path(a.result_path); r.parent.mkdir(parents=True, exist_ok=True); r.write_text(json.dumps({'stage':'cfd','completed':True,'decision':'REJECT','reason':'ok','expected_files':[], 'evidence':{}, 'entities':{}, 'source_exception':None, 'safety_exception':None, 'next_transition':'stop'}))\n"
            )
            command = f"{shlex.quote(sys.executable)} {shlex.quote(str(runner_script))} --run-id={{run_id}} --worktree={{worktree}} --result-path={{result_path}}"
            result = CommandStageRunner(command)("SHADOW-20260909T235002Z-0001", worktree)
            self.assertEqual(result.decision, "REJECT")

    def test_runner_failure_stops_before_any_cfd_continuation(self):
        holder, runner = self.make(["REJECT"])
        def fail(_run_id, _worktree):
            raise BatchError("stage runner failed: test")
        runner.stage_runner = fail
        outcome = runner.run(2, "BATCH-test")
        self.assertEqual(outcome.status, "BATCH_FAILED")
        self.assertEqual(outcome.runs, [])
        self.assertEqual(holder.accepted, [])


if __name__ == "__main__":
    unittest.main()
