# Commercial Friction Discovery Candidate Card

**Date:** `2026-09-08`

**CFD version:** `manual-pilot-v1`

**Decision:** `AUTHORIZE_SCOUT`

## Candidate

- **Candidate persona:** Project-financials or accounting manager at a commercial contractor using Procore and an accounting/ERP system for complex change orders.
- **Existing persona ID, if any:** None. This is not a request to create a persona.
- **Narrow workflow:** Correcting, reconciling, and re-entering approved change-order data after it moves from Procore into the accounting/ERP system, so contract value, job cost, and billing remain aligned.
- **Trigger/context:** A change order has missing or mismatched detail, cannot be corrected in the originating system after synchronization, or must be reconciled against a contract/reporting record.
- **Operational mechanism:** A paid project-management and accounting stack leaves staff to investigate export errors, restore or unlink records, map line items, re-enter data, and reconcile the financial result across systems.

## Commercial-friction evidence

- **Paid incumbent or paid labor already present:** **FACT:** the sources name Procore with Sage 300, QuickBooks Online, and Smoothlink. One practitioner describes a Sage 300 integration costing US$8,000–$10,000 per year. These are paid-stack signals; they do not establish demand for another purchase.
- **Existing workaround:** **FACT:** reported workarounds include staff support requests, manual change-order reports and contract records to tie out values, and a repeated CFO-controlled synchronization routine.
- **Economic consequence or labor burden:** **FACT:** a finance-community participant describes a roughly US$31 million, three-year project for which the current cost-plus workflow does not scale; a separate practitioner describes recurring manual synchronization at least at the start and end of each day and every two hours. **UNKNOWN:** total labor cost, frequency, and prevalence.
- **Post-adoption friction summary:** **FACT:** three attributable accounts describe recurring correction, reconciliation, or synchronization work after adopting Procore plus an accounting stack. **HYPOTHESIS:** a narrow, cross-system change-order-control workflow may remain after competent adoption for a subset of contractors.

| Source type | Direct source link | Attributable evidence | Post-adoption mechanism | Paid/labor or economic link | Notes / limitations |
|---|---|---|---|---|---|
| Construction-software user community | [Sage Community — Owner Change Orders and Procore](https://communityhub.sage.com/us/sage_construction_and_real_estate/f/sage-300-construction-and-real-estate/170313/owner-change-orders-and-procore) | A user with about 1.5 years of Procore and Sage 300 use reports that needed change-order detail does not transfer, and that an error cannot simply be deleted or unlinked without support. | Staff must correct or reverse synchronized change-order records after export. | Named paid Procore and Sage 300 stack. | One organization; product/integration-specific detail is material disconfirmation. |
| Construction-finance professional community | [CFMA Café — Procore/Smoothlink/QBO](https://cafe.cfma.org/discussion/procoresmoothlinkqbo-1) | A participant on a roughly US$31 million, three-year job reports that its cost-plus workflow does not work with Procore, Smoothlink, and QBO and uses change-order reports/contract records to tie out amounts. | Contract/change-order values require manual reconciliation outside the integrated stack. | Named paid stack and reported non-scalability on a large project. | One organization; contract type and configuration may be unusual. |
| Practitioner community | [r/ConstructionManagers — Procore/Sage 300 integration](https://www.reddit.com/r/ConstructionManagers/comments/1f0ew4i/) | A practitioner reports paying US$8,000–$10,000 annually for a Sage 300 integrator and says the CFO schedules repeated synchronization to keep numbers current. | A routine human process bridges synchronization timing between the project and accounting systems. | Paid integration plus recurring finance-leader labor. | One organization; could be a deliberate control choice rather than a residual commercial gap. |
| Incumbent documentation (contradictory) | [Procore — unlink synchronized prime contract change orders](https://support.procore.com/products/online/user-guide/company-level/erp-integrations/tutorials/unlink-pccos-synced-with-erp) | Procore documents reset/unlink workflows and ERP-specific prerequisites for correcting synchronized records. | The incumbent provides a correction path, though some cases require permissions or actions in the ERP first. | Existing incumbent coverage. | This is documentation, not a customer account; it limits but does not erase the reported recurring work. |

## Cross-company recurrence check

- **Independent organizations/users:** **FACT:** three separate public accounts describe the mechanism after adoption: Procore/Sage 300 correction limits, Procore/Smoothlink/QBO tie-outs, and Procore/Sage 300 synchronization routines.
- **Stack variability:** **FACT:** the accounting-side stacks vary between Sage 300 and QuickBooks Online/Smoothlink; all supporting accounts share Procore.
- **What appears structural:** **HYPOTHESIS:** approved change orders must retain aligned financial meaning across project-management, contract, job-cost, billing, and accounting records; exceptions can require human correction when the systems' state or data model diverges.
- **What appears implementation-specific:** **FACT:** every supporting account uses Procore, and each names an integration, contract, or correction-path constraint. **HYPOTHESIS:** the mechanism may be a Procore-to-ERP integration pattern rather than a broader construction workflow.
- **Evidence against generalization:** **FACT:** Procore offers documented reset/unlink controls. **FACT:** a construction-community commenter describes double entry as a way to verify Sage data, which may be ordinary financial control rather than an unsolved job. No non-Procore account was found in this triage pass.

## Actor map

| Role | Evidence-backed assessment | Unknowns |
|---|---|---|
| User | **FACT:** accounting personnel, project managers, and a CFO are described as using, reviewing, or controlling the synchronization/reconciliation workflow. | Which role owns exceptions at contractors of different sizes. |
| Selector | **HYPOTHESIS:** controller/CFO and construction-finance leadership are plausible selectors because the accounts place financial correctness and synchronization control with those functions. | Whether IT, operations, accounting, or project leadership controls the choice. |
| Buyer | **HYPOTHESIS:** a finance leader accountable for job-cost and billing accuracy is a plausible buyer because the sources show paid accounting, project-management, and integration spend. | No source records a decision to buy an additional residual-work solution. |
| Payer | **HYPOTHESIS:** the contractor funds the existing Procore, accounting/ERP, and integration stack. | Budget category and separate willingness to pay are unknown. |

## Quick absorption check

- **Relevant incumbent, service, free-tool, or normal-process coverage:** **FACT:** Procore provides ERP synchronization and documented reset/unlink procedures. **FACT:** its documentation describes ERP-specific conditions, auditability, and correction prerequisites. **FACT:** reconciliation reports, line-item mapping, and control routines are available as process coverage.
- **Could this be an isolated defect, poor implementation, clinical/professional judgment, or ordinary process issue?** **POSSIBLE, but not plainly established.** Each account has integration-specific facts, and verification may be an appropriate accounting control. However, the same concrete correction/reconciliation mechanism appears across three independent organizations using varied accounting-side stacks after paid adoption.
- **Contradictory evidence:** **FACT:** the incumbent has correction paths. **FACT:** at least one practitioner treats double entry as a verification method. No source demonstrates that a separate product purchase is necessary, desired, or superior to competent configuration and finance process.

## Source limitations

- **Independent URL count:** 4 (three supporting accounts and one incumbent counter-source).
- **Source-type count:** 3 (construction-software user community, construction-finance professional community, practitioner community; incumbent documentation is counterevidence).
- **Concentration or access constraints:** All three supporting accounts use Procore; two include Sage 300. Public discussion access does not establish company size, implementation quality, or frequency of the workflow.
- **Persona-fit / prevalence limits:** The evidence may concentrate on complex contracts, particular connectors, and exception cases. It cannot establish prevalence, economic magnitude, market size, or separate willingness to pay.

## Promotion gate

- [x] Narrow persona plus concrete recurring workflow.
- [x] At least three independent URLs across at least two source types, where available.
- [x] At least two attributable post-adoption signals with the same operational mechanism.
- [x] Direct link to paid software, paid labor, contractor/consultant work, or measurable economic cost.
- [x] Plausible user, selector, buyer, and payer hypothesis grounded in evidence.
- [x] Quick absorption check does not plainly explain the issue as an excluded or already-solved case.

## Rationale

**FACT:** Three independent public accounts describe paid project-management/accounting stacks with recurring change-order synchronization, correction, or reconciliation work. They differ on the accounting-side stack and context, while sharing Procore.

**ESTIMATE:** None. This CFD pass does not estimate prevalence, labor hours, cost, or market size.

**ASSUMPTION:** A future, independently authorized Scout could seek non-Procore contractor accounts, implementation/post-adoption evidence, and direct buyer/payer evidence without relying on this card.

**HYPOTHESIS:** A subset of commercial contractors may have a recurring, post-adoption change-order financial-continuity workflow that is not fully absorbed by project-management, ERP, and normal accounting controls.

**Decision rationale:** `AUTHORIZE_SCOUT` is a human-review recommendation only. The six approved CFD conditions are met at triage level, but the shared Procore dependency is a material falsification target. Before any formal Problem is considered, an authorized Scout must independently test the mechanism across non-identical incumbent stacks, separate it from integration/configuration defects and ordinary controls, and establish whether an identifiable buyer would pay separately. This card creates no canonical persona, evidence, Problem, Opportunity, or willingness-to-pay claim.

## CFD learning note

**FACT:** The authorized Scout independently reproduced paid construction project/accounting stacks, integration spend, manual synchronization and correction work, spreadsheet reconciliation, and some cross-company Procore-centered friction.

**FACT:** No formal Problem survived clustering. Cross-company recurrence alone was insufficient because the detailed cases shared Procore, the non-Procore signals were consultant/implementation-specific, and configured workflows, supported integrations, standardized administration, consolidated alternatives, and ordinary controls materially explained or absorbed the work.

**OPINION:** This is the second CFD-originated candidate to end `SCOUT_NO_PROBLEM` for a closely related structural-generalization reason: attractive paid-stack and manual-bridge signals did not establish a repeatable workflow independent of bespoke architecture, implementation conditions, incumbent/process adequacy, or normal financial control. Two pilot outcomes are insufficient to revise the CFD gate or taxonomy.

## Process safeguard

**PROCESS NOTE:** Future CFD discovery must not use user memory, prior ChatGPT conversations, known professional background, or personal interests to choose search domains unless the user explicitly authorizes that input. This construction-domain candidate is not a clean test of domain-blind CFD discovery.

## Later outcome (complete only after authorized downstream work)

- **Later outcome tag:** `SCOUT_NO_PROBLEM`
- **Later rejection pattern:** `product/vendor-specific; connector-specific; implementation/configuration-specific; ordinary control/professional judgment; insufficient cross-platform recurrence; source-quality/generalizability limitation`
- **Linked canonical records, if independently created later:** `PER-012; OBS-000200–OBS-000219; no Problem promoted`
