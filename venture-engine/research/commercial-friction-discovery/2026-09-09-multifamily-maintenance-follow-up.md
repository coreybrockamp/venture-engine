# Commercial Friction Discovery Candidate Card

**Date:** `2026-09-09`

**CFD version:** `manual-pilot-v2`

**Decision:** `REJECT`

## Candidate

- **Candidate persona:** Mid-market multifamily maintenance coordinator.
- **Existing persona ID, if any:** None; no persona is created by this card.
- **Narrow workflow:** Following a resident maintenance request from assignment through vendor estimate, resident update, invoice, and completion.
- **Trigger/context:** A public operator account described a 659-unit portfolio using AppFolio and two maintenance coordinators.
- **Operational mechanism:** Human follow-up across vendor, resident, and work-order status when reminders or ownership are weak.

## Commercial-friction evidence

- **Paid incumbent or paid labor already present:** FACT — the operator uses AppFolio and employs two coordinators; AppFolio documents paid maintenance, vendor-portal, work-order, resident, and communication coverage.
- **Existing workaround:** FACT — the public thread describes spreadsheets, Rent Manager tracking, Property Meld, Trello, and a designated queue owner as alternatives or supplements.
- **Economic consequence or labor burden:** FACT — the account attributes vendor assignment, estimates, invoices, and weekly vendor payments to the coordinator role; no separate cost or willingness-to-pay evidence was found.
- **Post-adoption friction summary:** FACT — one AppFolio user reported missing reminders/task management and described coordination work after adoption.

| Source type | Direct source link | Attributable evidence | Post-adoption mechanism | Paid/labor or economic link | Notes / limitations |
|---|---|---|---|---|---|
| Public practitioner discussion | [r/PropertyManagement: Maintenance Coordination](https://www.reddit.com/r/PropertyManagement/comments/1rqnf89/maintenance_coordination/) | A 659-unit AppFolio operator reports two coordinators handle assignment, estimates, invoices, and vendor payments; reports inadequate reminders. | Vendor and resident follow-up / status tracking. | Paid AppFolio plus coordinator labor. | One thread; several replies are promotional or unverified. |
| Incumbent documentation | [AppFolio maintenance workflow](https://www.appfolio.com/property-management-maintenance) | AppFolio describes integrated maintenance, communication, accounting, work orders, and vendor payments. | Covers the workflow at the incumbent level. | Paid property-management software. | Vendor claim, used as counterevidence rather than customer proof. |
| Incumbent documentation | [AppFolio vendor portal](https://www.appfolio.com/help/vendor-portal) | Vendors can access work orders, coordinate with managers, upload invoices/documents, and track payment status. | Covers vendor-facing portions of the loop. | Paid platform feature. | Does not prove every implementation is adequate. |
| Incumbent documentation | [AppFolio Smart Maintenance](https://www.appfolio.com/services/smart-maintenance) | Product documentation describes vendor follow-up and work-order handling automation. | Directly targets the reported follow-up mechanism. | Paid platform feature. | Marketing material; no independent outcome claim taken from it. |

## Actor map

| Role | Evidence-backed assessment | Unknowns |
|---|---|---|
| User | Maintenance coordinator performs follow-up and status work. | How frequently the pain persists after competent configuration. |
| Selector | HYPOTHESIS — property-management leadership selects the stack/process. | Decision authority in the cited organization. |
| Buyer | HYPOTHESIS — property-management company. | Whether it would buy a separate tool. |
| Payer | HYPOTHESIS — property-management company. | Separate budget and willingness to pay. |

## Quick absorption check

- **Relevant incumbent, service, free-tool, or normal-process coverage:** FACT — AppFolio, Rent Manager, Property Meld, Trello/spreadsheets, a designated queue owner, and specialized maintenance products were all raised in the public discussion. AppFolio documentation covers the central work-order, vendor, resident, and follow-up loop.
- **Could this be an isolated defect, poor implementation, clinical/professional judgment, or ordinary process issue?** YES — the only direct friction account is AppFolio-specific, and the same thread attributes improvement to ownership/checklists/process without changing software.
- **Contradictory evidence:** FACT — a commenter reports cancelling Property Meld because Rent Manager's tracker “gets the job done”; another says assigning someone to the queue and using a checklist reduces slips. These are qualitative, single-thread counterexamples, not general performance claims.

## Source limitations

- **Independent URL count:** 4 (one customer/practitioner URL; three incumbent URLs).
- **Source-type count:** 2 (public practitioner discussion; incumbent documentation).
- **Concentration or access constraints:** All direct customer evidence is concentrated in one public thread; three counter sources are incumbent documentation.
- **Persona-fit / prevalence limits:** The only operating account is a single 659-unit AppFolio user; prevalence across property-management stacks is unestablished.

## Structural-generalization check

- **Independent organizations represented:** One attributable operating organization.
- **Distinct incumbent stacks / implementations represented:** One direct AppFolio implementation; alternatives are mentioned but not independently evidenced as the same failure.
- **Same operational mechanism across those contexts?:** UNKNOWN.
- **Path A — cross-implementation recurrence evidence:** FAIL — no independently attributable recurrence across distinct paid stacks.
- **Path B — vendor-independent evidence, if cross-stack evidence is unavailable:** FAIL — no vendor-independent public source establishes the residual mechanism after competent adoption.
- **Evidence against generalization:** The direct thread frames the issue as reminders/ownership/configuration and names existing tools/processes that may absorb it.
- **Structural-generalization gate result:** `FAIL`

## Promotion gate

- [x] Narrow persona plus concrete recurring workflow.
- [ ] At least three independent URLs across at least two source types, where available.
- [ ] At least two attributable post-adoption signals with the same operational mechanism.
- [x] Direct link to paid software, paid labor, contractor/consultant work, or measurable economic cost.
- [ ] Plausible user, selector, buyer, and payer hypothesis grounded in evidence.
- [ ] Quick absorption check does not plainly explain the issue as an excluded or already-solved case.
- [ ] Structural-generalization check passes through Path A or Path B.

**Product-specific handling:** The evidence is product-specific and fails structural generalization; `AUTHORIZE_SCOUT` is not available.

## Rationale

**FACT:** The card records real paid-software adoption and coordinator labor, plus one post-adoption task/reminder complaint.

**ESTIMATE:** None.

**ASSUMPTION:** None.

**HYPOTHESIS:** A property-management firm could be a buyer only if independent evidence later showed that the residual follow-up mechanism survives competent incumbent and process use.

**Decision rationale:** `REJECT`. The public evidence does not show a structurally recurring, residual paid job. It fails independent post-adoption recurrence, absorption, buyer/payer, and both v2 structural-generalization paths. No canonical Scout resources are authorized.

## Later outcome (complete only after authorized downstream work)

- **Later outcome tag:** `NOT_YET_RUN`
- **Later rejection pattern:** `NOT_YET_RUN`
- **Linked canonical records, if independently created later:** None; this candidate was not authorized for downstream work.
