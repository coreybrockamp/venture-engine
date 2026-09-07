#!/usr/bin/env python3
"""Small safe JSONL write helpers; records are appended, never silently deleted."""
from __future__ import annotations

import json
from pathlib import Path

from id_utils import KINDS, append_record
from validate_repo import FILES, SCHEMAS, load_schema, schema_errors

ROOT = Path(__file__).resolve().parents[1]

def load_records(kind: str) -> list[dict]:
    filename = FILES[f"{kind}s" if kind == "observation" else f"{kind}s"][0]
    return [json.loads(line) for line in (ROOT / "data" / filename).read_text().splitlines() if line.strip()]

def append_valid_record(kind: str, record: dict) -> str:
    """Validate a candidate then atomically allocate/check ID and append it."""
    plural = {"opportunity": "opportunities", "result": "results"}.get(kind, f"{kind}s")
    errors = schema_errors(record, load_schema(SCHEMAS[plural]))
    if errors:
        raise ValueError("schema validation failed: " + "; ".join(errors))
    return append_record(kind, record)
