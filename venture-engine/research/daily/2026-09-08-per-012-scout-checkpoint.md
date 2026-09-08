# PER-012 Scout Checkpoint — Construction Change-Order Financial Continuity

**Stage:** Scout complete; no clustering performed.
**Scope:** FACT-based public-source review only. No Problem, competitor, Opportunity, score, experiment, offer, landing page, or automation record was created.

## Coverage and quality controls

| Measure | Result |
|---|---:|
| Observations added | 20 |
| Independent URLs | 12 |
| Source types | 3 |
| Largest single-URL contribution | 2 observations (10%) |

| Source type | Observations | Share |
|---|---:|---:|
| Reddit practitioner communities | 11 | 55% |
| Public product-review sites | 7 | 35% |
| Construction/ERP industry community | 2 | 10% |

The normal-batch source-diversity target is met and no URL exceeds the 25% concentration rule. Reddit remains the largest source type; discussions are self-selected and several threads include vendors or implementers. Review sites provide needed counterevidence but may be incentivized or role-ambiguous. The industry-community evidence is from an integration partner rather than a direct operator.

| Evidence tier | Count |
|---|---:|
| Tier 1 — behavioral/spend or paid use | 1 |
| Tier 2 — active intent | 0 |
| Tier 4 — problem or contradictory evidence | 19 |

| Source-role classification | Observations |
|---|---:|
| Internal operator / practitioner or identified internal role | 15 |
| Consultant / implementer | 3 |
| Role unclear | 2 |

## Observed themes (not formal Problem clusters)

- **Procore-to-accounting synchronization and correction (8 observations):** practitioners describe paid Procore/Sage use, repeated synchronization routines, correction work after a synchronized error, painful accounting-side sync, or change-order reconciliation against spreadsheets ([OBS-000200](../../data/observations.jsonl)–[OBS-000201](../../data/observations.jsonl), [OBS-000204](../../data/observations.jsonl), [OBS-000207](../../data/observations.jsonl)). The strongest reported consequence is two people spending most of two days resolving a synchronized mistake; it is one account, not a prevalence measure.
- **Implementation, connector, and migration boundaries (5 observations):** compatibility with QB Desktop, a missing Procore-to-Viewpoint connector, and financial-workflow adoption choices produced double entry, stopped integrations, or separate processes ([OBS-000202](../../data/observations.jsonl), [OBS-000205](../../data/observations.jsonl)–[OBS-000206](../../data/observations.jsonl), [OBS-000209](../../data/observations.jsonl)–[OBS-000210](../../data/observations.jsonl)). These are material disconfirmation of a product-independent residual workflow.
- **Limited non-Procore recurrence (3 observations):** an Autodesk integration partner described manual tax-code reapplication in a Build-to-Vista implementation, while an Autodesk reviewer described multi-step budget-code updates ([OBS-000211](../../data/observations.jsonl)–[OBS-000212](../../data/observations.jsonl), [OBS-000219](../../data/observations.jsonl)). These sources show that cross-system/state-maintenance work exists outside Procore, but they do not independently establish the same operator-level recurring change-order financial mechanism.
- **Incumbent/process absorption (7 observations):** counterpart accounts describe Procore financial workflows as accurate after configuration, existing Procore modules avoiding double entry, Procore-to-Sage transfer working, and standardized training/admin support as adequate ([OBS-000203](../../data/observations.jsonl), [OBS-000208](../../data/observations.jsonl), [OBS-000215](../../data/observations.jsonl), [OBS-000217](../../data/observations.jsonl)–[OBS-000218](../../data/observations.jsonl)).

## Recurring workflow, paid stack, and workaround evidence

**FACT:** Named stacks include Procore, Sage 300 CRE, Sage ERP, QuickBooks Desktop/Online, Viewpoint Spectrum, Autodesk Build/Construction Cloud, and Viewpoint Vista. One operator reports a Sage 300 integrator costing about US$8,000–$10,000 per year; that is paid-adoption evidence, not willingness to pay for an additional tool.

**FACT:** Recorded workarounds include a CFO-triggered synchronization routine, two-person correction work after a synchronized error, spreadsheet reconciliation, double entry during a migration or missing-connector state, manual tax-code reapplication, and multi-place budget-code updates. These vary materially in whether they appear residual, implementation-specific, or normal financial control.

**FACT:** The clearest reported labor/consequence is one practitioner’s account of two people spending most of two days on a synchronized mistake and another practitioner’s report of hours reconciling a Procore change order to a spreadsheet. No source supplies comparable recurring labor, billing-delay, WIP-error, margin, or revenue-leakage measurements for the narrow persona.

## Cross-platform recurrence and structural assessment

**FACT:** Paid Procore/Sage accounts independently report synchronization and reconciliation friction. A Procore/Viewpoint Spectrum account reports double entry but lacks the connector, making it an incomplete-adoption case. Autodesk Build/Viewpoint Vista evidence describes a manual tax-code correction but comes from an integration partner; an Autodesk reviewer reports multi-step updates without an accounting-system detail.

**INFERENCE:** The Scout did not establish the same recurring, post-competent-adoption change-order financial-continuity mechanism across multiple project-management/ERP platforms. It found a plausible cross-platform *category* of state-maintenance work, but the strongest detailed cases remain Procore-specific or connector/configuration-specific. This is a Scout-stage assessment, not a formal Problem conclusion.

## Buyer and payer evidence

**FACT:** A CFO controls synchronization in one operator account; accounting teams, finance/accounting employees, project managers, and project coordinators appear in the corpus. Contractors demonstrably fund project-management, accounting/ERP, and integration software.

**UNKNOWN:** No source establishes who selects, pays for, or would separately buy a solution for this narrow workflow. Existing paid-stack spend and requested ERP synchronization are not separate willingness-to-pay evidence.

## Incumbent adequacy and negative evidence

- **FACT:** One firm moved from QBO/Procore to Premier and described the replacement as smoother ([OBS-000203](../../data/observations.jsonl)).
- **FACT:** A Procore user reported financial workflows more accurate than Excel after configuration ([OBS-000208](../../data/observations.jsonl)); another described linked modules preventing double entry ([OBS-000217](../../data/observations.jsonl)).
- **FACT:** A Sage reviewer described information successfully transferring from Procore to accounting ([OBS-000218](../../data/observations.jsonl)), and a Procore manager described standardized daily adoption, training, and an admin resource as material to value realization ([OBS-000215](../../data/observations.jsonl)).
- **FACT:** Multiple adverse accounts plainly involve an absent connector, migration, product compatibility, contract-specific markups, or a process choice ([OBS-000202](../../data/observations.jsonl), [OBS-000205](../../data/observations.jsonl)–[OBS-000206](../../data/observations.jsonl), [OBS-000209](../../data/observations.jsonl)).

## CFD hypothesis check (non-canonical traceability)

**Independently reproduced:** paid multi-system adoption; manual synchronization, correction, re-entry, and spreadsheet reconciliation; a concrete paid-integrator figure; and several operator-adjacent accounts of finance/project handoff friction.

**Weakened:** detailed recurring post-adoption cases are concentrated in Procore/Sage. The non-Procore evidence is thin and largely consultant/implementation-specific. Several accounts show that configuration, a supported integration, standardized workflow, or a consolidated product can absorb the apparent work.

**Misleading or unresolved CFD signals:** paid integration and a spreadsheet do not identify a residual buyer. A manual tie-out may be an intentional control, a contract-specific calculation, or migration/configuration debt rather than an unserved product job.

## Evidence-quality constraints and gaps

- The source set contains no direct, independently attributable account of the same recurring mechanism across two non-identical mature stacks.
- Direct operator accounts do not consistently state company size, GC versus subcontractor role, connector maturity, correction cadence, or economic impact.
- Review-site evidence is self-selected and can be incentivized; Reddit evidence is self-selected and may include supplier participation.
- No observation establishes a formal Problem, opportunity, structural market gap, residual willingness to pay, or a separate buyer/payer.

## Next permitted action

Review this PER-012 Scout checkpoint with the user. Do not start Problem Clustering without separate authorization.
