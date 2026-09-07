#!/usr/bin/env python3
"""Safe stable-ID allocation and JSONL append helpers for Venture Engine records."""
from __future__ import annotations

import fcntl
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KINDS = {
    "persona": ("PER", 3, "personas.yaml"),
    "observation": ("OBS", 6, "observations.jsonl"),
    "problem": ("PROB", 4, "problems.jsonl"),
    "opportunity": ("OPP", 4, "opportunities.jsonl"),
    "experiment": ("EXP", 4, "experiments.jsonl"),
    "competitor": ("COMP", 4, "competitors.jsonl"),
}

def _record_ids(kind: str) -> set[str]:
    prefix, width, filename = KINDS[kind]
    if filename == "personas.yaml":
        return {f"PER-{number:03d}" for number in range(1, 11)}
    path = ROOT / "data" / filename
    return {json.loads(line).get(f"{kind}_id") for line in path.read_text().splitlines() if line.strip()}

def next_id(kind: str) -> str:
    """Return the next unused ID. Use append_record for a race-safe allocation + write."""
    prefix, width, _ = KINDS[kind]
    ids = _record_ids(kind)
    values = [int(match.group(1)) for item in ids if item and (match := re.fullmatch(fr"{prefix}-(\d{{{width}}})", item))]
    return f"{prefix}-{(max(values, default=0) + 1):0{width}d}"

def append_record(kind: str, record: dict) -> str:
    """Allocate/check the entity ID and append one JSON record while holding a file lock."""
    if kind not in KINDS or kind == "persona":
        raise ValueError("kind must be a non-persona entity kind")
    _, _, filename = KINDS[kind]
    id_field = f"{kind}_id"
    lock_path = ROOT / "data" / ".id-allocation.lock"
    with lock_path.open("a+") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        record_id = record.get(id_field) or next_id(kind)
        if record_id in _record_ids(kind):
            raise ValueError(f"duplicate {id_field}: {record_id}")
        record[id_field] = record_id
        with (ROOT / "data" / filename).open("a") as target:
            target.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")
        fcntl.flock(lock, fcntl.LOCK_UN)
    return record_id
