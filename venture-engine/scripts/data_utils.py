#!/usr/bin/env python3
"""Small safe JSONL write helpers; records are appended, never silently deleted."""
from __future__ import annotations

import json
import fcntl
from pathlib import Path

from id_utils import KINDS, append_record
from validate_repo import FILES, SCHEMAS, load_schema, schema_errors

ROOT = Path(__file__).resolve().parents[1]

def _plural(kind: str) -> str:
    return {"opportunity": "opportunities", "result": "results"}.get(kind, f"{kind}s")

def load_records(kind: str) -> list[dict]:
    filename = FILES[f"{kind}s" if kind == "observation" else f"{kind}s"][0]
    return [json.loads(line) for line in (ROOT / "data" / filename).read_text().splitlines() if line.strip()]

def append_valid_record(kind: str, record: dict) -> str:
    """Validate a candidate then atomically allocate/check ID and append it."""
    plural = _plural(kind)
    errors = schema_errors(record, load_schema(SCHEMAS[plural]))
    if errors:
        raise ValueError("schema validation failed: " + "; ".join(errors))
    return append_record(kind, record)

def update_valid_record(kind: str, record: dict) -> str:
    """Validate and atomically replace one existing record while retaining its ID."""
    plural = _plural(kind)
    errors = schema_errors(record, load_schema(SCHEMAS[plural]))
    if errors:
        raise ValueError("schema validation failed: " + "; ".join(errors))
    id_field = f"{kind}_id"
    record_id = record.get(id_field)
    if not record_id:
        raise ValueError(f"missing {id_field}")
    filename = FILES[plural][0]
    target = ROOT / "data" / filename
    lock_path = ROOT / "data" / ".id-allocation.lock"
    with lock_path.open("a+") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        rows = [json.loads(line) for line in target.read_text().splitlines() if line.strip()]
        matches = [index for index, row in enumerate(rows) if row.get(id_field) == record_id]
        if len(matches) != 1:
            raise ValueError(f"expected one existing {id_field}: {record_id}")
        rows[matches[0]] = record
        temporary = target.with_suffix(target.suffix + ".tmp")
        temporary.write_text("".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows))
        temporary.replace(target)
        fcntl.flock(lock, fcntl.LOCK_UN)
    return record_id
