# Record Schemas

The singular schema names (`observation.schema.json`, `problem.schema.json`, and so on) are the public contract entry points. They reference the existing plural implementation files so prior paths remain compatible. JSON Schema files define one JSON object per line in the matching `data/*.jsonl` file. Required fields protect identity, provenance, and lifecycle state; optional fields support progressively richer research. Empty JSONL files are valid at Phase 1.

Relationships: observations may nominate a candidate problem; problems cite observation IDs; opportunities cite a persona and problem; experiments cite opportunities; results cite experiments. IDs are never reused. Validate with `scripts/validate_repo.py` before handoff.

Canonical vocabulary definitions live in `config/system-settings.yaml`: evidence strength is 1–5, confidence is 0–100, and statuses/stages/decisions are listed there. Problem `source_observation_ids`, opportunity `source_ids`/`experiment_ids`, and competitor `related_problem_ids`/`related_opportunity_ids` are deliberate many-to-many links. Use `null` only where a schema explicitly allows an unknown or not-yet-researched value; do not invent placeholders. Append historical revisions with timestamps, retain contradiction and decision history, and update an existing stable-ID record rather than create a duplicate.

`schema.sql` mirrors these core records in SQLite for future querying. JSONL remains canonical until an import and migration procedure is approved and documented.
