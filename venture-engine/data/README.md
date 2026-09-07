# Data Records

The six JSONL files are deliberately empty in Phase 1. Add exactly one validated JSON object per line, never an array or Markdown. Treat additions as append-only; if a record changes, append the revised object with its same stable ID and newer `updated_at`, then document the material change.

| File | Schema | Purpose |
|---|---|---|
| `observations.jsonl` | `schemas/observation.schema.json` | Atomic, sourced findings |
| `problems.jsonl` | `schemas/problem.schema.json` | Evidence-backed clusters |
| `opportunities.jsonl` | `schemas/opportunity.schema.json` | Testable commercial hypotheses |
| `competitors.jsonl` | `schemas/competitor.schema.json` | Dated market alternatives |
| `experiments.jsonl` | `schemas/experiment.schema.json` | Pre-registered test designs |
| `experiment-results.jsonl` | `schemas/experiment-result.schema.json` | Results separate from test design |
