# Commercial Friction Discovery Candidate Card

**Date:** `2026-09-08`

**CFD version:** `manual-pilot-v1`

**Decision:** `AUTHORIZE_SCOUT`

## Candidate

- **Candidate persona:** Finance / revenue-operations owner at a B2B SaaS company with non-standard contracts.
- **Existing persona ID, if any:** None. This is not a request to create a persona.
- **Narrow workflow:** Recurring close-period reconciliation of bookings, billing, revenue, and ARR changes across Salesforce, a billing/CPQ system, NetSuite, and reporting tools.
- **Trigger/context:** Contract amendments, non-standard terms, usage or volume pricing, new mappings, and month-end close.
- **Operational mechanism:** A paid commercial stack records related lifecycle events in separate systems; finance personnel export, compare, correct mappings, investigate exceptions, and reconcile the resulting revenue/ARR state.

## Commercial-friction evidence

- **Paid incumbent or paid labor already present:** **FACT:** accounts describe Salesforce, NetSuite, Younium, Alteryx, Tableau, Google Sheets, and Abacum. One account reports an offshore team reviewing material monthly changes. These are current-system or labor signals, not evidence that a new purchase would occur.
- **Existing workaround:** **FACT:** reported workarounds include spreadsheets/Google Sheets, monthly data checks, manual overrides, and ongoing mapping maintenance.
- **Economic consequence or labor burden:** **FACT:** one practitioner reports offshore review of monthly account-level changes above a stated threshold; another reports a US$30,000 accumulated reconciliation issue. **UNKNOWN:** frequency, comparability, and total cost across the proposed persona.
- **Post-adoption friction summary:** **FACT:** multiple accounts report reconciliation or mapping work after adoption of named paid systems. **HYPOTHESIS:** the recurring mechanism may be a sufficiently narrow pre-Scout target: preserving financial meaning through contract changes across a complex quote-to-cash stack.

| Source type | Direct source link | Attributable evidence | Post-adoption mechanism | Paid/labor or economic link | Notes / limitations |
|---|---|---|---|---|---|
| Practitioner community | [r/FPandA — ARR reporting discussion](https://www.reddit.com/r/FPandA/comments/1ll21c1/anyone_in_saas_want_to_brag_about_their_arr/) | Participants at firms ranging from roughly US$25M to US$550M ARR describe Salesforce/NetSuite/Excel or Sheets workflows, monthly reconciliation, manual overrides, and an offshore review team for material changes. | Contract, churn, and mapping changes are reconciled between commercial and financial reporting systems. | Named paid stack; reported offshore review labor. | Several accounts occur in one thread; they are not independent URLs. Some participants also report that data hygiene, Excel, or Abacum adequately handles their case. |
| Practitioner community | [r/NetSuite — B2B SaaS billing-engine discussion](https://www.reddit.com/r/Netsuite/comments/1skc64g/suitable_billing_engine_for_b2b_saas_suitebilling/) | A practitioner describes a post-acquisition stack of Salesforce, Younium, and NetSuite with source-of-truth conflict and slow integrations at transaction volume. | Lifecycle data must cross three paid systems; current integration behavior remains operationally limiting. | Named paid systems; no separate residual-work spend is reported. | One account; may be an implementation, scale, or vendor-fit issue rather than a general residual job. |
| Practitioner community | [r/NetSuite — Salesforce/NetSuite integration discussion](https://www.reddit.com/r/Netsuite/comments/1n0x2y0/has_anyone_successfully_integrated_salesforce_and/) | Participants describe custom-field mapping upkeep, failed transactions, API limits, duplicate handling, and split system ownership after integration adoption. | Commercial data integration requires continuing exception and mapping work as systems evolve. | Named paid CRM/ERP and third-party integration layers. | Discussion includes implementers and providers; it does not establish prevalence or a buyer for an additional layer. |
| Public product review | [G2 — NetSuite review context](https://www.g2.com/software/salesforce) | A named NetSuite reviewer reports integration delays and manual intervention, while also reporting that NetSuite plus BlackLine reduces reconciliation work. | Integration failure can require manual intervention; reconciliation tools may absorb it. | Existing NetSuite and BlackLine use. | The page is an aggregated review context, not a SaaS quote-to-cash case. It is primarily contradictory/absorption evidence. |

## Actor map

| Role | Evidence-backed assessment | Unknowns |
|---|---|---|
| User | **FACT:** finance managers, finance teams, and operational reviewers perform or consume the reconciled reporting described in the sources. | Exact owner by company size and stack maturity. |
| Selector | **HYPOTHESIS:** the controller, VP Finance, or RevOps leader is likely to evaluate a workflow change because the evidence places the work across those functions. | Whether selection is finance-led, RevOps-led, IT-led, or shared. |
| Buyer | **HYPOTHESIS:** a finance executive accountable for close accuracy and revenue reporting is a plausible economic buyer. | No source records a purchase decision for an additional residual-work solution. |
| Payer | **HYPOTHESIS:** the operating B2B SaaS company already funds the named software and review labor. | Budget owner, budget category, and separate willingness to pay are unknown. |

## Quick absorption check

- **Relevant incumbent, service, free-tool, or normal-process coverage:** **FACT:** Oracle documents Salesforce/NetSuite synchronization; practitioners name iPaaS and revenue/reporting tools; the G2 reviewer reports that BlackLine reduces reconciliation work. **FACT:** some r/FPandA participants describe clean data hygiene, Excel, or Abacum as adequate.
- **Could this be an isolated defect, poor implementation, clinical/professional judgment, or ordinary process issue?** **POSSIBLE, but not plainly established.** Single incidents may be setup or mapping defects. The repeated theme across separate accounts is change-sensitive commercial-to-financial reconciliation after paid-stack adoption, so the proposed Scout should test whether that recurrence survives competent configuration rather than presuming it does.
- **Contradictory evidence:** **FACT:** incumbent tools and a disciplined reporting process can materially absorb the work; one product-review account explicitly reports reduced reconciliation burden with NetSuite plus BlackLine. No source demonstrates a separate purchase for the proposed residual workflow.

## Source limitations

- **Independent URL count:** 4.
- **Source-type count:** 2 (practitioner community; public product review).
- **Concentration or access constraints:** Three URLs are Reddit discussions and are partly populated by implementers or vendors. The product-review source is useful chiefly as disconfirmation and is not a direct quote-to-cash workflow account.
- **Persona-fit / prevalence limits:** Company revenue, stack complexity, contract complexity, transaction volume, and implementation maturity vary. Evidence is preliminary; it cannot establish frequency, market size, or opportunity-specific willingness to pay.

## Promotion gate

- [x] Narrow persona plus concrete recurring workflow.
- [x] At least three independent URLs across at least two source types, where available.
- [x] At least two attributable post-adoption signals with the same operational mechanism.
- [x] Direct link to paid software, paid labor, contractor/consultant work, or measurable economic cost.
- [x] Plausible user, selector, buyer, and payer hypothesis grounded in evidence.
- [x] Quick absorption check does not plainly explain the issue as an excluded or already-solved case.

## Rationale

**FACT:** The public accounts show paid CRM, billing, ERP, integration, and reporting stacks coexisting with recurring reconciliation, manual review, and mapping work. They also show credible absorption: modern reconciliation and integration tools, data hygiene, and routine process can solve some cases.

**ESTIMATE:** None. This CFD pass does not estimate prevalence, cost, or market size.

**ASSUMPTION:** A future Scout could access independent accounts in B2B SaaS finance, RevOps, accounting, and product-review/public implementation sources without relying on this card.

**HYPOTHESIS:** Complex contract-change reconciliation may remain a recurring operational job after competent adoption of the current stack for a narrow subset of B2B SaaS firms.

**Decision rationale:** `AUTHORIZE_SCOUT` is warranted only as a recommendation for human review because all preliminary gate conditions are met. It does not establish a canonical persona, Problem, Opportunity, residual willingness to pay, or a solution. Any authorized Scout must independently verify post-adoption recurrence, distinguish it from configuration failures, and seek direct buyer/payer and separate-payment evidence.

## Rejected signals encountered during the broad pass

- **FACT:** Multichannel-commerce inventory reconciliation showed named tools that synchronize inventory; remaining spreadsheet work often reflected master-data needs or a defined source-of-truth process rather than a proven residual paid job. See [r/shopify](https://www.reddit.com/r/shopify/comments/1veu85a/how_to_consolidate_inventory_across_multiple/) and [r/ecommerce](https://www.reddit.com/r/ecommerce/comments/1qz7idf/how_do_you_handle_mismatched_data_across_multiple/).
- **FACT:** Generic accounting and small-business invoice reconciliation produced real manual work, but sources commonly pointed to established accounting, payment, or reconciliation products and ordinary process as adequate coverage. See [r/smallbusiness — invoice matching](https://www.reddit.com/r/smallbusiness/comments/1qat837/spent_my_saturday_manually_matching_47_invoices/) and [r/Netsuite — account reconciliations](https://www.reddit.com/r/Netsuite/comments/1cj9yyh/account_reconciliations/).
- **OPINION:** These were not retained as CFD candidates because the first-pass evidence did not isolate a post-adoption, tool-independent mechanism with a clear buyer that survived the absorption check.

## CFD learning note

**FACT:** The authorized Scout independently reproduced paid multi-system stacks, spreadsheet/export and manual-override behavior, mapping/exception work, and finance/reporting reconciliation. It also independently found that current billing, reconciliation, and configured ERP/process options can materially absorb much of the work.

**FACT:** No formal Problem survived clustering. The canonical evidence did not establish one repeatable structural workflow after competent adoption; the candidate mechanisms were bounded by implementation/configuration debt, bespoke architecture, ordinary financial control, professional judgment, product-specific friction, and source-quality limits.

**OPINION:** This single pilot result is insufficient to revise the CFD promotion gate, taxonomy, or thresholds. It is a recorded downstream outcome, not evidence that CFD is ineffective or that its authorization bar should change.

## Later outcome (complete after authorized downstream work)

- **Later outcome tag:** `SCOUT_NO_PROBLEM`
- **Later rejection pattern:** `implementation/configuration-specific; incumbent/process adequacy; bespoke architecture/complexity; ordinary control/professional judgment; source-quality limitation`
- **Linked canonical records, if independently created later:** `PER-011; OBS-000180–OBS-000199; no Problem promoted`
