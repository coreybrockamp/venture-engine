# Commercial Friction Discovery Candidate Card

**Date:** `2026-09-09`

**CFD version:** `manual-pilot-v2`

**Decision:** `HOLD`

## Candidate

- **Candidate persona:** Independent auto-repair shop service advisor or back-office owner.
- **Existing persona ID, if any:** None; no persona is created by this card.
- **Narrow workflow:** Moving supplier parts, labor, and invoice detail into repair orders and reconciling supplier statements after shop-management-software adoption.
- **Trigger/context:** Public practitioners described paid shop-management systems paired with separate parts/labor or supplier systems.
- **Operational mechanism:** Re-entry or reconciliation when source-system document granularity differs from the repair-order/accounting record.

## Commercial-friction evidence

- **Paid incumbent or paid labor already present:** FACT — both direct accounts describe using commercial shop-management software (Mitchell Shop Manager or Tekmetric) with external parts/labor suppliers or systems.
- **Existing workaround:** FACT — one account manually enters parts and labor from three programs; another reports product-team workarounds that do not work for its split-invoice reconciliation case.
- **Economic consequence or labor burden:** FACT — the direct accounts describe substantial typing and reconciling a supplier statement; no independently verified time, dollar loss, or separate willingness-to-pay evidence was found.
- **Post-adoption friction summary:** FACT — the accounts report workflow friction after adoption, but the first is catalog/estimate entry and the second is invoice-versus-order reconciliation.

| Source type | Direct source link | Attributable evidence | Post-adoption mechanism | Paid/labor or economic link | Notes / limitations |
|---|---|---|---|---|---|
| Public practitioner discussion | [r/mechanics: Automotive Shop Management Software](https://www.reddit.com/r/mechanics/comments/1eyyhye/) | A Mitchell Shop Manager user describes manually moving parts from RepairLink and labor from AllData/ProDemand into estimates. | Catalog/labor data re-entry. | Paid shop-management and repair-information tools; manual office work. | One operator account; no cost quantified. |
| Public practitioner discussion | [r/mechanics: shop software with QuickBooks integration](https://www.reddit.com/r/mechanics/comments/1miqxp6/shop_management_software_w_quickbooks_integration/) | A Tekmetric user says one Worldpac order can produce several invoices while Tekmetric imports order totals, making statement reconciliation difficult; stated workarounds fail. | Supplier-invoice versus repair-order reconciliation. | Paid Tekmetric and supplier purchasing; recurring statement reconciliation. | One operator account; product-specific and source type is the same as the first account. |
| Incumbent documentation | [PartsTech + Tekmetric integration](https://partstech.com/software/management-system-integrations/connect-with-tekmetric/) | PartsTech documents one-screen supplier search/order integration with Tekmetric. | Covers substantial parts-ordering handoff. | Existing integrated tooling. | Vendor claim, retained as counterevidence. |
| Incumbent documentation | [PartsTech multi-system integration](https://get.partstech.com/endeavor) | PartsTech says it integrates with 35+ shop-management systems and can transfer parts into repair orders. | Covers broad parts-entry workflow. | Free/paid product options; existing alternative. | Vendor claim; does not establish invoice-statement adequacy. |

## Actor map

| Role | Evidence-backed assessment | Unknowns |
|---|---|---|
| User | Service advisor or office staff performs estimate entry and supplier-statement reconciliation. | Whether the same person owns both tasks across shops. |
| Selector | HYPOTHESIS — shop owner or manager selects software/integrations. | Selection process and integration authority. |
| Buyer | HYPOTHESIS — independent repair-shop owner. | Separate budget from the incumbent stack. |
| Payer | HYPOTHESIS — repair business. | Separate willingness to pay for a residual bridge. |

## Quick absorption check

- **Relevant incumbent, service, free-tool, or normal-process coverage:** FACT — PartsTech documents integrated parts ordering and repair-order transfer across many shop systems; the public discussions name multiple specialist systems and integration choices.
- **Could this be an isolated defect, poor implementation, clinical/professional judgment, or ordinary process issue?** POSSIBLY — the accounts concern different incumbent combinations and may be product integration, setup, supplier-document, or ordinary accounting-control issues.
- **Contradictory evidence:** FACT — PartsTech advertises direct supplier-to-repair-order integration for Tekmetric and 35+ management systems. This is vendor documentation, not independent proof of universal adequacy.

## Source limitations

- **Independent URL count:** 4 (two practitioner URLs; two incumbent URLs).
- **Source-type count:** 2 (public practitioner discussions; incumbent documentation).
- **Concentration or access constraints:** All direct customer evidence is Reddit-based; each mechanism has one attributable account.
- **Persona-fit / prevalence limits:** Shop size, stack configuration, accounting process, supplier mix, and recurrence are not consistently known.

## Structural-generalization check

- **Independent organizations represented:** Two attributable operator accounts.
- **Distinct incumbent stacks / implementations represented:** Mitchell Shop Manager + RepairLink/AllData/ProDemand; Tekmetric + Worldpac.
- **Same operational mechanism across those contexts?:** UNKNOWN — both concern cross-system parts information, but one is catalog/labor entry and the other invoice-statement reconciliation.
- **Path A — cross-implementation recurrence evidence:** FAIL — there is not yet attributable recurrence of one sufficiently specific residual mechanism across the two stacks.
- **Path B — vendor-independent evidence, if cross-stack evidence is unavailable:** FAIL — no vendor-independent source establishes a durable residual workflow after competent adoption.
- **Evidence against generalization:** Existing integration products explicitly target supplier-to-repair-order transfer; no source establishes whether remaining invoice reconciliation is widespread and tool-independent.
- **Structural-generalization gate result:** `FAIL`

## Promotion gate

- [x] Narrow persona plus concrete recurring workflow.
- [x] At least three independent URLs across at least two source types, where available.
- [ ] At least two attributable post-adoption signals with the same operational mechanism.
- [x] Direct link to paid software, paid labor, contractor/consultant work, or measurable economic cost.
- [ ] Plausible user, selector, buyer, and payer hypothesis grounded in evidence.
- [ ] Quick absorption check does not plainly explain the issue as an excluded or already-solved case.
- [ ] Structural-generalization check passes through Path A or Path B.

**Product-specific handling:** The first six conditions are not strong enough and structural generalization fails; `AUTHORIZE_SCOUT` is unavailable.

## Rationale

**FACT:** Two paid-shop-system users describe real post-adoption data-entry or reconciliation work.

**ESTIMATE:** None.

**ASSUMPTION:** None.

**HYPOTHESIS:** A residual parts-document handoff job may exist only if later independent sources show the same specific mechanism persists after competent integration/process use.

**Decision rationale:** `HOLD`. This is stronger than a generic complaint because it includes paid systems and two operational accounts, but it does not establish a single structural residual paid job. It needs independent same-mechanism recurrence, evidence beyond one source type, clearer absorption results, and buyer/payment support. No canonical Scout resources are authorized.

## Later outcome (complete only after authorized downstream work)

- **Later outcome tag:** `NOT_YET_RUN`
- **Later rejection pattern:** `NOT_YET_RUN`
- **Linked canonical records, if independently created later:** None; this card has not received downstream authorization.
