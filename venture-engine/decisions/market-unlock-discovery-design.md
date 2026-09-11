# Market Unlock Discovery (MUD) — Design Proposal

**Status:** design only; not implemented, piloted, or authorized for live discovery.  
**Relationship to CFD:** complementary parallel lens; `manual-pilot-v2` remains unchanged.

## 1. Strategic purpose

MUD detects a narrow **persona + valuable desired outcome + access barrier** where people effectively do not participate because an outcome is too expensive, complex, inaccessible, infeasible, or reserved for a better-resourced customer class. It is for non-consumption, affordability/complexity unlocks, capability democratization, newly feasible outcomes, and previously tolerated constraints.

It is not for generic inconvenience, trend/TAM scanning, technology-first ideas, minor convenience improvements, an already-paid system’s residual work, or a case where regulation, safety, physical input cost, professional judgment, or low desire is the real constraint. Existing paid systems with a recurring post-adoption bridge remain CFD territory. A candidate can be surfaced by either or both lenses; neither is subordinate.

## 2. Discovery unit and non-canonical boundary

The smallest useful MUD unit is an **access hypothesis**:

> A named persona repeatedly seeks a specific outcome, but a named barrier prevents participation or forces a consequential substitute; a bounded enabler may now make that barrier materially weaker.

It is not a persona record, Problem, Opportunity, product concept, or willingness-to-pay finding. A MUD card is dated, non-canonical triage only. It cannot create downstream entities or authorize Scout without human review.

## 3. Signal and barrier taxonomies

### Strong signals

- Repeated attributable accounts of wanting an outcome, attempting it, and abandoning/avoiding it because of one identified barrier.
- Consequential substitute behavior: paid experts, substantial DIY effort, waiting, forgone revenue, reduced participation, or avoided action.
- The same barrier affects independent users or contexts, not one bad vendor or free-tier complaint.
- A sophisticated segment achieves the outcome through costly staff, services, custom work, or infrastructure while the target segment cannot.
- Credible evidence that a defined enabling change weakens the exact barrier.

### Moderate signals

- One credible account plus a documented, repeated barrier in a second source.
- Meaningful adjacent spend or sustained effort, without proof that the barrier causes non-consumption.
- A credible enabler with a clear timing mechanism but incomplete user evidence.

### Weak or misleading signals

“People would love this,” TAM, trend reports, founder narratives, hypothetical survey interest, free-user complaints, generic friction, fashionable technology, aspirational intent without attempts, or a feature that marginally improves adequate access. These do not promote a candidate.

### Barrier taxonomy

| Potentially unlockable | Usually fundamental or excluded |
|---|---|
| Price/model mismatch; complexity/setup; expertise access; distribution/access; minimum scale; implementation burden; missing infrastructure; trust/coordination; time; technical feasibility newly changed | Legal prohibition; required licensed/professional judgment; safety boundary; irreducible physical-input cost; absent demand; unavoidable fraud/risk control; a normal process that already provides adequate access |

MUD must name one primary barrier. Multiple vague barriers are a `HOLD`, not evidence of breadth.

## 4. Latent-demand, enabler, and timing model

Latent demand requires an attributable **desire → attempt/substitute → barrier → consequence** chain. At least two independent sources must support the same chain, and the card must record why the barrier—not indifference—explains non-consumption. Acceptable behavior includes paid indirect help, sustained DIY work, repeated failed attempts, queue/wait behavior, explicit opt-out after an effort threshold, or consequential avoidance. Adjacent spending is corroboration only.

An enabler hypothesis is required but must remain at mechanism level: identify the specific barrier, the credible change that may weaken it, and why its economics/capability differ now. Do not describe a product. “AI exists” fails. A documented cost decline, infrastructure/API availability, distribution shift, changed regulation, or new hardware capability can qualify. “Why now” is corroborating evidence, not a fashionable mandatory story; an overlooked durable barrier may pass without it.

Minimum actor evidence: user and beneficiary must be directly evidenced; likely buyer and payer must be plausible from the affected behavior, adjacent spend, or existing purchasing role. A MUD card cannot claim new-category willingness to pay.

## 5. Barrier generalization and falsification

MUD replaces CFD’s stack-based structural test with **barrier generalization**: the same access barrier must recur across at least two independent user contexts, segments, geographies, or existing approaches, or credible attributable evidence must establish that the barrier is not vendor-specific. Similar aspirations alone do not count.

Immediate `REJECT` triggers: no observed attempts/consequence; an adequate free/simple alternative; fundamental legal/safety/professional barrier; only a free-tier or poor-implementation complaint; barrier attributable to one vendor; no plausible beneficiary/buyer path; or an enabler that does not change the binding constraint. Falsification must actively test low desire, market segmentation, incumbent access, price sensitivity, and whether the claimed enabler changes economics rather than presentation.

## 6. Scout-authorization gate

Recommend `AUTHORIZE_SCOUT` only when all conditions pass:

1. One narrow persona, desired outcome, and concrete access barrier are defined.
2. At least three independent attributable URLs across two source types are available, unless an access exception is documented and human review is requested rather than granted.
3. At least two independent accounts support the same desire → attempt/substitute → barrier → consequence chain.
4. The consequence is meaningful: paid indirect help, sustained labor, foregone economic/operational value, repeated abandonment, or material behavior change.
5. Evidence supports that the barrier, not low desire, is suppressing participation.
6. User and beneficiary are evidenced; buyer/payer is a grounded plausible hypothesis, with no fabricated willingness-to-pay claim.
7. The barrier generalizes across independent contexts or has credible vendor-independent support.
8. A specific enabler/why-now hypothesis could materially weaken the binding barrier; it is not technology-first speculation.
9. Incumbent, substitute, regulatory, safety, and professional-judgment falsification does not explain the case away.

`HOLD` applies when the unit is narrow and the desire/attempt chain is real but one remediable evidence gap remains—usually breadth, buyer evidence, barrier causality, or enabler proof. The card must name the exact missing proof. `REJECT` applies to any immediate-rejection trigger, speculative candidate, or multiple foundational gate failures. Neither outcome creates a persona or starts Scout.

## 7. Source model and candidate-card specification

Preferred sources: attributable practitioner and consumer communities; “how can I do X?” and abandonment discussions; professional/trade forums; verified service-marketplace demand; public pricing and capacity/wait evidence; job posts showing expert labor; product reviews of inaccessible incumbents; documented infrastructure or regulatory changes. Seek at least two source families. Treat consultant/vendor material, trend reports, startup blogs, surveys, and founder narratives as context only unless independently corroborated.

A future non-canonical MUD card must contain only these fields:

- date, MUD version, decision, and candidate slug;
- persona, desired outcome, trigger, and primary barrier;
- current behavior, attempt/substitute, consequence, and non-consumption evidence;
- indirect spend/effort and latent-demand chain;
- user, beneficiary, selector, buyer, payer, and uncertainties;
- enabler hypothesis and why-now evidence;
- incumbent/substitute and fundamental-barrier falsification;
- barrier-generalization evidence; independent URL/source-type counts and concentration;
- gate checklist, FACT/ESTIMATE/ASSUMPTION/HYPOTHESIS rationale, and later-outcome placeholder.

## 8. Coexistence, Scout, and autonomy boundaries

CFD and MUD run independently and may share source families, but every card declares its lens. A matching persona/workflow/outcome uses one cross-link rather than duplicate cards; the first card remains historical and the second records its distinct hypothesis. `CFD_REJECT` does not block MUD if the MUD case is access/non-consumption; `MUD_REJECT` does not block CFD if post-adoption residual evidence emerges. Conflicting outcomes require human review before Scout.

Scout remains unchanged. An approved MUD handoff supplies the access hypothesis and falsification targets, but Scout independently gathers canonical observations and tests whether a recurring Problem exists. It must not accept latent demand, an enabler, or willingness to pay as proven merely because MUD promoted the card.

MUD inherits all current constraints: no autonomous Scout, Market Analysis, Opportunity, scoring, experiment, outreach, spend, self-modifying gate, scheduler, or remote mutation. MUD-specific prohibitions are product concepts, technology-first selection, and using absence of spend as proof of demand.

## 9. Future controller and batch architecture

If separately implemented, use a distinct fixed **MUD Discovery Bundle** modeled on Bundle 1, not a generic parameterized controller: `preflight → MUD stage runner → checks → terminal stop`. It needs its own allowlist and terminal codes (`MUD_REJECT`, `MUD_HOLD`, `MUD_AUTHORIZE_SCOUT_REVIEW`) while sharing existing worktree, validation, audit, acceptance, and no-remote-mutation controls. Do not add it to the current controller yet.

Validate single MUD runs first. Only after successful supervised pilots should a distinct, explicitly invoked MUD batch be considered. Do not mix CFD and MUD candidates within a batch until comparative audit data exists; no schedule or alternating cadence is authorized.

## 10. Historical backtest and validation path

Before implementation, replay MUD against the existing calibration portfolio with cutoffs and source labels unchanged. Pre-register expected coverage: Shopify and Square should be evaluated as potential access/non-consumption catches; Airtable and Zapier as ambiguous; Homejoy, technology-first ideas, and low-value convenience improvements must remain rejected. Score only gate outcomes and reasons—do not tune on individual results.

Keep MUD only if it materially improves recall for its intended class, preserves the control rejection, produces auditable causal/barrier explanations, and does not generate a high volume of speculative Scout promotions. Redesign or abandon it if it mostly produces technology-first claims, cannot distinguish low demand from inaccessible demand, duplicates CFD without added recall, fails the backtest, or its falsification is routinely inconclusive.

Minimum sequence: **design review → historical backtest → review of results/proposed refinements → implementation review → one supervised shadow pilot → limited manual live pass → comparative CFD/MUD yield review**. No stage implies permission for the next one.

## 11. Naming recommendation

Keep **Market Unlock Discovery (MUD)**. It describes the target condition—an outcome unlocked for a previously excluded group—without implying a solution, market size, or guaranteed demand.
