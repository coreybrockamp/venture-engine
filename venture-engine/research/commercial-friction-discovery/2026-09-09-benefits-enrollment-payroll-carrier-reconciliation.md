# Commercial Friction Discovery Candidate Card

**Date:** `2026-09-09`

**CFD version:** `manual-pilot-v2`

**Decision:** `REJECT`

## Candidate

- **Candidate persona:** Benefits, HRIS, or payroll administrator at a multi-carrier employer.
- **Existing persona ID, if any:** None. This is not a request to create a persona.
- **Narrow workflow:** Reconcile benefit elections, payroll deductions, carrier invoices, and effective-date changes after enrollment and during recurring payroll cycles.
- **Trigger/context:** Enrollment changes, terminations, life events, carrier bills, and payroll close.
- **Operational mechanism:** Separate benefit, payroll, and carrier records can disagree; staff compare files, investigate discrepancies, and correct deductions or enrollment records.

## Commercial-friction evidence

- **Paid incumbent or paid labor already present:** **FACT:** a public operational review identifies AlphaStaff Prism, payroll spreadsheets, and an outsourced HR team in a benefits/payroll workflow. **FACT:** public accounts describe employer payroll and carrier-bill reconciliation. These are incumbent/labor signals, not proof of a separate purchase.
- **Existing workaround:** **FACT:** reported work includes Excel comparisons, manual adjustments, and recurring review with payroll and benefits stakeholders.
- **Economic consequence or labor burden:** **FACT:** the operational review says enrollment/calculation errors can remain undetected for several payroll cycles and require retroactive adjustment; it labels the related gap high impact. **UNKNOWN:** comparable labor cost, frequency, and prevalence across employers.
- **Post-adoption friction summary:** **FACT:** three independent accounts describe reconciliation or correction work after a benefits/payroll/carrier workflow is in place. **HYPOTHESIS:** the handoff may recur across employers, but the available public record does not show that it survives competent connected-platform adoption.

| Source type | Direct source link | Attributable evidence | Post-adoption mechanism | Paid/labor or economic link | Notes / limitations |
|---|---|---|---|---|---|
| Practitioner community | [r/workday — benefit-plan invoices against payroll](https://www.reddit.com/r/workday/comments/1m1eflg/how_are_people_actually_reconciling_benefit_plan/) | An employee at a new employer reports monthly deduction discrepancies, carrier-bill differences, and manual Excel reconciliation. | Payroll deductions and carrier billing require manual comparison and correction. | Employer payroll and carrier workflow are already operating; no separate spend is stated. | One organization; the thread does not identify the complete incumbent stack or prove a recurring residual after competent configuration. |
| Practitioner community | [r/learnpython — reconciling employee benefits](https://www.reddit.com/r/learnpython/comments/su5a1j/building_a_program_to_reconcile_employee_benefits/) | A practitioner reports using Excel to compare a monthly insurance invoice with payroll deductions; employee events create mismatches. | Carrier invoice and payroll records need a recurring comparison. | Existing employee-benefits and payroll operations are implicit; no paid-tool or labor amount is reported. | One organization; no named benefits-administration platform or buyer evidence. |
| Public operational review | [Children's Trust of Alachua County operational assessment](https://mccmeetingspublic.blob.core.usgovcloudapi.net/chldtoacfl-meet-90ac58518e0d4cef87602a4a02d4b264/ITEM-Attachment-001-93667808385f41e4ab9a6d7749ca84f4.pdf) | The review identifies AlphaStaff Prism, payroll spreadsheets, outsourced HR, enrollment/calculation errors not found for several payroll cycles, and recommends a recurring verification step. | Benefits enrollment information does not reliably reach payroll without review and reconciliation. | Named external system and outsourced HR; high-impact error/correction risk. | Formal assessment, not a direct customer account; it may describe a configuration and governance gap at one organization. |
| Public process guidance (contradictory) | [OPM — joint payroll-office/carrier reconciliations](https://www.opm.gov/healthcare-insurance/healthcare/reference-materials/reference/eligibility-for-health-benefits/) | The guidance prescribes scheduled electronic matching and discrepancy resolution between payroll offices and carriers. | Reconciliation is an established control process. | Institutional process coverage; not customer-friction evidence. | Government-specific workflow; it shows ordinary control can address the mechanism. |
| Incumbent documentation (contradictory) | [Worklio — connected benefits, payroll, and carrier reconciliation](https://www.worklio.com/product/benefits) | The incumbent describes integrated elections, payroll deductions, carrier feeds, and discrepancy reporting. | A connected platform claims to reduce exports, rekeying, and missed changes. | Existing paid-suite coverage. | Vendor capability claim, not independent proof of adoption or efficacy; material absorption evidence. |
| Incumbent documentation (contradictory) | [Tabulera — carrier connections and reconciliation](https://tabulera.com/technology/carrier-connections) | The incumbent describes EDI carrier connections plus benefits and payroll reconciliation for employers, PEOs, and brokers. | Dedicated services/software address file exchange and reconciliation. | Existing paid-service coverage. | Vendor claim; it weakens a claim that the bridge is unserved. |

## Actor map

| Role | Evidence-backed assessment | Unknowns |
|---|---|---|
| User | **FACT:** benefits, payroll, and HR personnel perform or coordinate the reconciliation described in the public accounts and operational review. | Which role owns exceptions at employers of different sizes or benefit structures. |
| Selector | **HYPOTHESIS:** a benefits leader, HRIS owner, or payroll lead would select a workflow change because the work spans those functions. | Whether brokers, PEOs, finance, or HR control the selection. |
| Buyer | **HYPOTHESIS:** the employer's HR or finance leadership is a plausible buyer because it funds the benefits/payroll operation and bears correction risk. | No source records a decision to buy an additional residual-work product or service. |
| Payer | **HYPOTHESIS:** the employer pays for current payroll, benefits administration, carrier, and outsourced-HR arrangements. | Budget owner and separate willingness to pay are unknown. |

## Quick absorption check

- **Relevant incumbent, service, free-tool, or normal-process coverage:** **FACT:** OPM documents scheduled electronic matching and discrepancy resolution. **FACT:** Worklio and Tabulera describe connected enrollment, payroll, carrier-feed, and reconciliation coverage. **FACT:** the operational assessment recommends an explicit recurring verification process with the outsourced HR team.
- **Could this be an isolated defect, poor implementation, clinical/professional judgment, or ordinary process issue?** **YES, plausibly.** The detailed evidence can be explained by incomplete configuration, disconnected vendor selection, or an ordinary accuracy-control process. Public evidence does not establish the same residual burden after competent deployment of the available connected platforms and controls.
- **Contradictory evidence:** **FACT:** established platforms and scheduled reconciliation procedures directly cover the stated handoff. No independent source shows paid users switching among competent connected alternatives while retaining the same unabsorbed mechanism.

## Source limitations

- **Independent URL count:** 6.
- **Source-type count:** 4 (practitioner community, public operational review, public process guidance, incumbent documentation).
- **Concentration or access constraints:** Two direct practitioner accounts are Reddit posts; no primary interview, public review with verified stack, or cross-vendor post-adoption account was available in this triage pass. Vendor materials are used only as absorption evidence.
- **Persona-fit / prevalence limits:** Organization size, carrier count, benefits complexity, broker/PEO role, implementation maturity, and error frequency are largely unknown. The evidence cannot establish market size, cost, or separate willingness to pay.

## Structural-generalization check

- **Independent organizations represented:** **FACT:** at least three organizations/accounts are represented by the two practitioner accounts and the public operational review.
- **Distinct incumbent stacks / implementations represented:** **FACT:** AlphaStaff Prism is named in one account; the two practitioner accounts identify payroll/carrier reconciliation but not their complete stacks. Distinct competent implementations are not attributable from the available record.
- **Same operational mechanism across those contexts?:** **PARTIALLY.** Each describes a payroll-versus-benefits/carrier mismatch and manual reconciliation, but the available details do not establish the same mechanism after comparable incumbent adoption.
- **Path A — cross-implementation recurrence evidence:** **FAIL.** The sources do not show the same residual burden across two meaningfully documented stacks, vendors, or operating configurations.
- **Path B — vendor-independent evidence, if cross-stack evidence is unavailable:** **FAIL.** The public sources show that reconciliation is a recurring business control, but not that a residual commercial burden persists independently of vendor configuration or competent process. Consultant/vendor assertions are not used to fill that gap.
- **Evidence against generalization:** **FACT:** connected incumbents and scheduled electronic matching directly target the handoff; the operational review recommends a governance/process correction rather than a distinct new purchase.
- **Structural-generalization gate result:** `FAIL`

## Promotion gate

- [x] Narrow persona plus concrete recurring workflow.
- [x] At least three independent URLs across at least two source types, where available.
- [x] At least two attributable post-adoption signals with the same operational mechanism.
- [x] Direct link to paid software, paid labor, contractor/consultant work, or measurable economic cost.
- [x] Plausible user, selector, buyer, and payer hypothesis grounded in evidence.
- [ ] Quick absorption check does not plainly explain the issue as an excluded or already-solved case.
- [ ] Structural-generalization check passes through Path A or Path B.

**Product-specific handling:** This is not an `AUTHORIZE_SCOUT` candidate. Although there is real operational friction, the public record does not establish a residual mechanism that survives competent incumbent and process coverage.

## Rationale

**FACT:** Public operator and organizational accounts show manual benefits/payroll/carrier reconciliation, including Excel work, delayed-error detection, and correction risk. Public guidance and incumbent material also show established electronic matching, reconciliation services, and connected-platform coverage.

**ESTIMATE:** None. This CFD pass does not estimate prevalence, labor hours, cost, or market size.

**ASSUMPTION:** None used to elevate the candidate. A future, separately authorized CFD pass would need independent, attributable cross-stack evidence of recurring burden after competent connected-platform adoption before reconsidering this workflow.

**HYPOTHESIS:** Benefits/payroll/carrier reconciliation can be commercially important in fragmented deployments, but the present record does not support a structurally independent residual job.

**Decision rationale:** `REJECT`. Conditions 6 and 7 fail. The evidence is consistent with a real but incumbent- and process-absorbed control workflow; it must not produce persona selection or Scout authorization.

## Rejected signals encountered during the broad pass

- **FACT:** Payroll-to-ERP general-ledger mapping showed recurring manual corrections in UKG, Workday, Paycom, and multi-provider payroll discussions, but the detailed accounts pointed to mapping configuration, one vendor's reporting/access limitations, or ordinary payroll/finance control. See [UKG discussion](https://www.reddit.com/r/Payroll/comments/1nunm8h), [Paycom discussion](https://www.reddit.com/r/Payroll/comments/1rmrvoy/paycom/), and [SAP mapping guidance](https://community.sap.com/t5/human-capital-management-q-a/interface-sap-erp-hcm-payroll-to-sap-s-4hana-public-cloud-g-l-account/qaa-p/14476953/highlight/true). The multi-provider payroll-to-ERP account was also concentrated in one uncorroborated forum thread, so it could not satisfy v2 structural generalization.
- **FACT:** Freight-bill audit/reconciliation, accounts-payable invoice review, and marketplace-accounting reconciliation showed paid services or tools plus manual work, but the available evidence commonly described ordinary audit/control work, implementation-specific exceptions, or established TMS/accounting/connector coverage. They were not retained as candidate cards.
- **FACT:** Identity-access review showed spreadsheet-based collection across SaaS systems, but native governance tools and required review controls made the apparent bridge too close to an incumbent-coverage and normal-control case at triage level. It was not retained as a candidate card.

## Later outcome (complete only after authorized downstream work)

- **Later outcome tag:** `NOT_YET_RUN`
- **Later rejection pattern:** `NOT_YET_RUN`
- **Linked canonical records, if independently created later:** None. No downstream work is authorized.
