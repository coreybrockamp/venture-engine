#!/usr/bin/env python3
"""Bounded, local-only controller for the approved shadow-pilot-v1 graph.

This module deliberately does not dispatch research agents. A future approved runner
supplies structured stage-result JSON; this controller enforces the fixed graph,
checks the repository, and records an auditable stop.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable

ROOT = Path(__file__).resolve().parents[1]
POLICY_PATH = ROOT / "config" / "shadow-autonomy.yaml"
REQUIRED_MANIFEST_FIELDS = {
    "run_id", "started_at", "policy_version", "bundle", "starting_commit", "branch", "worktree",
    "approved_candidate_ref", "stages_attempted", "stages_completed", "terminal_stop_code",
    "terminal_reason", "evidence", "entities_created", "files_changed", "validator_result",
    "tests_result", "local_commit", "remote_mutated", "next_human_decision",
}


def load_policy(path: Path = POLICY_PATH) -> dict:
    """The policy is JSON-compatible YAML, avoiding a new runtime dependency."""
    return json.loads(path.read_text())


def utc_run_id(sequence: int = 1, now: datetime | None = None) -> str:
    now = now or datetime.now(timezone.utc)
    return f"SHADOW-{now.strftime('%Y%m%dT%H%M%SZ')}-{sequence:04d}"


def run_command(args: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, cwd=cwd, text=True, capture_output=True, check=False)


def git_paths(cwd: Path, command: Callable = run_command) -> set[str]:
    result = command(["git", "status", "--porcelain", "-z"], cwd)
    if result.returncode:
        raise RuntimeError(result.stderr or result.stdout)
    paths = set()
    for item in result.stdout.split("\0"):
        if not item:
            continue
        path = item[3:]
        if " -> " in path:
            path = path.rsplit(" -> ", 1)[-1]
        paths.add(path)
    return paths


def is_within(path: Path, parent: Path) -> bool:
    """Return whether path is parent itself or nested beneath it, without I/O."""
    try:
        path.resolve().relative_to(parent.resolve())
        return True
    except ValueError:
        return False


def parse_approval(path: Path) -> dict | None:
    if not path.is_file():
        return None
    text = path.read_text()
    if "Shadow Bundle 2 Approval: APPROVED" not in text:
        return None
    values = {}
    for label, key in (("Candidate Card", "card"), ("Persona ID", "persona_id"), ("Persona Slug", "persona_slug")):
        match = re.search(rf"^{re.escape(label)}:\s*(.+)$", text, re.MULTILINE)
        if not match:
            return None
        values[key] = match.group(1).strip()
    if not re.fullmatch(r"PER-\d{3}", values["persona_id"]) or not re.fullmatch(r"[a-z0-9-]+", values["persona_slug"]):
        return None
    return values


@dataclass
class StageResult:
    stage: str
    completed: bool
    decision: str = ""
    reason: str = ""
    expected_files: list[str] = field(default_factory=list)
    evidence: dict = field(default_factory=dict)
    entities: dict = field(default_factory=dict)
    source_exception: str | None = None
    safety_exception: str | None = None
    next_transition: str = "stop"

    @classmethod
    def from_path(cls, path: Path) -> "StageResult":
        value = json.loads(path.read_text())
        required = {"stage", "completed", "decision", "reason", "expected_files", "evidence", "entities", "source_exception", "safety_exception", "next_transition"}
        missing = required - set(value)
        if missing:
            raise ValueError(f"stage result missing fields: {', '.join(sorted(missing))}")
        return cls(**{key: value[key] for key in required})


@dataclass
class Outcome:
    code: str
    reason: str
    stages_attempted: list[str]
    stages_completed: list[str]
    evidence: dict = field(default_factory=dict)
    entities: dict = field(default_factory=lambda: {"personas": [], "observations": [], "problems": []})
    files_changed: list[str] = field(default_factory=list)
    validator_result: str = "not run"
    tests_result: str = "not run"
    next_human_decision: str = "Review the shadow-run report."


class ShadowController:
    """Fixed-graph policy evaluator. It has no dynamic agent/stage selection."""

    def __init__(self, root: Path = ROOT, policy: dict | None = None, command: Callable = run_command):
        self.root, self.policy, self.command = root, policy or load_policy(root / "config" / "shadow-autonomy.yaml"), command

    def policy_valid(self, bundle: str) -> bool:
        fixed = {"discovery": ["cfd"], "approved_candidate": ["persona_resolution", "scout", "cluster"]}
        configured = self.policy.get("bundles", {})
        return (self.policy.get("policy_version") == "shadow-pilot-v1" and bundle in configured
                and configured[bundle].get("stages") == fixed[bundle]
                and not set(self.policy.get("forbidden_stages", ())) & set(fixed[bundle]))

    def preflight(self, bundle: str, approval_ref: Path | None = None, check_runner: Callable | None = None) -> Outcome | None:
        if not self.policy_valid(bundle):
            return Outcome("POLICY_VIOLATION", "Requested bundle or policy violates shadow-pilot-v1.", [], [])
        branch = self.command(["git", "branch", "--show-current"], self.root)
        if branch.returncode or branch.stdout.strip() != self.policy["git"]["required_start_branch"]:
            return Outcome("POLICY_VIOLATION", "Expected clean local main baseline.", [], [])
        if git_paths(self.root, self.command):
            return Outcome("DIRTY_BASELINE", "Local main has uncommitted changes.", [], [])
        if bundle == "approved_candidate" and not approval_ref:
            return Outcome("POLICY_VIOLATION", "Bundle 2 requires a human-approved candidate reference.", [], [])
        if bundle == "approved_candidate" and not parse_approval(approval_ref):
            return Outcome("POLICY_VIOLATION", "Candidate approval reference is missing or invalid.", [], [])
        if check_runner:
            validator_ok, tests_ok = check_runner(self.root)
            if not validator_ok:
                return Outcome("VALIDATION_FAILED", "Baseline repository validator failed.", [], [], validator_result="failed")
            if not tests_ok:
                return Outcome("TESTS_FAILED", "Baseline test suite failed.", [], [], validator_result="passed", tests_result="failed")
        return None

    def create_isolated_worktree(self, run_id: str) -> tuple[str, Path]:
        """Create a fresh local-only shadow branch; callers must pass preflight first."""
        top = self.command(["git", "rev-parse", "--show-toplevel"], self.root)
        if top.returncode:
            raise RuntimeError(top.stderr or top.stdout)
        repository_root = Path(top.stdout.strip()).resolve()
        branch = f"{self.policy['git']['shadow_branch_prefix']}{run_id}"
        parent = self._worktree_parent(repository_root)
        worktree = (parent / run_id).resolve()
        if is_within(worktree, repository_root):
            raise ValueError("shadow worktree path must be outside the Git top-level checkout")
        if worktree.exists():
            raise ValueError("shadow worktree already exists; worktrees are never reused")
        registered = self.command(["git", "worktree", "list", "--porcelain"], self.root)
        if registered.returncode:
            raise RuntimeError(registered.stderr or registered.stdout)
        if any(line == f"worktree {worktree}" or line == f"branch refs/heads/{branch}" for line in registered.stdout.splitlines()):
            raise ValueError("shadow run ID is already registered to a worktree")
        branch_exists = self.command(["git", "show-ref", "--verify", "--quiet", f"refs/heads/{branch}"], self.root)
        if branch_exists.returncode == 0:
            raise ValueError("shadow run ID already has a local branch and cannot be reused")
        parent.mkdir(parents=True, exist_ok=True)
        result = self.command(["git", "worktree", "add", "-b", branch, str(worktree), "main"], self.root)
        if result.returncode:
            raise RuntimeError(result.stderr or result.stdout)
        return branch, worktree

    @staticmethod
    def _worktree_parent(repository_root: Path) -> Path:
        """Use a hidden sibling of the checkout, never a directory within it."""
        return repository_root.parent / f".{repository_root.name}-shadow-worktrees"

    def write_artifacts(self, worktree: Path, manifest: dict) -> tuple[Path, Path]:
        directory = worktree / "reports" / "shadow-runs"
        directory.mkdir(parents=True, exist_ok=True)
        json_path = directory / f"{manifest['run_id']}.json"
        report_path = directory / f"{manifest['run_id']}.md"
        json_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
        report_path.write_text(self.report(manifest))
        return json_path, report_path

    def local_shadow_commit(self, worktree: Path, run_id: str) -> str | None:
        """Optional one-commit helper. It never pushes, merges, or alters main."""
        if not self.policy["git"]["allow_local_commit"]:
            return None
        if not git_paths(worktree, self.command):
            return None
        add = self.command(["git", "add", "-A"], worktree)
        if add.returncode:
            raise RuntimeError(add.stderr or add.stdout)
        commit = self.command(["git", "commit", "-m", f"shadow pilot: {run_id}"], worktree)
        if commit.returncode:
            raise RuntimeError(commit.stderr or commit.stdout)
        head = self.command(["git", "rev-parse", "HEAD"], worktree)
        if head.returncode:
            raise RuntimeError(head.stderr or head.stdout)
        return head.stdout.strip()

    def allowed_path(self, bundle: str, path: str, run_id: str, approval: dict | None) -> bool:
        common = {"SYSTEM_STATUS.md", "CHANGELOG.md", f"reports/shadow-runs/{run_id}.json", f"reports/shadow-runs/{run_id}.md"}
        if path in common:
            return True
        if bundle == "discovery":
            return bool(re.fullmatch(r"research/commercial-friction-discovery/\d{4}-\d{2}-\d{2}-[^/]+\.md", path))
        if not approval:
            return False
        slug, persona_id = approval["persona_slug"], approval["persona_id"].lower()
        return path in {"config/personas.yaml", f"personas/{slug}.md", "data/observations.jsonl", "data/problems.jsonl"} or bool(re.fullmatch(rf"research/daily/\d{{4}}-\d{{2}}-\d{{2}}-{persona_id}-scout-checkpoint\.md", path)) or bool(re.fullmatch(rf"research/problem-clustering/\d{{4}}-\d{{2}}-\d{{2}}-{persona_id}-problem-clustering\.md", path))

    def evaluate(self, bundle: str, results: list[StageResult], run_id: str, approval: dict | None = None,
                 checks: dict[str, tuple[bool, bool]] | None = None, changed: dict[str, set[str]] | None = None) -> Outcome:
        checks, changed = checks or {}, changed or {}
        if not self.policy_valid(bundle):
            return Outcome("POLICY_VIOLATION", "Invalid policy or unsupported bundle.", [], [])
        required = self.policy["bundles"][bundle]["stages"]
        attempted, completed, evidence, entities, seen = [], [], {}, {"personas": [], "observations": [], "problems": []}, set()
        for index, result in enumerate(results):
            attempted.append(result.stage)
            if index >= len(required) or result.stage != required[index] or result.stage in self.policy["forbidden_stages"]:
                return Outcome("POLICY_VIOLATION", "Stage is not in this bundle's fixed graph.", attempted, completed)
            allowed_next = {"cfd": {"stop"}, "persona_resolution": {"scout"}, "scout": {"cluster", "stop"}, "cluster": {"stop"}}
            if result.next_transition not in allowed_next[result.stage]:
                return Outcome("POLICY_VIOLATION", "Stage result requested an unauthorized transition.", attempted, completed)
            if result.source_exception:
                return Outcome("SOURCE_EXCEPTION", result.source_exception, attempted, completed, evidence, entities)
            if result.safety_exception:
                return Outcome("SAFETY_BOUNDARY", result.safety_exception, attempted, completed, evidence, entities)
            if not result.completed:
                return Outcome("RUNNER_FAILED", result.reason or f"{result.stage} did not complete.", attempted, completed)
            actual = changed.get(result.stage, set())
            forbidden = sorted(path for path in actual if not self.allowed_path(bundle, path, run_id, approval))
            if forbidden:
                return Outcome("FORBIDDEN_WRITE", f"Forbidden writes: {', '.join(forbidden)}", attempted, completed, files_changed=sorted(actual))
            undeclared = sorted(path for path in actual if path not in set(result.expected_files))
            if undeclared:
                return Outcome("UNEXPECTED_DIFF", f"Undeclared writes: {', '.join(undeclared)}", attempted, completed, files_changed=sorted(actual))
            seen |= actual
            completed.append(result.stage)
            evidence.update(result.evidence)
            for key in entities:
                entities[key].extend(result.entities.get(key, []))
            if result.stage in self.policy["bundles"][bundle]["checks_after"]:
                validator_ok, tests_ok = checks.get(result.stage, (True, True))
                if not validator_ok:
                    return Outcome("VALIDATION_FAILED", f"Validator failed after {result.stage}.", attempted, completed, evidence, entities, sorted(seen), "failed", "not run")
                if not tests_ok:
                    return Outcome("TESTS_FAILED", f"Tests failed after {result.stage}.", attempted, completed, evidence, entities, sorted(seen), "passed", "failed")
            if bundle == "discovery":
                code = self.policy["bundles"][bundle]["terminal_mappings"].get(result.decision)
                return Outcome(code or "POLICY_VIOLATION", result.reason or result.decision, attempted, completed, evidence, entities, sorted(seen), "passed", "passed")
            if result.stage == "scout" and result.decision == "INSUFFICIENT_EVIDENCE":
                return Outcome("SCOUT_INSUFFICIENT_EVIDENCE", result.reason, attempted, completed, evidence, entities, sorted(seen), "passed", "passed")
            if result.stage == "cluster":
                code = self.policy["bundles"][bundle]["terminal_mappings"].get(result.decision)
                return Outcome(code or "POLICY_VIOLATION", result.reason or result.decision, attempted, completed, evidence, entities, sorted(seen), "passed", "passed")
        return Outcome("RUNNER_FAILED", "Stage result sequence ended before a terminal stop.", attempted, completed, evidence, entities, sorted(seen))

    def manifest(self, run_id: str, bundle: str, outcome: Outcome, start: str = "", branch: str = "", worktree: str = "", approval_ref: str | None = None) -> dict:
        value = {"run_id": run_id, "started_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"), "policy_version": self.policy["policy_version"], "bundle": bundle, "starting_commit": start, "branch": branch, "worktree": worktree, "approved_candidate_ref": approval_ref, "stages_attempted": outcome.stages_attempted, "stages_completed": outcome.stages_completed, "terminal_stop_code": outcome.code, "terminal_reason": outcome.reason, "evidence": outcome.evidence, "entities_created": outcome.entities, "files_changed": outcome.files_changed, "validator_result": outcome.validator_result, "tests_result": outcome.tests_result, "local_commit": None, "remote_mutated": False, "next_human_decision": outcome.next_human_decision}
        if set(value) != REQUIRED_MANIFEST_FIELDS:
            raise AssertionError("manifest contract drift")
        return value

    @staticmethod
    def report(manifest: dict) -> str:
        return "\n".join([f"# Shadow Run {manifest['run_id']}", "", f"- Bundle: `{manifest['bundle']}`", f"- Starting commit: `{manifest['starting_commit']}`", f"- Branch/worktree: `{manifest['branch']}` / `{manifest['worktree']}`", f"- Stages completed: {', '.join(manifest['stages_completed']) or 'None'}", f"- Terminal stop: `{manifest['terminal_stop_code']}`", f"- Why it stopped: {manifest['terminal_reason']}", f"- Evidence: {json.dumps(manifest['evidence'], sort_keys=True)}", f"- Entities: {json.dumps(manifest['entities_created'], sort_keys=True)}", f"- Validator/tests: {manifest['validator_result']} / {manifest['tests_result']}", f"- Changed files: {', '.join(manifest['files_changed']) or 'None'}", "- Git: local commit none; remote mutation false.", f"- Next human decision: {manifest['next_human_decision']}", ""])


def main() -> int:
    parser = argparse.ArgumentParser(description="Evaluate bounded shadow-pilot stage-result files; it never dispatches research.")
    parser.add_argument("--bundle", required=True, choices=("discovery", "approved_candidate"))
    parser.add_argument("--approved-candidate-ref", type=Path)
    args = parser.parse_args()
    controller = ShadowController()
    def checks(root: Path) -> tuple[bool, bool]:
        validator = run_command([sys.executable, "scripts/validate_repo.py"], root)
        tests = run_command([sys.executable, "-m", "unittest", "discover", "-s", "tests"], root)
        return validator.returncode == 0, tests.returncode == 0

    preflight = controller.preflight(args.bundle, args.approved_candidate_ref, checks)
    if preflight:
        print(json.dumps(controller.manifest(utc_run_id(), args.bundle, preflight), indent=2, sort_keys=True))
        return 2
    print("Controller preflight passed. A separately authorized runner must create an isolated worktree and provide structured stage results; no research was dispatched.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
