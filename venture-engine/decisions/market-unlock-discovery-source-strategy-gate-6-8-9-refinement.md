# MUD Source Strategy — Gate 6/8/9 Narrow Refinement

**Status:** design only; not implemented, piloted, or authorized for live discovery.  
**Scope:** a late-stage evidence module for Gate 6 (buyer/payer), Gate 8 (barrier-specific enabler), and Gate 9 (alternative/fundamental-constraint falsification). It preserves the approved MUD gate and broader source strategy.

## 1. Objective and deterministic activation

This refinement improves observability for the three remaining role gaps without revisiting desire, attempt, barrier, consequence, or generalization sourcing. Activate it only when Gates **1–5 and 7** are supported by attributable evidence, Gate 8 has no substantive contradiction, and no immediate-rejection trigger has appeared. Otherwise stop under the existing ladder.

The trigger prevents spending an expanded budget on weak candidates. A candidate that is narrow and has a strong generalized latent-demand chain, but lacks only Gate 6, 8, or 9 evidence, is **authorization-proximate**. It may enter this module once.

## 2. Gate 6 — buyer/payer standard and method

### Minimum grounded hypothesis

Gate 6 passes only when the record identifies the evidenced user/beneficiary and one plausible economic actor, plus a concrete link between that actor and current spending, budget ownership, purchase authority, reimbursement, service purchase, or repeated payment for an adjacent substitute. A title, market size, or "someone must pay" is insufficient. A signed procurement record is not required.

| Evidence class | Treatment |
|---|---|
| Direct purchase, deposit, reimbursement, RFP, budget line, contract, or named service purchase | Strong direct evidence |
| Documented adjacent spend; named owner with responsibility plus demonstrated authority; repeated paid substitute | Acceptable grounded hypothesis support |
| Job description alone; category-spend statistic; generic role responsibility | Weak inference only |
| Founder claim, TAM, assumed CFO/consumer willingness, title without purchase context | Unusable |

### Bounded search sequence

1. Name user, beneficiary, selector, buyer, payer, gatekeeper, and intermediary; leave unknown roles explicit.
2. Find current economic behavior: substitute pricing, expert/service purchases, reimbursements, deposits, or recurring adjacent spend.
3. Find ownership: public role responsibilities, procurement/RFP language, benefit/program documentation, or practitioner approval discussions.
4. Test purchase authority: whether the identified actor can buy this class of outcome or already pays to obtain it indirectly.
5. Name access control: insurer, employer, platform, regulator, lender, marketplace, or professional intermediary.

Use public pricing, service marketplaces, RFPs/procurement records, reimbursement/benefit documents, job descriptions paired with budget evidence, public disclosures, marketplace transactions, practitioner budget discussions, and reviews naming payment. Stop `HOLD` when user demand is strong but no grounded economic link appears after two relevant source-family attempts. Reject if a gatekeeper/funder makes the target’s access structurally unavailable rather than merely hard to observe.

### Consumer and intermediary logic

For consumers, payer plausibility needs more than desire: attributable adjacent purchases, paid professional substitutes, deposits/financing, repeated paid attempts, price-visible waitlists, or costly DIY behavior. A consumer’s complaint alone is `WEAK`.

For two-sided, employer-sponsored, insurance, education, healthcare, financing, or marketplace cases, create separate rows for beneficiary, user, payer, selector, intermediary, and gatekeeper. Treat complexity as a sourcing task only while an economic path is plausible. Use `HOLD` when payer/intermediary evidence is incomplete but no fundamental constraint has won. Use substantive `REJECT` when regulation, risk underwriting, clinical/professional judgment, or platform economics is the actual binding constraint. Kiva-style regulated intermediation is therefore at least partly substantive, not a pure observability gap.

## 3. Gate 8 — enabler standard and method

Gate 8 needs one authoritative, contemporaneous source showing a specific change in availability, cost, capacity, infrastructure, regulation, distribution, or standards adoption, plus a written causal link to the named barrier. A product launch cannot be its own proof of an enabler.

| Strength | Evidence |
|---|---|
| Strong | measurable cost decline; formal regulatory change; documented API/platform availability; authoritative hardware/platform penetration; measurable distribution reach; standards adoption |
| Moderate | independent technical/trade reporting confirms availability and practical deployment, but magnitude or target access is incomplete |
| Weak / excluded | launch press, investor/founder narrative, generic trend article, "AI will transform," adjacent technology progress |

Apply the **barrier-link test**: (a) state the binding barrier; (b) identify the enabler’s changed variable; (c) show how that variable lowers cost, expertise, minimum scale, distribution, or implementation burden for the target; (d) state what remains unchanged. If this causal path cannot be written without a product claim, Gate 8 fails.

For timing, prefer dated regulatory notices, official pricing/API release notes, operator documentation, standards bodies, infrastructure penetration datasets, payment/broadband/logistics records, or independent contemporary trade reporting. Later success narratives are excluded.

## 4. Gate 9 — falsification standard and adequacy test

Gate 9 does not require proving no alternative exists. It requires a bounded, credible finding that relevant alternatives do **not adequately remove the named barrier for the target**, or that no adequate substitute was identified after a documented counter-search. Use the latter language only; never claim universal absence.

Select only relevant alternatives: free option, cheap self-service product, template/spreadsheet/DIY process, open source, professional/consultant, incumbent premium product, marketplace, organizational workaround, adjacent category, and doing without. For each relevant class, test:

1. Is the target able to access it?
2. What is the full cost, minimum, time, and expertise requirement?
3. Does it achieve the specified outcome, not merely an adjacent task?
4. Does the original barrier persist?
5. Is non-consumption rational despite its availability?

Classify each alternative `ADEQUATE`, `PARTIAL`, `INACCESSIBLE_TO_TARGET`, or `UNKNOWN`. A cheap/simple alternative defeats the hypothesis only when it is accessible to the target and adequately achieves the desired outcome. A crude workaround does not automatically defeat it. `UNKNOWN` never becomes evidence of inadequacy.

Professional services indicate an access barrier when price, capacity, wait time, geography, minimum engagement, expertise scarcity, or target-segment economics prevent adequate access despite demonstrated desire. They indicate an adequate solution when attributable evidence shows the target can obtain satisfactory outcome delivery at acceptable economics. Service use alone proves neither a software opportunity nor inadequacy.

## 5. Late-stage ladder and conditional budget

**Recommendation: small conditional extension.** Preserve the base budget for all candidates (four query rounds, twelve opened URLs, three family attempts). Authorization-proximate candidates receive one extra **three-role mini-pass**: at most **two query rounds**, **six opened URLs**, and **two additional source-family attempts total**, allocated across Gate 6/8/9. It cannot reopen Gates 1–5/7 or create an endless search.

| Pass | Focus | Stop rule |
|---|---|---|
| A. Buyer/payer | economic behavior → owner/authority → gatekeeper | stop after two relevant families without a grounded link |
| B. Enabler | primary/authoritative mechanism → barrier-link test | stop when causal link is absent or source is only product/hype |
| C. Falsification | relevant alternatives → adequacy matrix → fundamental constraint | reject immediately if adequate/simple/professional/fundamental explanation wins |

Run only sources needed for the unresolved role. A substantive failure terminates the module; a surviving but unproven role is `HOLD`, not more research.

## 6. Ledger metadata and confidence language

Add audit metadata only—no schema or new official state:

| Role | Labels |
|---|---|
| Buyer/payer | `DIRECT_PURCHASE`, `ADJACENT_PURCHASE`, `BUDGET_OWNERSHIP`, `GROUNDED_HYPOTHESIS`, `WEAK`, `UNKNOWN`, `INTERMEDIARY` |
| Enabler | `DIRECT_BARRIER_UNLOCK`, `AVAILABILITY`, `COST`, `ADOPTION`, `BARRIER_LINKED`, `PLAUSIBLE`, `ADJACENT_ONLY`, `NONE` |
| Falsification | `SUBSTITUTE`, `PRICE`, `ACCESSIBILITY`, `ADEQUACY`, `DISQUALIFYING`, `NON_DISQUALIFYING`, `UNKNOWN` |

At the card level, summarize buyer/payer as `DIRECT`, `GROUNDED_HYPOTHESIS`, `WEAK`, or `UNKNOWN`; enabler as `DIRECT_BARRIER_UNLOCK`, `PLAUSIBLE`, `ADJACENT_ONLY`, or `NONE`; and alternative adequacy as `ADEQUATE`, `PARTIAL`, `INACCESSIBLE_TO_TARGET`, or `UNKNOWN`. These terms improve auditability without numeric scoring.

When Gates 1–5/7 are strong, no substantive Gate 9 failure exists, and Gate 6/8/9 cannot be completed within the mini-pass, retain official `HOLD` and add `OBSERVABILITY_HOLD` metadata. It identifies a close, bounded public-evidence limitation without creating a fourth decision or implying promotion.

## 7. Historical diagnosis

| Case | Most useful refinement | Plausibly public at cutoff? |
|---|---|---|
| Warby Parker | alternative-adequacy matrix and buyer evidence; authoritative evidence for direct-distribution economics | buyer/alternative evidence partly yes; independent enabler evidence limited |
| Kiva | intermediary/gatekeeper map and regulatory/underwriting falsification | partly, but substantive risk/intermediation remains |
| Wix | small-business payer/agency pricing and DIY adequacy | partly; early archives likely sparse |
| Canva | non-designer budget/outsourcing evidence and browser/tool availability evidence | partly; direct buyer evidence likely limited |
| Dropbox | individual/team payer evidence, cloud/broadband availability, sync-alternative adequacy | partly; payer evidence likely weak publicly |

## 8. Public-web ceiling and future sources

| Role | Public-web ceiling | Reason |
|---|---|---|
| Buyer/payer | `PARTIALLY_SUFFICIENT` | public pricing/service purchases can support hypotheses, but private budgets/procurement often remain hidden |
| Enabler | `PUBLIC_WEB_USUALLY_SUFFICIENT` | authoritative documentation and public regulation/infrastructure sources are often available |
| Falsification | `PARTIALLY_SUFFICIENT` | alternatives/pricing are public, but target-segment adequacy often is not |

Future conceptual extensions—not approved for purchase or implementation—include interviews, expert networks, proprietary transaction/procurement datasets, paid market databases, search-query datasets, and survey panels. Use better public web sourcing now; record the structural limits rather than treating absence as proof.

## 9. Targeted validation and exit criteria

After review, validate this refinement only on **Warby Parker, Dropbox, Kiva, and one preserved control (Juicero)**. Warby and Dropbox are closest to authorization; Kiva tests substantive/intermediary handling; Juicero tests that stronger economic/alternative research does not create a false positive. Preserve prior outcomes and cutoffs.

Proceed to a separately reviewed bounded MUD implementation/live-pilot proposal only if the targeted validation recovers authorization-grade Gate 6/8/9 evidence for at least one close historical positive, preserves the control rejection, and requires no gate change. Stop source-strategy calibration and conclude public-web MUD is not currently economical if that targeted validation leaves all close positives blocked by documented unavailable public evidence or substantive alternative adequacy. No additional broad calibration is justified.

## 10. Future implementation requirements and next action

Later implementation only would require a reviewed candidate-card template addition, ledger validation rules, conditional-budget and authorization-proximity checks, audit reporting, focused tests, and human-review boundaries. No such change is authorized here.

**Next action:** Review this Gate 6/8/9 refinement design and explicitly authorize or decline the four-case targeted historical validation. Do not implement MUD or run live discovery during that validation.
