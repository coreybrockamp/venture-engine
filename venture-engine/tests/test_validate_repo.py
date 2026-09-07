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
    def run_persona_fixture(self, transform):
        sys.path.insert(0, str(ROOT / "scripts"))
        import validate_repo
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            shutil.copytree(ROOT / "schemas", temp_root / "schemas")
            shutil.copytree(ROOT / "config", temp_root / "config")
            shutil.copytree(ROOT / "personas", temp_root / "personas")
            (temp_root / "data").mkdir()
            for name in ("observations", "problems", "opportunities", "competitors", "experiments", "experiment-results"):
                (temp_root / "data" / f"{name}.jsonl").touch()
            config = temp_root / "config" / "personas.yaml"
            config.write_text(transform(config.read_text()))
            original_root, validate_repo.ROOT = validate_repo.ROOT, temp_root
            output = StringIO()
            try:
                with redirect_stdout(output): result = validate_repo.main()
            finally:
                validate_repo.ROOT = original_root
            return result, output.getvalue()

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
            shutil.copytree(ROOT / "config", temp_root / "config")
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

    def test_persona_validator_rejects_duplicate_persona_id(self):
        result, output = self.run_persona_fixture(lambda text: text.replace("persona_id: PER-002", "persona_id: PER-001"))
        self.assertEqual(result, 1)
        self.assertIn("duplicate or missing persona_id 'PER-001'", output)

    def test_persona_validator_rejects_missing_persona_file(self):
        result, output = self.run_persona_fixture(lambda text: text.replace("personas/aging-parent-caregiver.md", "personas/missing.md"))
        self.assertEqual(result, 1)
        self.assertIn("personas: missing file for PER-001", output)

    def test_persona_validator_rejects_invalid_research_status(self):
        result, output = self.run_persona_fixture(lambda text: text.replace("research_status: UNRESEARCHED", "research_status: INVALID", 1))
        self.assertEqual(result, 1)
        self.assertIn("personas: invalid research status for PER-001", output)

    def test_id_generation_empty_next_and_gaps(self):
        sys.path.insert(0, str(ROOT / "scripts"))
        import id_utils
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir); (temp_root / "data").mkdir()
            for name in ("observations", "problems", "opportunities", "competitors", "experiments"):
                (temp_root / "data" / f"{name}.jsonl").touch()
            original_root, id_utils.ROOT = id_utils.ROOT, temp_root
            try:
                self.assertEqual(id_utils.next_id("observation"), "OBS-000001")
                (temp_root / "data" / "observations.jsonl").write_text('{"observation_id":"OBS-000001"}\n{"observation_id":"OBS-000003"}\n')
                self.assertEqual(id_utils.next_id("observation"), "OBS-000004")
                self.assertEqual(id_utils.next_id("problem"), "PROB-0001")
            finally: id_utils.ROOT = original_root

    def test_validator_rejects_missing_agent_instruction(self):
        sys.path.insert(0, str(ROOT / "scripts"))
        import validate_repo
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            for name in ("schemas", "config", "personas", "agents"): shutil.copytree(ROOT / name, temp_root / name)
            (temp_root / "agents" / "scout.md").unlink()
            (temp_root / "data").mkdir()
            for name in ("observations", "problems", "opportunities", "competitors", "experiments", "experiment-results"): (temp_root / "data" / f"{name}.jsonl").touch()
            original_root, validate_repo.ROOT = validate_repo.ROOT, temp_root; output = StringIO()
            try:
                with redirect_stdout(output): self.assertEqual(validate_repo.main(), 1)
            finally: validate_repo.ROOT = original_root
            self.assertIn("missing required instruction file scout.md", output.getvalue())

    def append_fixture(self):
        sys.path.insert(0, str(ROOT / "scripts"))
        import data_utils, id_utils, validate_repo
        temp_dir = tempfile.TemporaryDirectory(); temp_root = Path(temp_dir.name)
        shutil.copytree(ROOT / "schemas", temp_root / "schemas")
        (temp_root / "data").mkdir()
        for name in ("observations", "problems", "opportunities", "competitors", "experiments", "experiment-results"):
            (temp_root / "data" / f"{name}.jsonl").touch()
        roots = (data_utils.ROOT, id_utils.ROOT, validate_repo.ROOT)
        data_utils.ROOT = id_utils.ROOT = validate_repo.ROOT = temp_root
        return temp_dir, temp_root, data_utils, id_utils, validate_repo, roots

    @staticmethod
    def valid_observation(record_id="OBS-000001"):
        return {"observation_id":record_id,"created_at":"2026-09-07T00:00:00Z","timestamp":"2026-09-07T00:00:00Z","persona_id":"PER-001","source_type":"reddit","source_url":"https://example.com/post","source_date":"2026-09-07","date_accessed":"2026-09-07","observation":"A sourced observation.","evidence_type":"problem","evidence_strength":4,"researcher_agent":"scout","confidence":70}

    def test_append_helper_valid_append(self):
        temp_dir, temp_root, data_utils, id_utils, validate_repo, roots = self.append_fixture()
        try:
            record = self.valid_observation()
            self.assertEqual(data_utils.append_valid_record("observation", record), "OBS-000001")
            lines = (temp_root / "data" / "observations.jsonl").read_text().splitlines()
            self.assertEqual(len(lines), 1); self.assertEqual(json.loads(lines[0]), record)
            self.assertEqual((temp_root / "data" / "problems.jsonl").read_text(), "")
            self.assertEqual(validate_repo.schema_errors(json.loads(lines[0]), validate_repo.load_schema("observation.schema.json")), [])
        finally:
            data_utils.ROOT, id_utils.ROOT, validate_repo.ROOT = roots; temp_dir.cleanup()

    def test_append_helper_valid_opportunity_append(self):
        temp_dir, temp_root, data_utils, id_utils, validate_repo, roots = self.append_fixture()
        try:
            record = {"opportunity_id":"OPP-0001","created_at":"2026-09-07T00:00:00Z","updated_at":"2026-09-07T00:00:00Z","persona_id":"PER-001","problem_id":"PROB-0001","opportunity_name":"x","one_sentence_pitch":"x","customer":"x","problem":"x","solution_hypothesis":"x","value_proposition":"x","key_assumptions":[],"biggest_risks":[],"opportunity_score":None,"confidence_score":None,"current_stage":"analysis","strategic_decision":None,"source_ids":[],"experiment_ids":[],"status":"researching"}
            self.assertEqual(data_utils.append_valid_record("opportunity", record), "OPP-0001")
            self.assertEqual(len((temp_root / "data" / "opportunities.jsonl").read_text().splitlines()), 1)
        finally:
            data_utils.ROOT, id_utils.ROOT, validate_repo.ROOT = roots; temp_dir.cleanup()

    def test_append_helper_rejects_duplicate_id(self):
        temp_dir, temp_root, data_utils, id_utils, validate_repo, roots = self.append_fixture()
        try:
            data_utils.append_valid_record("observation", self.valid_observation())
            with self.assertRaisesRegex(ValueError, "duplicate observation_id: OBS-000001"):
                data_utils.append_valid_record("observation", self.valid_observation())
            self.assertEqual(len((temp_root / "data" / "observations.jsonl").read_text().splitlines()), 1)
        finally:
            data_utils.ROOT, id_utils.ROOT, validate_repo.ROOT = roots; temp_dir.cleanup()

    def test_append_helper_rejects_schema_violation(self):
        temp_dir, temp_root, data_utils, id_utils, validate_repo, roots = self.append_fixture()
        try:
            invalid = self.valid_observation(); invalid["source_type"] = "not-allowed"
            with self.assertRaisesRegex(ValueError, "schema validation failed.*invalid controlled value"):
                data_utils.append_valid_record("observation", invalid)
            self.assertEqual((temp_root / "data" / "observations.jsonl").read_text(), "")
        finally:
            data_utils.ROOT, id_utils.ROOT, validate_repo.ROOT = roots; temp_dir.cleanup()

if __name__ == "__main__": unittest.main()
