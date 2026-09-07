# Operational Integrity Procedure

Before every agent run, run `python3 venture-engine/scripts/validate_repo.py`. If it fails: **STOP → report the issue → preserve data → repair → re-run validation**. Run the same command after every meaningful write before handing off.

Use `generate_id.py observation` (or another supported entity) only to inspect the next ID. Use `data_utils.append_valid_record()` for writes: it validates the schema, checks IDs under a lock, and appends exactly one JSONL line. It does not silently update or delete history. Updates require an explicitly documented, auditable revision workflow.

Fixtures belong in tests or temporary directories, never `data/`. The validator verifies contracts and references; it cannot prove source truth, prevent a human from manually editing files, or enforce append-only history outside these helpers.
