# Market Unlock Discovery (MUD) — Bounded Source Strategy

**Status:** design only; not implemented, piloted, or authorized for live discovery.  
**Purpose:** improve evidence acquisition without changing the approved nine-condition MUD gate, CFD, controller, or canonical data model.

## 1. Objective and operating principles

The expanded calibration indicates a source-observability bottleneck. This strategy improves what MUD can see, not what it must prove. Prefer observed behavior over stated preference; firsthand accounts over summaries; independent contexts over repeated claims; failed/blocked attempts over generic dissatisfaction; and explicit counterevidence over confirmation. Label actor role, date, directness, and independence. Exclude hindsight, startup-idea content, and technology-first claims as demand evidence.

## 2. Gate-to-source map

| Gate | Evidence needed | Strong source roles | Weak evidence / false positive |
|---|---|---|---|
| 1. Narrow unit | Named actor, outcome, one barrier | firsthand community/support accounts | broad complaint or feature request |
| 2. Breadth | 3 attributable URLs, 2 meaningful types | community + review/marketplace/pricing/process source | syndicated coverage, vendor copies |
| 3. Two chains | Two desire → attempt → barrier → consequence accounts | separate user/practitioner accounts, review narratives, service requests | two comments on one thread, complaint without consequence |
| 4. Consequence | Paid help, sustained labor, foregone value, abandonment | service listings, job posts, pricing, public process evidence | generic time-saving claim |
| 5. Barrier causality | Attempt despite desire; barrier caused opt-out | abandonment/help/access-limit discussions | low interest, bad onboarding, free-tier complaint |
| 6. Actor economics | Evidenced user/beneficiary and grounded payer hypothesis | procurement/pricing, job ownership, service purchase | title-based payer inference |
| 7. Generalization | Same barrier across independent contexts | separate communities/segments/geographies, practitioner evidence | one large thread, copied story, one vendor’s reviews |
| 8. Enabler | Specific mechanism weakens barrier | primary API/platform/regulatory/infrastructure documentation | hype or generic technology trend |
| 9. Falsification | Adequate-access/fundamental-constraint test | competitor docs/pricing, practitioner guidance, regulation | supportive sources only |

## 3. Bounded source taxonomy

| Family | Best use | Quality limit |
|---|---|---|
| Direct user/practitioner communities | desire, attempts, barriers, consequences | require author context and concrete behavior |
| Reviews | failed attempts, constrained access, workarounds | ratings or isolated product dissatisfaction are weak |
| Service marketplaces/directories | paid expertise and access cost | supply listing alone does not prove demand |
| Job postings | specialist labor and ownership | ordinary staffing does not prove an unlock |
| Public pricing/packaging | minimums, access tiers, implementation/service cost | price needs attributable avoidance evidence |
| Help/support/search discussions | setup, abandonment, missing expertise | routine support need is not an access barrier |
| DIY/maker/workaround communities | sustained substitutes and labor | down-weight hobby experimentation |
| Consultant/agency evidence | expertise gate and service cost | reject irreducibly judgment/safety/license-bound work |
| Public process documents | barrier mechanics and generalization | not demand proof by themselves |
| Category directories/marketplaces | capacity, distribution, availability | do not infer demand from listing count |
| Search behavior | discovery and intent corroboration | never satisfies a chain alone |
| Technology/infrastructure documentation | Gate 8 only | never demand evidence |

Initial live-pilot attempts should use direct communities, reviews, service/agency evidence, pricing, help/support, process documents, and infrastructure documentation. Directories and search behavior are discovery aids.

## 4. Evidence-chain and triangulation method

For a single narrow access hypothesis, search in order:

1. **Desire:** identify an actor explicitly seeking the outcome.
2. **Attempt/substitute:** establish what they bought, hired, built, delayed, or did instead.
3. **Barrier:** isolate one access constraint causing that substitute/non-consumption.
4. **Consequence:** establish cost, labor, abandonment, delay, reduced participation, or foregone output.
5. **Generalization:** obtain a second independent context with the same barrier.
6. **Actor economics and enabler:** ground buyer/payer and barrier-specific mechanism change.
7. **Counter-search:** test adequate alternatives, low desire, fundamental constraints, and unchanged economics.

The smallest robust role mix is two independent **direct behavior** sources, one **economic/access** source, one **buyer/payer** source, one **enabler** source, and one **falsification** source. A source may support more than one role, but it cannot inflate independent URL or source-type counts.

Useful diversity means distinct authorship, incentives, and actor contexts. Fake diversity includes syndicated reporting, vendor echo chambers, cloned directory pages, multiple comments attached to one story, or reviews copied across platforms. Record an `independence_group` before counting sources.

## 5. Actor-aware and non-consumption searching

Each card must name end user, beneficiary, selector, buyer, payer, gatekeeper, and professional intermediary. After a user signal, pivot to buyer budget/ownership, payer adjacent spend or service purchase, selector evaluation criteria, gatekeeper eligibility, and intermediary cost/limits. Do not infer a payer from job title alone.

Non-consumption is evidenced when desired-outcome attempts pair with an exclusion signal: delayed launch, stopped pursuit, paid indirect help, manual substitute, denial/minimum, waiting, reduced scope, or explicit decision to do without. Phrase searches only discover leads; source context must prove actor, action, barrier, and consequence.

## 6. Generalization, economics, enabler, and falsification

For Gate 7, seek the same named barrier in two independent communities, sizes, geographies, or existing approaches. One community remains weak even with many comments unless independent authors give distinct chains. One practitioner can support generalization only when they document differentiated clients; it remains corroboration, not a replacement for user evidence. Deduplicate repeated articles, screenshots, case studies, and vendor narratives.

Economic-consequence strength, in order: documented paid expert/service or foregone revenue; sustained headcount/manual labor or denied participation; repeated abandonment/delay with output loss; constrained capacity; credible price/minimum matched to attributable avoidance; generic time-saving claim. This is qualitative only.

Gate 8 needs a primary/authoritative source showing the exact mechanism change: API/platform availability, cost decline, infrastructure/distribution shift, regulation, or hardware penetration. It must connect to the named barrier. "AI is growing" and product announcements fail.

Every serious candidate runs counter-searches for cheap/simple alternatives, incumbent capability/pricing, low desire or premium segmentation, professional/safety/legal irreducibility, and whether the enabler changes unit economics. Use competitor documentation, independent guidance, public regulation, and disconfirming review narratives.

## 7. Search ladder, budget, and query families

| Level | Objective | Decision boundary |
|---|---|---|
| 1. Signal | narrow persona/outcome/barrier | reject if no attributable attempt after two query families |
| 2. Behavior | two causal-chain candidates | hold if one credible chain survives a source-family pivot |
| 3. Economics | meaningful consequence | reject when only convenience/hypothetical value exists |
| 4. Generalization | independent recurrence | hold when all evidence is one context |
| 5. Actor economics | grounded buyer/payer | hold when demand is real but payer is ungrounded |
| 6. Enabler | barrier-specific change | reject if it does not weaken the binding constraint |
| 7. Falsification | attempt to kill | reject if adequate/simple/fundamental explanation wins |

Per candidate: no more than **four query rounds**, **twelve opened URLs**, and **three source-family attempts**. Before a `HOLD` on gates 2, 3, or 7, perform one targeted second-source-family pivot. Do not extend the budget just to fill a checklist; immediate `REJECT` triggers stop early.

Query families derive from `persona + outcome + barrier`, never a product idea: desire; attempt/substitute; exclusion; consequence/abandonment; buyer/payer/adjacent spend; cross-context generalization; enabler mechanism; and counterevidence/cheap alternatives.

## 8. Ledger, gap handling, source quality, and blind spots

Use a Markdown source ledger **inside each future non-canonical MUD card**, with a companion Markdown appendix only when needed. Do not add JSONL or schemas yet. For each source record: URL, publication/access date, source type, actor, direct/indirect label, chain component, independence group, strength, candidate linkage, and short FACT/ESTIMATE/ASSUMPTION/HYPOTHESIS note.

Keep official outcomes `AUTHORIZE_SCOUT`, `HOLD`, and `REJECT`. For every unmet condition also label `SUBSTANTIVE_GAP`, `OBSERVABILITY_GAP`, or `MIXED_GAP`; name the missing source role, whether a bounded pivot occurred, and why further search is not warranted. This is learning metadata, not a fourth decision.

Exclude SEO/AI content farms, unverifiable screenshots, anonymous unsupported anecdotes, and retrospective founder mythology from chain proof. Treat vendor marketing, low-quality surveys, trend reporting, and a single product complaint as context only. Deduplicate syndication and cap one community thread as one context.

Public-web discovery is sufficient for a controlled pilot using communities, reviews, service/agency evidence, pricing, public process records, and infrastructure sources. It remains weak for private procurement, offline behavior, emerging markets, regulated/judgment-heavy work, ultra-high-net-worth niches, and low-discussion geographies. Source silence is not market absence. Future conceptual extensions—not authorized now—include licensed job/procurement/app-review datasets, search trends, marketplace transactions, interviews, and survey panels.

## 9. Calibration HOLD diagnosis

| Case | Observability-held gates | Plausible historical source family | Realistically public? |
|---|---|---|---|
| Warby Parker | 2, 3, 7; 9 mixed | optical-patient communities, insurer/retailer pricing, practitioner discussions | partly; attributable buyer chains likely sparse |
| Kiva | 2, 3, 7; 4/9 mixed | lender/borrower communities, partner-MFI records, policy/finance forums | limited; individual motives/consequences were often private |
| Wix | 2, 3, 7; 9 mixed | small-business communities, agency marketplaces, hosting/support forums | plausible, with uneven durable archives |
| Canva | 2, 3, 7; 9 mixed | marketer/design communities, agency pricing, tool support/reviews | plausible, but early evidence may be vendor-concentrated |
| Dropbox | 2, 3; 7/9 mixed | IT/admin communities, support forums, storage pricing, process documents | plausible, but individual consequences were often private |

This diagnosis does not rescore those cases.

## 10. Future live workflow, validation, and later implementation needs

A future live candidate follows: access signal → source plan by missing roles → desire → attempt/substitute → barrier → consequence → buyer/payer → generalization → enabler → falsification → gate decision/gap labels. `AUTHORIZE_SCOUT` still requires separate human approval.

Before implementation, replay this method on only the five expanded-calibration HOLD cases. Keep historical decisions locked; seek truly additional pre-cutoff evidence, measure recovery of missing chain components/source roles, and verify the three controls remain rejected. Review that replay before any MUD implementation, controller work, or live use.

Later implementation—not authorized by this document—would require a reviewed runner specification, Markdown template, source-role/independence checks, fixed-budget enforcement, audits, tests, controller integration review, a supervised-pilot protocol, and explicit human approval boundaries. No schema, JSONL, controller, batch, CFD, or live-workflow change occurs here.

## 11. Recommended next action

Review this bounded source-strategy design and explicitly authorize or decline the five-case historical source-method replay. Do not implement MUD or conduct live discovery during that replay.
