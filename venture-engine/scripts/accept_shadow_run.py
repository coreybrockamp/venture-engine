#!/usr/bin/env python3
"""Mechanically retain and clean up one normal Bundle 1 shadow run.

This is intentionally separate from the controller: it never dispatches research
or changes controller policy, and it is invoked explicitly after a run stops.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
from pathlib import Path

from shadow_controller import ShadowController, is_within


class AcceptanceError(RuntimeError):
    """A shadow run is not safe for routine acceptance."""


class ShadowRunAcceptor:
    NORMAL_CODES = {"CFD_REJECT", "CFD_HOLD"}

    def __init__(self, root: Path):
        self.root = root.resolve()
        self.controller = ShadowController(self.root)

    def git(self, args: list[str], cwd: Path | None = None) -> str:
        result = subprocess.run(["git", *args], cwd=cwd or self.root, text=True, capture_output=True)
        if result.returncode:
            raise AcceptanceError(result.stderr.strip() or result.stdout.strip() or "git command failed")
        return result.stdout

    def repository_root(self) -> Path:
        return Path(self.git(["rev-parse", "--show-toplevel"]).strip()).resolve()

    @staticmethod
    def digest(path: Path) -> str:
        return hashlib.sha256(path.read_bytes()).hexdigest()

    def engine_paths(self, worktree: Path) -> set[str]:
        raw = self.git(["status", "--porcelain", "-z", "--untracked-files=all"], worktree)
        prefix = f"{self.root.name}/"
        paths: set[str] = set()
        for item in raw.split("\0"):
            if not item:
                continue
            path = item[3:]
            if not path.startswith(prefix):
                raise AcceptanceError(f"shadow diff is outside engine root: {path}")
            paths.add(path[len(prefix):])
        return paths

    def load_and_validate(self, worktree: Path, run_id: str) -> tuple[dict, set[str], Path]:
        worktree = worktree.resolve()
        repository = self.repository_root()
        if is_within(worktree, repository):
            raise AcceptanceError("shadow worktree must be outside the Git top-level checkout")
        engine = worktree / self.root.name
        manifest_path = engine / "reports" / "shadow-runs" / f"{run_id}.json"
        report_path = manifest_path.with_suffix(".md")
        if not manifest_path.is_file() or not report_path.is_file():
            raise AcceptanceError("shadow manifest or Markdown report is missing")
        manifest = json.loads(manifest_path.read_text())
        if manifest.get("run_id") != run_id or manifest.get("bundle") != "discovery":
            raise AcceptanceError("manifest does not identify this Bundle 1 run")
        if manifest.get("policy_version") != self.controller.policy.get("policy_version"):
            raise AcceptanceError("manifest policy version does not match current policy")
        if manifest.get("terminal_stop_code") not in self.NORMAL_CODES:
            raise AcceptanceError("only normal CFD_REJECT or CFD_HOLD runs may be accepted")
        if manifest.get("validator_result") != "passed" or manifest.get("tests_result") != "passed":
            raise AcceptanceError("validator and tests must both have passed")
        if manifest.get("remote_mutated") is not False:
            raise AcceptanceError("remote mutation prevents routine acceptance")
        entities = manifest.get("entities_created", {})
        if any(entities.get(key) for key in ("personas", "observations", "problems")):
            raise AcceptanceError("canonical entities prevent routine acceptance")
        declared = set(manifest.get("files_changed", []))
        required = {"SYSTEM_STATUS.md", "CHANGELOG.md", f"reports/shadow-runs/{run_id}.json", f"reports/shadow-runs/{run_id}.md"}
        if not required <= declared:
            raise AcceptanceError("manifest omits required normal-run artifacts")
        if any(path.startswith(("data/", "personas/", "config/personas")) for path in declared):
            raise AcceptanceError("manifest declares canonical changes")
        if any(not self.controller.allowed_path("discovery", path, run_id, None) for path in declared):
            raise AcceptanceError("manifest declares a forbidden Bundle 1 path")
        actual = self.engine_paths(worktree)
        if actual != declared:
            raise AcceptanceError(f"actual shadow diff does not match manifest: {sorted(actual)} != {sorted(declared)}")
        report = report_path.read_text()
        if manifest["terminal_stop_code"] not in report or manifest["terminal_reason"] not in report:
            raise AcceptanceError("Markdown report does not match manifest")
        return manifest, declared, engine

    def verify_main(self, manifest: dict) -> None:
        if self.git(["branch", "--show-current"]).strip() != "main":
            raise AcceptanceError("acceptance must run from main")
        if self.git(["status", "--porcelain"]):
            raise AcceptanceError("main must be clean before acceptance")
        starting = manifest.get("starting_commit", "")
        if not starting:
            raise AcceptanceError("manifest is missing its starting commit")
        check = subprocess.run(["git", "merge-base", "--is-ancestor", starting, "HEAD"], cwd=self.root, text=True, capture_output=True)
        if check.returncode:
            raise AcceptanceError("main has advanced incompatibly from the run starting commit")

    def accept(self, worktree: Path, run_id: str, push: bool = True, cleanup: bool = True) -> str:
        manifest, declared, engine = self.load_and_validate(worktree, run_id)
        self.verify_main(manifest)
        repository = self.repository_root()
        copied: dict[str, str] = {}
        for path in sorted(declared):
            source, target = engine / path, self.root / path
            if not source.is_file():
                raise AcceptanceError(f"declared artifact is missing: {path}")
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
            if self.digest(source) != self.digest(target):
                raise AcceptanceError(f"artifact preservation failed: {path}")
            copied[path] = self.digest(target)
        top_paths = [f"{self.root.name}/{path}" for path in sorted(copied)]
        self.git(["add", "--", *top_paths], repository)
        self.git(["commit", "-m", f"venture engine: record shadow run {run_id}"], repository)
        commit = self.git(["rev-parse", "HEAD"], repository).strip()
        if push:
            self.git(["push", "origin", "main"], repository)
        if cleanup:
            for path, expected in copied.items():
                if not (self.root / path).is_file() or self.digest(self.root / path) != expected:
                    raise AcceptanceError("retained artifact changed before cleanup")
            self.git(["worktree", "remove", "--force", str(worktree.resolve())], repository)
            self.git(["branch", "-d", manifest["branch"]], repository)
        return commit


def main() -> int:
    parser = argparse.ArgumentParser(description="Explicitly accept one normal Bundle 1 shadow run.")
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--worktree", required=True, type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    try:
        commit = ShadowRunAcceptor(root).accept(args.worktree, args.run_id)
    except AcceptanceError as error:
        print(f"ACCEPTANCE_REFUSED: {error}")
        return 2
    print(f"ACCEPTED: {args.run_id} -> {commit}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
