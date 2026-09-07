# Decision Log

| Date | Decision | Context | Alternatives | Reason | Expected impact | Revisit date |
|---|---|---|---|---|---|---|
| 2026-09-07 | Use JSONL as initial canonical record store; define SQLite as a future projection. | Phase 1 needs portable, reviewable, append-friendly records. | SQLite-first; Markdown-only. | JSONL preserves append history and supports simple validation without infrastructure. | Reliable early capture and later migration. | After first complete research workflow. |
| 2026-09-07 | Keep existing `report-source.md` outside the structured database. | Its claims predate this system’s source-validation process. | Import immediately; delete it. | Preserve work without presenting it as newly validated evidence. | Avoids provenance inflation. | During a reviewed import pass. |
