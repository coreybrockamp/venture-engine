import subprocess
import sys
import json
import shutil
import tempfile
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class ValidateRepoTests(unittest.TestCase):
    def test_empty_phase_one_records_are_valid(self):
        result = subprocess.run([sys.executable, "scripts/validate_repo.py"], cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("Validation passed", result.stdout)

    def test_schema_rejects_unknown_fields_and_bad_timestamps(self):
        sys.path.insert(0, str(ROOT / "scripts"))
        from validate_repo import load_schema, schema_errors
        record = {"observation_id": "OBS-000001", "timestamp": "not-a-timestamp", "unexpected": True}
        errors = schema_errors(record, load_schema("observation.schema.json"))
        self.assertTrue(any("unknown field unexpected" in error for error in errors))
        self.assertTrue(any("malformed timestamp" in error for error in errors))

    def test_missing_required_field_is_rejected(self):
        sys.path.insert(0, str(ROOT / "scripts"))
        from validate_repo import load_schema, schema_errors
        errors = schema_errors({"observation_id": "OBS-000001"}, load_schema("observation.schema.json"))
        self.assertTrue(any("missing required field created_at" in error for error in errors))

    def test_opportunity_retest_is_rejected(self):
        sys.path.insert(0, str(ROOT / "scripts"))
        from validate_repo import load_schema, schema_errors
        record = {"opportunity_id":"OPP-0001","created_at":"2026-09-07T00:00:00Z","updated_at":"2026-09-07T00:00:00Z","persona_id":"PER-001","problem_id":"PROB-0001","opportunity_name":"x","one_sentence_pitch":"x","customer":"x","problem":"x","solution_hypothesis":"x","value_proposition":"x","key_assumptions":[],"biggest_risks":[],"opportunity_score":1,"confidence_score":1,"current_stage":"researching","strategic_decision":"RETEST","source_ids":[],"experiment_ids":[],"status":"researching"}
        errors = schema_errors(record, load_schema("opportunity.schema.json"))
        self.assertTrue(any("invalid controlled value 'RETEST'" in error for error in errors))

    def test_experiment_result_retest_is_valid(self):
        sys.path.insert(0, str(ROOT / "scripts"))
        from validate_repo import load_schema, schema_errors
        record = {"experiment_id":"EXP-0001","recorded_at":"2026-09-07T00:00:00Z","result":"inconclusive","interpretation":"needs more data","confidence":25,"recommended_action":"RETEST"}
        self.assertEqual(schema_errors(record, load_schema("experiment-result.schema.json")), [])

    def test_validator_rejects_duplicate_ids_and_broken_references(self):
        sys.path.insert(0, str(ROOT / "scripts"))
        import validate_repo
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            shutil.copytree(ROOT / "schemas", temp_root / "schemas")
            (temp_root / "data").mkdir()
            for name in ("observations", "problems", "opportunities", "competitors", "experiments", "experiment-results"):
                (temp_root / "data" / f"{name}.jsonl").touch()
            (temp_root / "data" / "observations.jsonl").write_text('{"observation_id":"OBS-000001"}\n{"observation_id":"OBS-000001"}\n')
            (temp_root / "data" / "problems.jsonl").write_text('{"problem_id":"PROB-0001","source_observation_ids":["OBS-999999"]}\n')
            original_root, validate_repo.ROOT = validate_repo.ROOT, temp_root
            output = StringIO()
            try:
                with redirect_stdout(output): self.assertEqual(validate_repo.main(), 1)
            finally:
                validate_repo.ROOT = original_root
            self.assertIn("duplicate observation_id", output.getvalue())
            self.assertIn("references missing OBS-999999", output.getvalue())

if __name__ == "__main__": unittest.main()
