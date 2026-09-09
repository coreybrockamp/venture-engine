#!/usr/bin/env python3
"""Run a bounded foreground sequence of approved Bundle 1 shadow runs.

This wrapper is deliberately not a research engine or scheduler.  A human supplies
one reviewed CFD stage-runner command for the invocation.  That command must write a
structured ``StageResult`` JSON file; this module then applies the existing
controller and normal-run acceptance lifecycle one run at a time.
"""
from __future__ import annotations

import argparse
import json
import shlex
import subprocess
import sys
from string import Formatter
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable

from accept_shadow_run import AcceptanceError, ShadowRunAcceptor
from shadow_controller import Outcome, ShadowController, StageResult, utc_run_id


MIN_RUNS, MAX_RUNS, DEFAULT_RUNS = 1, 10, 5
NORMAL_CODES = {"CFD_REJECT", "CFD_HOLD"}
ESCALATION_CODES = {"CFD_AUTHORIZE_SCOUT_REVIEW", "SOURCE_EXCEPTION", "SAFETY_BOUNDARY"}


class BatchError(RuntimeError):
    """A condition that prevents a safe next Bundle 1 run."""


@dataclass
class BatchRun:
    run_id: str
    starting_commit: str
    terminal_code: str
    terminal_reason: str
    acceptance: str
    cleanup: str
    worktree: str


@dataclass
class BatchOutcome:
    batch_id: str
    status: str
    reason: str
    requested_max_runs: int
    starting_commit: str
    ending_commit: str = ""
    runs: list[BatchRun] = field(default_factory=list)
    authorize_scout_occurred: bool = False
    final_synchronized: bool = False
    audit_paths: list[str] = field(default_factory=list)

    def report(self) -> dict:
        return {
            "batch_id": self.batch_id,
            "started_at": self.batch_id.removeprefix("BATCH-"),
            "finished_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
            "requested_max_runs": self.requested_max_runs,
            "runs_attempted": len(self.runs),
            "run_ids": [run.run_id for run in self.runs],
            "starting_main_sha": self.starting_commit,
            "ending_main_sha": self.ending_commit,
            "runs": [asdict(run) for run in self.runs],
            "reject_count": sum(run.terminal_code == "CFD_REJECT" for run in self.runs),
            "hold_count": sum(run.terminal_code == "CFD_HOLD" for run in self.runs),
            "authorize_scout_occurred": self.authorize_scout_occurred,
            "batch_status": self.status,
            "stop_reason": self.reason,
            "main_origin_synchronized": self.final_synchronized,
            "next_human_decision": self.next_human_decision(),
        }

    def next_human_decision(self) -> str:
        if self.status == "BATCH_ESCALATED":
            return "Review the preserved CFD candidate and provide explicit approval before Bundle 2."
        if self.status == "BATCH_FAILED":
            return "Review the failed batch audit and resolve the recorded safety or repository condition before another run."
        return "A human may explicitly initiate another bounded Bundle 1 batch or single discovery run."


def utc_batch_id(now: datetime | None = None) -> str:
    now = now or datetime.now(timezone.utc)
    return f"BATCH-{now.strftime('%Y%m%dT%H%M%SZ')}"


class BatchAuditStore:
    """Format an audit, then retain it only through the established acceptance helper."""

    def __init__(self, root: Path):
        self.root = root.resolve()

    def write(self, outcome: BatchOutcome) -> list[str]:
        markdown = (
            "\n".join([
                f"# Shadow Batch {outcome.batch_id}", "",
                f"- Status: `{outcome.status}`", f"- Requested/attempted: {outcome.requested_max_runs}/{len(outcome.runs)}",
                f"- Starting/ending main: `{outcome.starting_commit}` / `{outcome.ending_commit}`",
                f"- Terminal results: {', '.join(f'{run.run_id}: {run.terminal_code}' for run in outcome.runs) or 'None'}",
                f"- Stop reason: {outcome.reason}",
                f"- Main/origin synchronized: {outcome.final_synchronized}",
                f"- Next human decision: {outcome.next_human_decision()}", "",
            ])
        )
        try:
            ShadowRunAcceptor(self.root).record_batch_audit(outcome.batch_id, outcome.report(), markdown)
        except AcceptanceError as error:
            raise BatchError(str(error)) from error
        relative = [f"reports/shadow-runs/batches/{outcome.batch_id}.json", f"reports/shadow-runs/batches/{outcome.batch_id}.md"]
        outcome.audit_paths = relative
        return relative


class CommandStageRunner:
    """Run one explicitly supplied, reviewed CFD runner command in a worktree."""

    def __init__(self, command_template: str):
        required = {"{run_id}", "{worktree}", "{result_path}"}
        try:
            self.argv_template = shlex.split(command_template)
            fields = {field_name for _, field_name, _, _ in Formatter().parse(command_template) if field_name}
        except ValueError as error:
            raise ValueError(f"invalid --stage-runner command: {error}") from error
        if not required <= {f"{{{field}}}" for field in fields}:
            raise ValueError("--stage-runner must include {run_id}, {worktree}, and {result_path}")
        unsupported = fields - {"run_id", "worktree", "result_path"}
        if unsupported:
            raise ValueError(f"--stage-runner contains unsupported placeholders: {', '.join(sorted(unsupported))}")

    def __call__(self, run_id: str, worktree: Path) -> StageResult:
        engine = worktree / "venture-engine"
        result_path = engine / "reports" / "shadow-runs" / f"{run_id}.stage-result.json"
        command = [token.format(run_id=run_id, worktree=str(worktree), result_path=str(result_path))
                   for token in self.argv_template]
        completed = subprocess.run(command, cwd=engine, text=True, capture_output=True)
        if completed.returncode:
            raise BatchError(f"stage runner failed: {completed.stderr.strip() or completed.stdout.strip()}")
        if not result_path.is_file():
            raise BatchError("stage runner did not create its structured StageResult file")
        result = StageResult.from_path(result_path)
        result_path.unlink()
        return result


class ShadowBatchRunner:
    """Sequentially compose preflight, one supplied CFD runner, and acceptance."""

    def __init__(self, root: Path, stage_runner: Callable[[str, Path], StageResult],
                 controller_factory: Callable[[Path], ShadowController] = ShadowController,
                 acceptor_factory: Callable[[Path], ShadowRunAcceptor] = ShadowRunAcceptor,
                 audit_store_factory: Callable[[Path], BatchAuditStore] = BatchAuditStore):
        self.root = root.resolve()
        self.stage_runner = stage_runner
        self.controller_factory = controller_factory
        self.acceptor_factory = acceptor_factory
        self.audit_store_factory = audit_store_factory

    def _git(self, *args: str) -> str:
        result = subprocess.run(["git", *args], cwd=self.root, text=True, capture_output=True)
        if result.returncode:
            raise BatchError(result.stderr.strip() or result.stdout.strip() or "git command failed")
        return result.stdout

    def baseline(self) -> str:
        if self._git("branch", "--show-current").strip() != "main":
            raise BatchError("baseline is not local main")
        if self._git("status", "--porcelain"):
            raise BatchError("baseline is dirty")
        head, remote = self._git("rev-parse", "HEAD").strip(), self._git("rev-parse", "origin/main").strip()
        if head != remote:
            raise BatchError("local main is not synchronized with origin/main")
        return head

    def checks(self, engine: Path) -> tuple[bool, bool]:
        validator = subprocess.run([sys.executable, "scripts/validate_repo.py"], cwd=engine, capture_output=True, text=True)
        tests = subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", "tests"], cwd=engine, capture_output=True, text=True)
        return validator.returncode == 0, tests.returncode == 0

    def changed_paths(self, worktree: Path) -> set[str]:
        raw = self._git_in(worktree, "status", "--porcelain", "-z", "--untracked-files=all")
        paths: set[str] = set()
        for item in raw.split("\0"):
            if item:
                path = item[3:]
                if not path.startswith("venture-engine/"):
                    raise BatchError(f"shadow diff is outside engine root: {path}")
                paths.add(path.removeprefix("venture-engine/"))
        return paths

    def allocate_run_id(self, first_sequence: int) -> str:
        """Avoid retained audit IDs and preserved failed-run branches."""
        for sequence in range(first_sequence, 10_000):
            run_id = utc_run_id(sequence)
            reports = self.root / "reports" / "shadow-runs"
            branch = subprocess.run(["git", "show-ref", "--verify", "--quiet", f"refs/heads/codex/shadow/{run_id}"], cwd=self.root)
            if not (reports / f"{run_id}.json").exists() and not (reports / f"{run_id}.md").exists() and branch.returncode:
                return run_id
        raise BatchError("could not allocate a fresh shadow run ID")

    @staticmethod
    def _git_in(cwd: Path, *args: str) -> str:
        result = subprocess.run(["git", *args], cwd=cwd, text=True, capture_output=True)
        if result.returncode:
            raise BatchError(result.stderr.strip() or result.stdout.strip() or "git command failed")
        return result.stdout

    def run(self, max_runs: int = DEFAULT_RUNS, batch_id: str | None = None) -> BatchOutcome:
        if not MIN_RUNS <= max_runs <= MAX_RUNS:
            raise ValueError(f"--max-runs must be between {MIN_RUNS} and {MAX_RUNS}")
        batch_id = batch_id or utc_batch_id()
        try:
            start = self.baseline()
        except BatchError as error:
            return BatchOutcome(batch_id, "BATCH_FAILED", str(error), max_runs, "")
        outcome = BatchOutcome(batch_id, "BATCH_COMPLETE", "Requested maximum reached.", max_runs, start)
        for sequence in range(1, max_runs + 1):
            try:
                starting_commit = self.baseline()
                controller = self.controller_factory(self.root)
                preflight = controller.preflight("discovery", check_runner=self.checks)
                if preflight:
                    raise BatchError(f"{preflight.code}: {preflight.reason}")
                run_id = self.allocate_run_id(sequence)
                branch, worktree = controller.create_isolated_worktree(run_id)
                result = self.stage_runner(run_id, worktree)
                changed = self.changed_paths(worktree)
                terminal = controller.evaluate("discovery", [result], run_id, checks={"cfd": self.checks(worktree / "venture-engine")}, changed={"cfd": changed})
                terminal.next_human_decision = ("Review the preserved CFD candidate and provide explicit approval before Bundle 2."
                                                if terminal.code == "CFD_AUTHORIZE_SCOUT_REVIEW" else outcome.next_human_decision())
                audit_paths = {
                    f"reports/shadow-runs/{run_id}.json",
                    f"reports/shadow-runs/{run_id}.md",
                }
                terminal.files_changed = sorted(set(terminal.files_changed) | audit_paths)
                manifest = controller.manifest(run_id, "discovery", terminal, start=starting_commit, branch=branch, worktree=str(worktree))
                json_path, report_path = controller.write_artifacts(worktree / "venture-engine", manifest)
                declared = set(terminal.files_changed)
                if {str(json_path.relative_to(worktree / "venture-engine")), str(report_path.relative_to(worktree / "venture-engine"))} - declared:
                    raise BatchError("manifest omitted its controller audit files")
                if self.changed_paths(worktree) != declared:
                    raise BatchError("manifest/report files do not match the shadow diff")
                if terminal.code not in NORMAL_CODES:
                    outcome.runs.append(BatchRun(run_id, starting_commit, terminal.code, terminal.reason, "NOT_ACCEPTED", "PRESERVED", str(worktree)))
                    outcome.status = "BATCH_ESCALATED" if terminal.code in ESCALATION_CODES else "BATCH_FAILED"
                    outcome.reason = f"{terminal.code}: {terminal.reason}"
                    outcome.authorize_scout_occurred = terminal.code == "CFD_AUTHORIZE_SCOUT_REVIEW"
                    break
                commit = self.acceptor_factory(self.root).accept(worktree, run_id)
                self.baseline()  # acceptance must leave a clean, synchronized fresh baseline
                outcome.runs.append(BatchRun(run_id, starting_commit, terminal.code, terminal.reason, f"ACCEPTED:{commit}", "CLEANED", str(worktree)))
            except (BatchError, AcceptanceError, ValueError, RuntimeError) as error:
                outcome.status = "BATCH_FAILED"
                outcome.reason = str(error)
                break
        try:
            outcome.ending_commit = self.baseline()
            outcome.final_synchronized = True
        except BatchError:
            outcome.ending_commit = ""
            outcome.final_synchronized = False
        try:
            self.audit_store_factory(self.root).write(outcome)
            self.baseline()
        except BatchError as error:
            outcome.status = "BATCH_FAILED"
            outcome.reason = f"batch audit persistence failed: {error}"
            outcome.final_synchronized = False
        return outcome


def main() -> int:
    parser = argparse.ArgumentParser(description="Run a bounded, foreground Bundle 1 shadow-discovery batch.")
    parser.add_argument("--max-runs", type=int, default=DEFAULT_RUNS, help="bounded run count (1-10; default 5)")
    parser.add_argument("--stage-runner", required=True, help="reviewed command containing {run_id}, {worktree}, and {result_path}")
    args = parser.parse_args()
    runner = ShadowBatchRunner(Path(__file__).resolve().parents[1], CommandStageRunner(args.stage_runner))
    outcome = runner.run(args.max_runs)
    print(json.dumps(outcome.report(), indent=2, sort_keys=True))
    return 0 if outcome.status == "BATCH_COMPLETE" else 2


if __name__ == "__main__":
    raise SystemExit(main())
