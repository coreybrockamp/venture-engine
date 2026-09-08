# `shadow-pilot-v1` controller

The controller is a bounded state machine, not an autonomous research agent. `AGENTS.md` remains authoritative; the policy only narrows permissions.

The controller is the enforcement/state-machine layer. Research reasoning is supplied through the structured stage-runner interface; the controller CLI does not independently invent or dispatch unrestricted research work. This intentional boundary will be exercised by the first supervised integration pilot.

## Bundles

- `discovery`: CFD only. `REJECT`, `HOLD`, and `AUTHORIZE_SCOUT` all stop; the last requires human review before any persona or Scout work.
- `approved_candidate`: requires a human approval file containing `Shadow Bundle 2 Approval: APPROVED`, `Candidate Card:`, `Persona ID:`, and `Persona Slug:`. It may run persona resolution, Scout, and Cluster only. A zero-promotion result stops; any promoted Problem escalates. Market Analysis is unreachable.

## Running later

Run from a clean `main` baseline. The controller exposes worktree, structured-stage-result, validation, allowlist, and artifact methods for a later separately authorized runner. Its current CLI performs preflight only; it deliberately does not dispatch an LLM, browse, create a worktree, push, merge, reset, or schedule anything.

The default for a future runner is to preserve an isolated worktree uncommitted. The controller exposes an optional one-local-commit helper for a normal, passing terminal result. Human review decides whether to retain or remove any worktree; no automatic cleanup occurs.

## Stage-result contract

Each result is JSON with `stage`, `completed`, `decision`, `reason`, `expected_files`, `evidence`, `entities`, `source_exception`, and `safety_exception`. The controller uses these fields—not prose—to choose its fixed stop code. A future Codex runner must write these results and may not select other stages.
