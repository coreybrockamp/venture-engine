# Shadow-run audit records

`shadow-pilot-v1` writes a JSON manifest and Markdown report here only from an isolated `codex/shadow/<run-id>` worktree. They are audit records, not canonical customer evidence.

Nothing reaches `main` automatically: the controller never pushes, merges, schedules itself, or starts a downstream commercial stage. Human review is required at every escalation gate and before accepting or discarding a shadow branch/worktree. After a normal `REJECT` or `HOLD` run's card and audit records are retained here, a human-directed mechanical cleanup may remove its external worktree and local branch; retained audit records are permanent.

The controller is not active until a separately authorized run supplies structured stage results. A stopped or failed worktree is preserved for audit.
