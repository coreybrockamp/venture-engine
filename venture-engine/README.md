# Venture Research & Validation Engine

Persistent operating system for finding, testing, and prioritizing evidence-backed venture opportunities. It intentionally separates **observations** (atomic evidence) from **problems**, **opportunities**, and **experiment results** so conclusions can be revised without losing provenance.

## Phase 1 status

Architecture, schemas, templates, operating instructions, and validation tooling are installed. No new market research, problem records, opportunities, competitors, or experiments have been seeded. Existing `../report-source.md` is preserved as a legacy research artifact and has not been imported as validated records.

## Operating flow

`persona → observation → problem → market analysis → opportunity → experiment → result → scale / iterate / kill`

Use JSONL in `data/` as the portable append-only source of truth. `database/schema.sql` defines the eventual SQLite projection; do not treat it as canonical until a documented import workflow exists. See `schemas/README.md`, `config/`, and `agents/` for controlled fields and procedures.

## Common commands

```sh
python3 scripts/validate_repo.py       # validate JSONL, IDs, dates, references, and statuses
python3 -m unittest discover -s tests  # run validation-tool tests
```

Create a record only from real, revisitable evidence. Create an approval request before any external action that requires human approval. Put resulting reports in dated folders without generating empty routine reports.

## Layout

- `personas/`: living persona profiles; unresearched sections are explicit.
- `data/`: append-only records; `schemas/` defines their shape.
- `research/`, `opportunities/`, `experiments/`, `offers/`, `validation/`: durable working artifacts by lifecycle stage.
- `agents/`, `automations/`: role and recurring-run instructions.
- `reports/`, `decisions/`: system memory and human review trail.
