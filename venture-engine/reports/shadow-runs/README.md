# Shadow-run audit records

`shadow-pilot-v1` writes a JSON manifest and Markdown report here only from an isolated `codex/shadow/<run-id>` worktree. They are audit records, not canonical customer evidence.

Nothing reaches `main` from the controller itself: it never pushes, merges, schedules itself, or starts a downstream commercial stage. Human review is required at every escalation gate. A separately initiated routine batch may accept only a passed normal `REJECT` or `HOLD` through the same acceptance helper, then remove that completed external worktree and local branch; retained audit records are permanent.

The controller is not active until a separately authorized run supplies structured stage results. A stopped or failed worktree is preserved for audit.

Routine foreground batches may additionally retain JSON and Markdown operational summaries in `batches/`. They summarize individual run manifests/reports; they do not replace those records or establish customer evidence. A batch never schedules itself and stops before Bundle 2 or Scout.
