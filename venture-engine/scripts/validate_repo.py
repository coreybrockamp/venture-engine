#!/usr/bin/env python3
"""Dependency-free integrity checks for append-only Venture Engine JSONL."""
from __future__ import annotations

import json
import re
import sys
from datetime import date, datetime
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
FILES = {
    "observations": ("observations.jsonl", "observation_id", r"OBS-\d{6}", ["created_at", "timestamp", "persona_id", "source_type", "source_url", "source_date", "date_accessed", "observation", "evidence_type", "evidence_strength", "researcher_agent", "confidence"]),
    "problems": ("problems.jsonl", "problem_id", r"PROB-\d{4}", ["created_at", "updated_at", "persona_id", "problem_statement", "job_to_be_done", "problem_category", "confidence_score", "evidence_strength", "source_observation_ids", "status", "date_last_validated"]),
    "opportunities": ("opportunities.jsonl", "opportunity_id", r"OPP-\d{4}", ["created_at", "updated_at", "persona_id", "problem_id", "opportunity_name", "opportunity_score", "confidence_score", "current_stage", "strategic_decision", "source_ids", "experiment_ids", "status"]),
    "competitors": ("competitors.jsonl", "competitor_id", r"COMP-\d{4}", ["created_at", "updated_at", "name", "website", "category", "related_problem_ids", "related_opportunity_ids", "pricing_last_checked", "source_ids", "status"]),
    "experiments": ("experiments.jsonl", "experiment_id", r"EXP-\d{4}", ["opportunity_id", "created_at", "hypothesis", "persona_id", "problem_id", "offer", "channel", "primary_metric", "success_threshold", "failure_threshold", "kill_criteria", "status", "human_approval_required"]),
    "results": ("experiment-results.jsonl", "experiment_id", r"EXP-\d{4}", ["recorded_at", "result", "interpretation", "confidence", "recommended_action"]),
}
STATUSES = {"problems": {"candidate", "researching", "validated", "deprioritized", "rejected", "archived"}, "opportunities": {"researching", "active", "testing", "winner", "rejected", "archived"}, "competitors": {"active", "inactive", "acquired", "shutdown", "unknown"}, "experiments": {"proposed", "approved", "active", "completed", "paused", "killed"}}
SCHEMAS = {"observations": "observation.schema.json", "problems": "problem.schema.json", "opportunities": "opportunity.schema.json", "competitors": "competitor.schema.json", "experiments": "experiment.schema.json", "results": "experiment-result.schema.json"}

def valid_date(value: str) -> bool:
    try: date.fromisoformat(value[:10]); return True
    except (TypeError, ValueError): return False

def valid_datetime(value: str) -> bool:
    try:
        datetime.fromisoformat(value.replace("Z", "+00:00"))
        return "T" in value
    except (AttributeError, ValueError): return False

def load_schema(filename: str) -> dict:
    """Resolve the one-file local references used by public schema entry points."""
    path = ROOT / "schemas" / filename
    schema = json.loads(path.read_text())
    if "$ref" in schema:
        return load_schema(schema["$ref"])
    return schema

def schema_errors(value, schema, field="record"):
    """Small dependency-free JSON Schema subset used by this repository's contracts."""
    errors = []
    if "required" in schema and isinstance(value, dict):
        for required in schema["required"]:
            if required not in value: errors.append(f"{field}: missing required field {required}")
    if "additionalProperties" in schema and schema["additionalProperties"] is False and isinstance(value, dict):
        unknown = set(value) - set(schema.get("properties", {}))
        for name in sorted(unknown): errors.append(f"{field}: unknown field {name}")
    for name, child in schema.get("properties", {}).items():
        if isinstance(value, dict) and name in value:
            errors.extend(schema_errors(value[name], child, f"{field}.{name}"))
    expected = schema.get("type")
    if expected:
        types = expected if isinstance(expected, list) else [expected]
        checks = {"object": lambda x: isinstance(x, dict), "array": lambda x: isinstance(x, list), "string": lambda x: isinstance(x, str), "integer": lambda x: isinstance(x, int) and not isinstance(x, bool), "number": lambda x: isinstance(x, (int, float)) and not isinstance(x, bool), "boolean": lambda x: isinstance(x, bool), "null": lambda x: x is None}
        if not any(checks[item](value) for item in types): return [f"{field}: expected {' or '.join(types)}"]
    if "enum" in schema and value not in schema["enum"]: errors.append(f"{field}: invalid controlled value {value!r}")
    if isinstance(value, str):
        if "pattern" in schema and not re.fullmatch(schema["pattern"], value): errors.append(f"{field}: does not match required pattern")
        if schema.get("minLength") and len(value) < schema["minLength"]: errors.append(f"{field}: shorter than minimum length")
        if schema.get("format") == "date" and not valid_date(value): errors.append(f"{field}: malformed date")
        if schema.get("format") == "date-time" and not valid_datetime(value): errors.append(f"{field}: malformed timestamp")
        if schema.get("format") == "uri" and not urlparse(value).scheme: errors.append(f"{field}: malformed URI")
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        if "minimum" in schema and value < schema["minimum"]: errors.append(f"{field}: below minimum")
        if "maximum" in schema and value > schema["maximum"]: errors.append(f"{field}: above maximum")
    if isinstance(value, list) and "items" in schema:
        for index, child in enumerate(value): errors.extend(schema_errors(child, schema["items"], f"{field}[{index}]"))
    return errors

def load(kind, errors):
    filename, key, pattern, required = FILES[kind]
    records, ids = [], set()
    path = ROOT / "data" / filename
    schema = load_schema(SCHEMAS[kind])
    for number, raw in enumerate(path.read_text().splitlines(), 1):
        if not raw.strip(): continue
        try: record = json.loads(raw)
        except json.JSONDecodeError as exc: errors.append(f"{filename}:{number}: invalid JSON ({exc.msg})"); continue
        errors.extend(f"{filename}:{number}: {error}" for error in schema_errors(record, schema))
        missing = [field for field in required if field not in record]
        if missing: errors.append(f"{filename}:{number}: missing {', '.join(missing)}")
        value = record.get(key, "")
        if not re.fullmatch(pattern, str(value)): errors.append(f"{filename}:{number}: invalid {key} {value!r}")
        if value in ids: errors.append(f"{filename}:{number}: duplicate {key} {value}")
        ids.add(value)
        for field in ("source_date", "date_accessed", "date_checked", "start_date", "end_date", "date_last_validated"):
            if record.get(field) is not None and not valid_date(record[field]): errors.append(f"{filename}:{number}: malformed date in {field}")
        for field in ("timestamp", "created_at", "updated_at", "recorded_at"):
            if record.get(field) is not None and not valid_datetime(record[field]): errors.append(f"{filename}:{number}: malformed timestamp in {field}")
        if kind in STATUSES and record.get("status") not in STATUSES[kind]: errors.append(f"{filename}:{number}: invalid status {record.get('status')!r}")
        records.append(record)
    return records, ids

def main():
    errors, all_records, all_ids = [], {}, {}
    for kind in FILES: all_records[kind], all_ids[kind] = load(kind, errors)
    valid_personas = {f"PER-{n:03d}" for n in range(1, 11)}
    for kind, records in all_records.items():
        for record in records:
            if "persona_id" in record and record["persona_id"] not in valid_personas: errors.append(f"{kind}: orphan persona {record['persona_id']}")
            if kind == "problems":
                for ref in record.get("source_observation_ids", record.get("source_ids", [])):
                    if ref not in all_ids["observations"]: errors.append(f"problems: {record['problem_id']} references missing {ref}")
            if kind == "opportunities":
                if record.get("problem_id") not in all_ids["problems"]: errors.append(f"opportunities: {record['opportunity_id']} references missing {record.get('problem_id')}")
                for ref in record.get("experiment_ids", []):
                    if ref not in all_ids["experiments"]: errors.append(f"opportunities: {record['opportunity_id']} references missing {ref}")
            if kind == "experiments" and record.get("opportunity_id") not in all_ids["opportunities"]:
                errors.append(f"experiments: {record['experiment_id']} references missing {record.get('opportunity_id')}")
            if kind == "experiments" and record.get("problem_id") not in all_ids["problems"]:
                errors.append(f"experiments: {record['experiment_id']} references missing problem {record.get('problem_id')}")
            if kind == "results" and record.get("experiment_id") not in all_ids["experiments"]:
                errors.append(f"results: references missing {record.get('experiment_id')}")
            if kind == "competitors":
                for ref in record.get("related_problem_ids", []):
                    if ref not in all_ids["problems"]: errors.append(f"competitors: {record['competitor_id']} references missing {ref}")
                for ref in record.get("related_opportunity_ids", []):
                    if ref not in all_ids["opportunities"]: errors.append(f"competitors: {record['competitor_id']} references missing {ref}")
    if errors:
        print("Validation failed:", *[f"- {e}" for e in errors], sep="\n"); return 1
    print("Validation passed: no malformed records or broken references found."); return 0

if __name__ == "__main__": sys.exit(main())
