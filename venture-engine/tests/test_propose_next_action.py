"""Read-only supervisor proposals; every API interaction is mocked."""
from __future__ import annotations

import hashlib
import io
import json
import os
import sys
import tempfile
import types
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import propose_next_action as supervisor


class ProposalTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.top = Path(self.temp.name)
        self.root = self.top / "venture-engine"
        self._put(self.top / "AGENTS.md", "# Venture Research & Validation Engine — Agent Constitution\n")
        self._put(self.root / "AGENTS.md", "# Local Agent Entry Point\nRead ../AGENTS.md.\n")
        policy = Path(__file__).resolve().parents[1] / "config" / "shadow-autonomy.yaml"
        self._put(self.root / "config" / "shadow-autonomy.yaml", policy.read_text())
        self._put(self.root / "config" / "personas.yaml", "personas: []\n")
        self._put(self.root / "data" / "observations.jsonl", "")
        self._put(self.root / "research" / "commercial-friction-discovery" / "card.md",
                  "**Decision:** `AUTHORIZE_SCOUT` — recommendation only.\n")
        self._put(self.root / "decisions" / "shadow-bundle2-approval-2026-09-29-per-014.md",
                  "Shadow Bundle 2 Approval: APPROVED\n"
                  "Candidate Card: research/commercial-friction-discovery/card.md\n"
                  "Persona ID: PER-014\nPersona Slug: outpatient-prior-authorization-operations-lead\n")
        self._put(self.root / "reports" / "shadow-runs" / "SHADOW-20260930T014214Z-0001.json",
                  json.dumps({"run_id": "SHADOW-20260930T014214Z-0001", "bundle": "discovery",
                              "policy_version": "shadow-pilot-v1", "terminal_stop_code": "CFD_AUTHORIZE_SCOUT_REVIEW",
                              "files_changed": ["research/commercial-friction-discovery/card.md"]}))
        self._status()
        baseline = patch.object(supervisor, "_baseline_ok", return_value=True)
        baseline.start()
        self.addCleanup(baseline.stop)
        shadow = patch.object(supervisor, "_unretained_shadow_worktree", return_value=False)
        shadow.start()
        self.addCleanup(shadow.stop)

    @staticmethod
    def _put(path: Path, content: str):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)

    def _status(self, workstream=None, action=None):
        workstream = workstream or ("**No active persona pipeline.**\n"
            "Approved `PER-014` from `SHADOW-20260930T014214Z-0001` in "
            "`decisions/shadow-bundle2-approval-2026-09-29-per-014.md`.\n")
        action = action or ("Run the first supervised `shadow-pilot-v1` Bundle 2 pilot for the approved "
            "`PER-014` candidate using the valid human-approval reference. Stop after Cluster.\n")
        self._put(self.root / "SYSTEM_STATUS.md",
                  f"# System Status\n\n## Current Workstream\n\n{workstream}\n\n## NEXT ACTION\n\n{action}\n")

    @staticmethod
    def _proposal(action=supervisor.BUNDLE_2, state="BUNDLE_2_APPROVED_PENDING", approval=False):
        return {"current_state": state, "next_permitted_action": action,
                "rationale": "The explicit approval and fixed graph permit this proposal.",
                "human_approval_required": approval}

    def test_valid_permitted_proposal(self):
        result, valid = supervisor.propose(self.root, lambda _: self._proposal())
        self.assertTrue(valid)
        self.assertEqual(result["next_permitted_action"], supervisor.BUNDLE_2)

    def test_explicit_human_review_proposal(self):
        result, valid = supervisor.propose(self.root, lambda _: self._proposal(supervisor.STOP))
        self.assertTrue(valid)
        self.assertTrue(result["human_approval_required"])

    def test_bundle_one_still_requires_deliberate_human_invocation(self):
        self._status(workstream="**No active persona pipeline.**\nOperational Bundle 1.\n",
                     action="Run the next routine bounded Bundle 1 discovery batch with --max-runs 5.\n")
        result, valid = supervisor.propose(self.root, lambda _: self._proposal(
            supervisor.BUNDLE_1, "BUNDLE_1_READY", approval=False))
        self.assertTrue(valid)
        self.assertTrue(result["human_approval_required"])

    def test_unsupported_action_fails_closed(self):
        result, valid = supervisor.propose(self.root, lambda _: self._proposal("RUN_MARKET_ANALYSIS"))
        self.assertFalse(valid)
        self.assertEqual(result["next_permitted_action"], supervisor.STOP)

    def test_contradictory_repository_state_fails_before_model_call(self):
        self._put(self.root / "config" / "personas.yaml", "- {persona_id: PER-014}\n")
        called = []
        result, valid = supervisor.propose(self.root, lambda _: called.append(True))
        self.assertFalse(valid)
        self.assertFalse(called)
        self.assertEqual(result["current_state"], "HUMAN_REVIEW_REQUIRED")

    def test_malformed_model_output_fails_closed(self):
        for malformed in ("not JSON", {"current_state": "BUNDLE_2_APPROVED_PENDING"},
                          dict(self._proposal(), extra="unexpected"), dict(self._proposal(), human_approval_required="false")):
            with self.subTest(malformed=malformed):
                result, valid = supervisor.propose(self.root, lambda _: malformed)
                self.assertFalse(valid)
                self.assertEqual(result["next_permitted_action"], supervisor.STOP)

    def test_model_error_and_refusal_fail_closed(self):
        def error(_):
            raise RuntimeError("simulated API failure")
        result, valid = supervisor.propose(self.root, error)
        self.assertFalse(valid)
        self.assertEqual(result["next_permitted_action"], supervisor.STOP)
        response = types.SimpleNamespace(status="completed", output_text="", output=[])
        client = types.SimpleNamespace(responses=types.SimpleNamespace(create=lambda **_: response))
        with patch.dict(os.environ, {"OPENAI_API_KEY": "test-only"}), patch.dict(sys.modules, {"openai": types.SimpleNamespace(OpenAI=lambda **_: client)}):
            result, valid = supervisor.propose(self.root, supervisor.call_model)
        self.assertFalse(valid)
        self.assertIn("refused or incomplete", result["rationale"])

        refusal = types.SimpleNamespace(status="completed", output_text=json.dumps(self._proposal()),
                                        output=[types.SimpleNamespace(content=[types.SimpleNamespace(type="refusal")])])
        client.responses.create = lambda **_: refusal
        with patch.dict(os.environ, {"OPENAI_API_KEY": "test-only"}), patch.dict(sys.modules, {"openai": types.SimpleNamespace(OpenAI=lambda **_: client)}):
            result, valid = supervisor.propose(self.root, supervisor.call_model)
        self.assertFalse(valid)
        self.assertIn("model refused", result["rationale"])

    def test_official_client_request_is_schema_constrained_and_not_stored(self):
        requests = []
        response = types.SimpleNamespace(status="completed", output_text=json.dumps(self._proposal()), output=[])
        client = types.SimpleNamespace(responses=types.SimpleNamespace(
            create=lambda **kwargs: requests.append(kwargs) or response))
        with patch.dict(os.environ, {"OPENAI_API_KEY": "test-only"}), patch.dict(sys.modules, {"openai": types.SimpleNamespace(OpenAI=lambda **_: client)}):
            result, valid = supervisor.propose(self.root, supervisor.call_model)
        self.assertTrue(valid)
        self.assertEqual(result["next_permitted_action"], supervisor.BUNDLE_2)
        self.assertEqual(len(requests), 1)
        self.assertFalse(requests[0]["store"])
        self.assertEqual(requests[0]["text"]["format"]["type"], "json_schema")
        self.assertTrue(requests[0]["text"]["format"]["strict"])

    def test_model_cannot_override_missing_approval(self):
        (self.root / "decisions" / "shadow-bundle2-approval-2026-09-29-per-014.md").unlink()
        result, valid = supervisor.propose(self.root, lambda _: self._proposal(approval=False))
        self.assertFalse(valid)
        self.assertEqual(result["next_permitted_action"], supervisor.STOP)
        self.assertTrue(result["human_approval_required"])

    def test_run_audit_mismatch_fails_before_model_call(self):
        (self.root / "reports" / "shadow-runs" / "SHADOW-20260930T014214Z-0001.json").unlink()
        called = []
        result, valid = supervisor.propose(self.root, lambda _: called.append(True))
        self.assertFalse(valid)
        self.assertFalse(called)
        self.assertEqual(result["next_permitted_action"], supervisor.STOP)

    def test_dirty_baseline_fails_before_model_call(self):
        with patch.object(supervisor, "_baseline_ok", return_value=False):
            result, valid = supervisor.propose(self.root, lambda _: self._proposal())
        self.assertFalse(valid)
        self.assertEqual(result["next_permitted_action"], supervisor.STOP)

    def test_unretained_shadow_worktree_fails_before_model_call(self):
        with patch.object(supervisor, "_unretained_shadow_worktree", return_value=True):
            result, valid = supervisor.propose(self.root, lambda _: self._proposal())
        self.assertFalse(valid)
        self.assertEqual(result["next_permitted_action"], supervisor.STOP)

    def test_no_repository_writes_and_stdout_json(self):
        def digests():
            return {str(path.relative_to(self.top)): hashlib.sha256(path.read_bytes()).hexdigest()
                    for path in self.top.rglob("*") if path.is_file()}
        before = digests()
        output = io.StringIO()
        with patch.object(supervisor, "ROOT", self.root), patch.object(supervisor, "call_model", lambda _: self._proposal()), redirect_stdout(output):
            self.assertEqual(supervisor.main(), 0)
        self.assertEqual(digests(), before)
        self.assertEqual(json.loads(output.getvalue())["next_permitted_action"], supervisor.BUNDLE_2)


if __name__ == "__main__":
    unittest.main()
