# Commercial Friction Discovery Candidate Card

**Date:** `2026-09-09`

**CFD version:** `manual-pilot-v2`

**Decision:** `REJECT`

## Candidate

- **Candidate persona:** Dental-practice billing or accounts-receivable manager.
- **Existing persona ID, if any:** None; no persona is created by this card.
- **Narrow workflow:** Matching insurance remittance/payment details to patient claims and posting balances after practice-management-system adoption.
- **Trigger/context:** A public dental-office account described hours of daily payment posting in a Tracker-based workflow.
- **Operational mechanism:** Manual claim matching when payer statements or remittance data are not integrated with the practice-management system.

## Commercial-friction evidence

- **Paid incumbent or paid labor already present:** FACT — the direct account uses Tracker; the role handles payment posting and receivables. Industry documentation describes paid practice-management, clearinghouse, and electronic-remittance capabilities.
- **Existing workaround:** FACT — the account prints or downloads insurer statements and manually finds each matching claim; replies recommend 835/ERA files and electronic posting.
- **Economic consequence or labor burden:** FACT — the account reports 75–100 pages of reports and hours of daily work, but no independently verified cost or separate willingness-to-pay evidence was found.
- **Post-adoption friction summary:** FACT — the direct account reports the paper and electronic statements are not integrated into its PMS; this is one stack/integration condition.

| Source type | Direct source link | Attributable evidence | Post-adoption mechanism | Paid/labor or economic link | Notes / limitations |
|---|---|---|---|---|---|
| Public practitioner discussion | [r/CodingandBilling: dental payment posting](https://www.reddit.com/r/CodingandBilling/comments/1d3ih18/posting_payments_has_to_be_a_better_way_dental/) | A Canadian office with about 10 dentists reports 75–100 pages of reports, manual claim matching, and hours of daily posting in Tracker. | No remittance-to-PMS integration. | Paid PMS plus staff payment-posting labor. | One office and one PMS/country context. |
| Public practitioner discussion | [r/DentalInsurance: secondary payment error](https://www.reddit.com/r/DentalInsurance/comments/1u9ohkp/recvd_payment_from_secondary_but_submitted_claim/) | A Dentrix user reports occasional secondary-insurer payments against a primary claim and says there is no official tracking entry for that error. | Payer/order exception. | Paid PMS; no labor or frequency quantified. | Narrow exception, not evidence of a broad recurring workflow. |
| Industry association guidance | [ADA EDI transaction guide](https://www.ada.org/-/media/project/ada-organization/ada/ada-org/files/resources/practice/dental-insurance/aes-editransactionsfordental101.pdf) | The 835 is described as electronic payment/remittance information that supports reconciliation; practice systems are described as providing payment reconciliation capabilities. | Standard electronic remittance path. | Existing industry infrastructure. | Guidance, not operator outcome evidence. |
| Incumbent documentation | [Dentrix billing and payments suite](https://www.dentrix.com/dental-solutions/dental-insurance-billing-and-collections/billing-and-payments-suite/) | Dentrix documents automatic ledger posting and ERA payment posting. | Directly covers ordinary payment-posting workflow. | Existing paid practice-management tooling. | Vendor claim, retained as counterevidence. |
| Incumbent documentation | [Dentrix batch insurance payment entry](https://blog.dentrix.com/blog/2013/08/13/entering-batch-insurance-payments/) | Dentrix documents batch and electronic EOB/ERA payment-entry options. | Covers multi-claim payment posting. | Existing paid feature/option. | Vendor documentation; configuration/access varies. |

## Actor map

| Role | Evidence-backed assessment | Unknowns |
|---|---|---|
| User | Billing/AR staff matches and posts insurance payments. | How common this work remains after capable electronic remittance setup. |
| Selector | HYPOTHESIS — practice owner or office manager selects PMS, clearinghouse, and workflow. | Decision authority in the cited practice. |
| Buyer | HYPOTHESIS — dental practice. | Separate budget beyond PMS/clearinghouse. |
| Payer | HYPOTHESIS — dental practice. | Separate willingness to pay for an exception bridge. |

## Quick absorption check

- **Relevant incumbent, service, free-tool, or normal-process coverage:** FACT — 835/ERA remittance standards, clearinghouses, Dentrix automatic posting, and batch-entry features cover ordinary payment posting. The public discussion itself identifies electronic/automated posting as an established alternative.
- **Could this be an isolated defect, poor implementation, clinical/professional judgment, or ordinary process issue?** YES — the main account explicitly lacks integration between its remittance sources and Tracker; secondary-insurance ordering is payer-specific exception work.
- **Contradictory evidence:** FACT — commenters report electronic/automated posting has been standard for many years, and official materials document ERA/835 and batch/automatic posting paths. These sources do not prove universal adequacy.

## Source limitations

- **Independent URL count:** 5 (two practitioner URLs; one association guide; two incumbent URLs).
- **Source-type count:** 3 (public practitioner discussions; association guidance; incumbent documentation).
- **Concentration or access constraints:** The only quantified customer evidence is one Tracker-based Canadian practice. No independent recurrence after competent electronic-remittance adoption was found.
- **Persona-fit / prevalence limits:** Payer mix, country, clearinghouse, PMS, electronic-remittance enrollment, and secondary-coverage rules vary materially.

## Structural-generalization check

- **Independent organizations represented:** Two practitioner accounts, but only one describes recurring quantified work.
- **Distinct incumbent stacks / implementations represented:** Tracker/nonintegrated remittance workflow; Dentrix secondary-payment exception.
- **Same operational mechanism across those contexts?:** FAIL — one is a primary integration gap and the other is a narrow payer-order exception.
- **Path A — cross-implementation recurrence evidence:** FAIL — no one specific residual mechanism recurs across the two stacks.
- **Path B — vendor-independent evidence, if cross-stack evidence is unavailable:** FAIL — standards and established practice-management/clearinghouse features materially cover the normal workflow.
- **Evidence against generalization:** Electronic remittance, automatic/batch posting, and clearinghouse-supported reconciliation are documented existing paths.
- **Structural-generalization gate result:** `FAIL`

## Promotion gate

- [x] Narrow persona plus concrete recurring workflow.
- [x] At least three independent URLs across at least two source types, where available.
- [ ] At least two attributable post-adoption signals with the same operational mechanism.
- [x] Direct link to paid software, paid labor, contractor/consultant work, or measurable economic cost.
- [ ] Plausible user, selector, buyer, and payer hypothesis grounded in evidence.
- [ ] Quick absorption check does not plainly explain the issue as an excluded or already-solved case.
- [ ] Structural-generalization check passes through Path A or Path B.

**Product-specific handling:** The evidence is integration/payer-context specific and structural generalization fails; `AUTHORIZE_SCOUT` is not available.

## Rationale

**FACT:** One dental practice reports a substantial manual payment-posting burden after adopting its PMS.

**ESTIMATE:** None.

**ASSUMPTION:** None.

**HYPOTHESIS:** A residual payment-posting job might exist only if independent evidence showed one payer- and vendor-independent exception mechanism that persists after competent ERA/clearinghouse/PMS adoption.

**Decision rationale:** `REJECT`. The direct pain is real but concentrated in a nonintegrated Tracker workflow. Existing electronic-remittance standards, clearinghouse paths, and practice-management features absorb the normal job; the remaining exception evidence is too narrow and heterogeneous for a structural residual paid-job hypothesis. No canonical Scout resources are authorized.

## Later outcome (complete only after authorized downstream work)

- **Later outcome tag:** `NOT_YET_RUN`
- **Later rejection pattern:** `NOT_YET_RUN`
- **Linked canonical records, if independently created later:** None; this candidate was not authorized for downstream work.
