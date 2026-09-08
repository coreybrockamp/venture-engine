# PER-011 Scout Checkpoint — B2B SaaS Finance / Revenue Operations

**Stage:** Scout complete; no clustering performed.
**Scope:** FACT-based source review only. No Problem, competitor, Opportunity, score, experiment, offer, or automation record was created.

## Coverage and quality controls

| Measure | Result |
|---|---:|
| Observations added | 20 |
| Independent URLs | 11 |
| Source types | 3 |
| Largest single-URL contribution | 3 observations (15%) |

| Source type | Observations | Share |
|---|---:|---:|
| Reddit practitioner communities | 12 | 60% |
| Public software-review sites | 6 | 30% |
| Hacker News technical community | 2 | 10% |

The normal-batch source-diversity target is met. No individual URL exceeds the 25% concentration rule. Reddit remains a material source-type concentration and includes implementer/provider participation in several threads; product-review and technical-community evidence counterbalance it but are self-selected and role-specific.

| Evidence tier | Count |
|---|---:|
| Tier 1 — behavioral/spend or paid use | 5 |
| Tier 2 — active intent | 1 |
| Tier 4 — problem or contradictory evidence | 14 |

## Observed themes (not formal Problem clusters)

- **Contract-change and revenue/ARR reconciliation (9 observations):** internal finance and implementation accounts describe Salesforce, CPQ, NetSuite, Sheets, and revenue arrangements being reconciled or updated around reporting, amendments, and custom mappings ([OBS-000180](../../data/observations.jsonl)–[OBS-000184](../../data/observations.jsonl), [OBS-000188](../../data/observations.jsonl)–[OBS-000191](../../data/observations.jsonl)). The corpus includes both recurring manual override/mapping signals and evidence that correct data modeling, product types, and a properly configured ERP handle some of the apparent mismatch.
- **ERP-to-warehouse/BI discrepancy handling (4 observations):** practitioners describe finance checks outside NetSuite and case-by-case discrepancy investigation when warehouse transformation logic differs from ERP reporting ([OBS-000185](../../data/observations.jsonl)–[OBS-000187](../../data/observations.jsonl), [OBS-000198](../../data/observations.jsonl)). The evidence does not show that this is a product-independent job rather than reporting architecture, business-logic judgment, or a necessary control.
- **Incumbent absorption is substantial (7 observations):** Chargebee, ZoneReconcile, and Zuora review accounts report paid systems replacing spreadsheet schedules, manual matching, billing errors, or close work ([OBS-000193](../../data/observations.jsonl)–[OBS-000197](../../data/observations.jsonl)). These are direct counterweights to the CFD premise.
- **Boundary between residual work and accounting control (3 observations):** a technical-community account and finance-practitioner comments caution that manual adjustments, reconciliation back to an ERP, and unusual transactions can be appropriate control or judgment work ([OBS-000187](../../data/observations.jsonl), [OBS-000191](../../data/observations.jsonl), [OBS-000199](../../data/observations.jsonl)).

## Paid stack and workaround evidence

**FACT:** Named systems include Salesforce, Salesforce CPQ, NetSuite, Chargebee, Zuora, ZoneReconcile, Abacum, Databricks, Power BI, Excel, Google Sheets, and third-party integration platforms. Observed workarounds include Sheets/Excel exports, manual overrides, return authorizations for amendments, mapping maintenance, warehouse/BI investigations, and evaluation of middleware.

**FACT:** Two paid-labor signals are present but limited: the source corpus includes an internal implementation lead and a revenue-automation consultant. No attributable source establishes recurring headcount, contractor cost, outsourcing spend, or a separately purchased residual-work service for this exact persona.

**UNKNOWN:** Whether spreadsheet use is a durable bridge after competent adoption, a suitable reporting/control layer, or a temporary implementation artifact in any representative share of this persona.

## Post-adoption and consequence evidence

**FACT:** The strongest post-adoption signals are manual ARR overrides after a Salesforce/Abacum reporting transition ([OBS-000182](../../data/observations.jsonl)); finance checks and case-by-case discrepancy investigation outside a NetSuite/warehouse/BI stack ([OBS-000185](../../data/observations.jsonl)–[OBS-000186](../../data/observations.jsonl)); and ongoing mapping/exception maintenance in Salesforce/NetSuite integration discussions ([OBS-000188](../../data/observations.jsonl)).

**FACT:** The corpus reports manual and error-prone reporting, slow/inaccurate data views, manual matching, invoicing errors, and delayed revenue reconciliation as consequences. It does not provide independently comparable close-delay, leakage, headcount, contract value, or recurring-cost measures for the narrow target workflow.

## Buyer and payer evidence

**FACT:** Finance directors, accounting managers, a CEO, implementation leads, and revenue-automation consultants appear in the source corpus. The reviewed companies already use paid CRM, billing, ERP, reconciliation, and reporting systems.

**UNKNOWN:** The evidence does not identify a selector, economic buyer, payer, procurement path, or willingness to pay for any additional workflow layer. Existing category spend must not be interpreted as separate willingness to pay.

## Incumbent adequacy and negative evidence

- **FACT:** A finance director using Salesforce, NetSuite, Excel, and Google Sheets described a clean, painless roll-forward after data cleanup ([OBS-000181](../../data/observations.jsonl)).
- **FACT:** A SaaS respondent said correct product types and ERP revenue-recognition rules should handle billing-versus-revenue differences ([OBS-000191](../../data/observations.jsonl)).
- **FACT:** Chargebee, ZoneReconcile, and Zuora review accounts describe automated billing, revenue schedules, reconciliation rules, and matching as replacing or reducing spreadsheet/manual processes ([OBS-000193](../../data/observations.jsonl)–[OBS-000197](../../data/observations.jsonl)).
- **FACT:** Several alleged friction accounts were implementation/configuration, reporting-architecture, or bespoke-mapping cases—not evidence that a broad residual job exists ([OBS-000183](../../data/observations.jsonl)–[OBS-000184](../../data/observations.jsonl), [OBS-000187](../../data/observations.jsonl), [OBS-000199](../../data/observations.jsonl)).

## CFD hypothesis check (non-canonical traceability)

**Independently reproduced:** paid multi-system stacks; spreadsheet/export and manual-override behavior; ongoing mapping/exception work; and finance/reporting reconciliation after adoption.

**Weakened or failed:** the Scout did not independently establish paid bridge labor at a meaningful recurring scale, a repeatable post-competent-adoption mechanism distinct from implementation or normal controls, an identifiable separate buyer/payer, or separate willingness to pay. Source diversification strengthened confidence that incumbent absorption is material: review sources directly describe existing products eliminating manual work.

## Evidence-quality constraints and gaps

- Reddit is concentrated at 60% of observations and several threads include implementers, vendors, or prompts seeking market input. Treat these as bounded public accounts, not prevalence evidence.
- Product reviews are self-selected and sometimes incentivized; they are valuable for named-stack and adequacy evidence but do not establish a representative workflow.
- Hacker News accounts have unclear job roles and company context.
- Public evidence did not establish company size, contract complexity, cadence, labor cost, or procurement ownership consistently.
- No observation establishes an Opportunity, residual paid job, or willingness to pay.

## Next permitted action

Review this Scout evidence with the user. Do not start Problem Clustering without separate authorization.
