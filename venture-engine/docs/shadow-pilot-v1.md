# `shadow-pilot-v1` controller

The controller is a bounded state machine, not an autonomous research agent. `AGENTS.md` remains authoritative; the policy only narrows permissions.

The controller is the enforcement/state-machine layer. Research reasoning is supplied through the structured stage-runner interface; the controller CLI does not independently invent or dispatch unrestricted research work. This intentional boundary will be exercised by the first supervised integration pilot.

## Bundles

- `discovery`: CFD only. `REJECT`, `HOLD`, and `AUTHORIZE_SCOUT` all stop; the last requires human review before any persona or Scout work.
- `approved_candidate`: requires a human approval file containing `Shadow Bundle 2 Approval: APPROVED`, `Candidate Card:`, `Persona ID:`, and `Persona Slug:`. It may run persona resolution, Scout, and Cluster only. A zero-promotion result stops; any promoted Problem escalates. Market Analysis is unreachable.

## Running later

Run from a clean `main` baseline. The controller exposes worktree, structured-stage-result, validation, allowlist, and artifact methods for a later separately authorized runner. Its current CLI performs preflight only; it deliberately does not dispatch an LLM, browse, create a worktree, push, merge, reset, or schedule anything. When a runner uses the worktree helper, it derives the Git top-level checkout and creates a hidden sibling directory beside that checkout. A shadow worktree must never live inside the Git checkout, including inside `venture-engine/`'s enclosing project.

The default for a future runner is to preserve an isolated worktree uncommitted. The controller exposes an optional one-local-commit helper for a normal, passing terminal result. Human review decides whether to retain or remove any worktree; no automatic cleanup occurs.

## Operating status and worktree hygiene

Bundle 1 completed its initial three-run safety pilot with normal `CFD_REJECT` and `CFD_HOLD` terminal outcomes. It may now be deliberately invoked as routine bounded discovery under the unchanged `shadow-pilot-v1` policy and `manual-pilot-v2` gate. This authorizes neither a scheduler nor continuous operation. A routine normal outcome may authorize another deliberate Bundle 1 invocation without a new strategy review only when controller safety, validator, tests, write checks, and local/remote isolation all pass without an exception.

`CFD_AUTHORIZE_SCOUT_REVIEW` and every exception or enforcement code still require human/ChatGPT review. Bundle 2 remains a first-run pilot: a CFD card is never approval by itself, and its explicit human approval reference remains mandatory.

To prevent worktree accumulation, retain each completed run's card, JSON manifest, and Markdown report in the main repository before a human-directed mechanical cleanup. After that retention, an external `REJECT` or `HOLD` worktree may be removed with its local branch only when the operator has verified the retained artifacts; never delete the retained audit records. There is no automatic cleanup.

## Stage-result contract

Each result is JSON with `stage`, `completed`, `decision`, `reason`, `expected_files`, `evidence`, `entities`, `source_exception`, and `safety_exception`. The controller uses these fields—not prose—to choose its fixed stop code. A future Codex runner must write these results and may not select other stages.
