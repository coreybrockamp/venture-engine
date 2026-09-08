# Commercial Friction Discovery

## Role

Commercial Friction Discovery (CFD) is a manual, human-reviewed pre-Scout target-selection mode. It identifies narrowly defined persona/workflow candidates whose attributable preliminary evidence suggests commercial friction worth a full Scout pass.

Read the root `AGENTS.md` before acting.

## Purpose and boundary

CFD answers only: *Which persona/workflow deserves a full Scout pass?* It may begin with a broad industry or workflow hypothesis and does not require a predefined persona.

CFD creates a dated Markdown candidate card only. It is not a canonical evidence stage. A later Scout must independently verify sources and create canonical observations before any Problem, Market Analysis, Opportunity, score, experiment, or decision can exist.

## Inputs

- Broad industry or workflow hypotheses.
- Existing persona catalog and unused personas where relevant.
- Prior portfolio rejection patterns.
- Public source universe and source-access constraints.
- Approved safety, legal, regulatory, and no-go boundaries.

## Explicit non-goals

Do not create formal Observations, Problems, competitors, Opportunities, scores, experiments, offers, product concepts, or persona records. Do not conduct full Market Analysis. Do not conclude that willingness to pay for a new product is established. Do not authorize Scout without required human review.

## Signal taxonomy

### Strong

- Multiple independent accounts of duplicate or reconciliation work after paid adoption.
- Paid human labor bridging tools.
- Recurring costly errors after incumbent adoption.
- Switching while continuing to pay.
- A documented recurring workaround tied to a clear buyer.

### Moderate

- One credible post-adoption account plus a known paid stack.
- Repeated manual workflow with plausible economic cost.
- Integration requests while using named paid tools.
- Recurring cross-vendor handoffs.

### Weak or misleading

- Generic complaints, large TAM, category spend alone, or trendiness.
- Isolated bugs, free-user complaints, bad implementation, or poor provider quality.
- Vague “too many tools” complaints.
- Pain adequately solved by normal process.

## Required research behavior

Use attributable sources and direct links. Preserve contradictory evidence and actively try to falsify the candidate. Separate **FACT**, **ESTIMATE**, **ASSUMPTION**, **HYPOTHESIS**, and **OPINION**. Never invent a buyer, payer, willingness-to-pay claim, paid workaround, or commercial consequence. Do not propose a solution.

## Scout-authorization gate

Recommend `AUTHORIZE_SCOUT` only when every condition is satisfied:

1. A narrow persona and concrete recurring workflow are defined.
2. At least three independent URLs across at least two source types are attributable, where available.
3. At least two post-adoption signals show the same operational mechanism.
4. Direct evidence links that mechanism to paid software, paid labor, contractor/consultant work, or measurable economic cost.
5. A plausible user, selector, buyer, and payer hypothesis is grounded in evidence.
6. A quick absorption check does not show the issue is plainly an isolated defect, poor implementation, clinical/professional judgment, or a workflow normal process already solves.

If any condition fails, the only permitted outcomes are `HOLD` or `REJECT`. The card must state the missing evidence and preserve the disconfirmation.

## Output and handoff

Use `research/commercial-friction-discovery/TEMPLATE.md` for each dated candidate card. State source limitations, the gate result, rationale, and placeholders for later outcomes. Human review is mandatory before any persona selection or Scout authorization. The first canonical handoff is an independently authorized Scout pass.
