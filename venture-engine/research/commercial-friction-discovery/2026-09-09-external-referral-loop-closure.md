# Commercial Friction Discovery Candidate Card

**Date:** `2026-09-09`

**CFD version:** `manual-pilot-v2`

**Decision:** `AUTHORIZE_SCOUT`

## Candidate

- **Candidate persona:** Referral-operations manager at a multi-site outpatient provider organization that sends patients to external specialists.
- **Existing persona ID, if any:** None. This is not a request to create a persona.
- **Narrow workflow:** Close the administrative loop for external referrals: send the packet, coordinate with the patient and receiving office, confirm the appointment, obtain the consult result, and update the originating record.
- **Trigger/context:** A patient is referred outside the originating organization or EHR network, or a consult report does not return after the scheduled visit.
- **Operational mechanism:** The referral leaves one organization and system of record, then requires status chasing and information return across patient, receiving-office, and originating-provider boundaries before it can be closed.

## Commercial-friction evidence

- **Paid incumbent or paid labor already present:** **FACT:** the sources describe existing C-EMR, Visualutions referral software, Epic, and a third-party OCR component integrated with Epic. **FACT:** sources identify referral coordinators, including a full-time, non-exempt coordinator role, performing the bridging work. These are paid-stack and paid-labor signals, not evidence that a separate purchase would occur.
- **Existing workaround:** **FACT:** reported practices include referral flags, daily SQL-generated Excel lists, calls to specialist offices, fax/scan processing, future-dated follow-up flags, and referral logs/workqueues.
- **Economic consequence or labor burden:** **FACT:** the UCSF case describes access-coordinator verification/correction after automated extraction; UNC tracks time to schedule and loop closure; the Community Healthcare User Group account describes coordinator work across 12 sites. **UNKNOWN:** comparable labor cost, delay, prevalence, and budget impact across the proposed persona.
- **Post-adoption friction summary:** **FACT:** attributable accounts describe the same external-referral closure work after adopting different EHR/referral configurations. **HYPOTHESIS:** the bridge is created by cross-organization record and status boundaries, rather than by one vendor's limitation; an authorized Scout must test that claim independently.

| Source type | Direct source link | Attributable evidence | Post-adoption mechanism | Paid/labor or economic link | Notes / limitations |
|---|---|---|---|---|---|
| Healthcare practitioner community | [Community Healthcare User Group — referral coordination](https://www.chugusers.com/forums/cps-c-emr-pm/Referral-Coordinaton-Tracking-and-Follow-Up-Workflows---What-do-you-do/) | Participants describe C-EMR referral flags, Indx Logic, daily SQL-generated Excel lists across 12 sites, coordinator calls/scheduling, and follow-up for missing specialist reports. A participant also reports using Visualutions referral software. | The originating organization must pursue external scheduling and returned consult documentation after the referral is created. | Referral coordinators perform the recurring bridge work; named C-EMR and Visualutions software are in use. | Multiple organizations appear in one discussion, so individual accounts are not independent URLs. Exact staff cost is unknown. |
| Health-system operating guidance | [UNC Health — Epic referral workflow](https://news.unchealthcare.org/2015/06/epic-unc-update-training/) | UNC distinguishes external referrals, requires an acting referral coordinator per clinic, directs daily workqueue management, and requires follow-up to close the loop and receive results. | External referrals and referrals without an internal destination require active workqueue and coordinator follow-up in Epic. | Dedicated coordinator role and existing Epic implementation. | One health system; its defined process may be competent ordinary care operations rather than a separately purchasable residual job. |
| Employer job description | [Asian Services in Action — Referral Coordinator](https://www.asiaohio.org/wp-content/uploads/2019/02/Referral-Coordinator-Job-Description_2025.pdf) | A full-time, non-exempt coordinator tracks clinician/radiology referrals, obtains consultant notes, and uploads outside medical records not integrated to Epic. | External records and results must be acquired and inserted into Epic to complete the originating workflow. | Explicit full-time role using Epic. | Job description, not a customer complaint or cost study; it does not quantify volume or prove that the role is exclusively referral-loop work. |
| Public health-system case study | [UCSF — referral automation with Epic](https://www.ucop.edu/information-technology-services/initiatives/sautter-award-program/sautter-2020/ucsf-health-digital-patient-experience---patient-access-program.pdf) | UCSF describes a third-party OCR component integrated with Epic; an access coordinator still verifies and corrects transcribed referral data before creating the digital referral record. | Automation reduces fax intake work, but staff retain an exception/verification step at the cross-system handoff. | Existing Epic plus commercial OCR component and access-coordinator labor. | The source concerns intake rather than every later stage of loop closure; it supports residual administrative review, not full workflow prevalence. |
| Incumbent case study (contradictory) | [Cerner Direct Referrals — Truman Medical Centers](https://www.casestudies.com/company/cerner/case-study/truman-medical-centers-improves-patient-referral-process) | The case says Cerner Direct Referrals, centralized intake, policy change, and staff retraining materially improved handling of external referrals from 35 institutions. | An integrated referral product and standardized process can materially reduce external-referral delay and handling inconsistency. | Existing Cerner investment and operating-process coverage. | Vendor case-study context; used as absorption evidence, not independent customer-friction proof. |
| Incumbent case study (contradictory) | [ReferralMD — Baptist Memorial](https://referralmd.com/solutions/baptist-memorial-healthcare/) | ReferralMD describes an Epic-integrated platform used to organize outbound referrals, waitlists, patient interactions, and coordinator productivity. | A dedicated referral platform claims to reduce manual steps and improve processing. | Existing Epic and a 52-FTE coordinator operation. | Vendor case-study context; does not establish a separate unmet need after its adoption. |

## Actor map

| Role | Evidence-backed assessment | Unknowns |
|---|---|---|
| User | **FACT:** referral coordinators and access coordinators send, track, follow up on, and close referrals in the cited organizations. | Whether the role also owns payer authorization, clinical triage, or patient navigation in each organization. |
| Selector | **HYPOTHESIS:** referral-operations, ambulatory-care, or access leadership is a plausible selector because the sources place workflow design, staffing, and metrics with clinics and health systems. | Whether IT, revenue cycle, clinical leadership, or a referral center owns selection. |
| Buyer | **HYPOTHESIS:** a provider organization's operations or ambulatory leadership is a plausible buyer because it funds EHRs, referral products, and coordinator roles. | No source records a decision to purchase a distinct residual-work solution. |
| Payer | **HYPOTHESIS:** the provider organization pays existing EHR/referral software and coordinator labor. | Budget category, contract owner, and separate willingness to pay are unknown. |

## Quick absorption check

- **Relevant incumbent, service, free-tool, or normal-process coverage:** **FACT:** Epic workqueues/reports, Cerner Direct Referrals, ReferralMD, Visualutions, and UCSF's Epic-integrated OCR workflow provide material coverage. **FACT:** a defined referral owner and recurring follow-up are sensible normal care processes.
- **Could this be an isolated defect, poor implementation, clinical/professional judgment, or ordinary process issue?** **PARTIALLY, but not plainly.** Clinical triage, insurance decisions, patient preference, and relationship-sensitive scheduling are excluded from this candidate. The retained administrative bridge—status and documentation transfer across external organizations—appears across the cited EHR configurations, including where a formal process and automation exist. An authorized Scout must seek disconfirming evidence that competent network integration or standard operating practice eliminates the narrow loop-closure burden.
- **Contradictory evidence:** **FACT:** Cerner's case describes large improvement after centralized intake, policy change, retraining, and integrated referral technology. **FACT:** Epic supports workqueues, tracking, and reporting. These show that some organizations can absorb material portions of the work through incumbents and process.

## Source limitations

- **Independent URL count:** 6.
- **Source-type count:** 4 (healthcare practitioner community, health-system operating guidance, employer job description, public health-system case study; two vendor case studies are counterevidence).
- **Concentration or access constraints:** The direct accounts are public operational materials, not interviews or verified product reviews. Two counter-sources are vendor case studies and are used only to test absorption. Public sources do not reveal contract price, staffing allocation, or implementation maturity consistently.
- **Persona-fit / prevalence limits:** Findings may concentrate on larger systems, FQHCs, or organizations with external networks. They do not establish frequency, market size, patient outcomes, economic magnitude, or opportunity-specific willingness to pay.

## Structural-generalization check

- **Independent organizations represented:** **FACT:** the Community Healthcare User Group account(s), UNC Health, Asian Services in Action, and UCSF represent distinct operating organizations; vendor case studies add separate counterexamples.
- **Distinct incumbent stacks / implementations represented:** **FACT:** C-EMR with Indx Logic/Visualutions and SQL-generated lists; Epic with workqueues, external-record handling, and third-party OCR; and Cerner Direct Referrals are materially different configurations.
- **Same operational mechanism across those contexts?:** **YES, at triage level.** The supporting accounts describe an external referral leaving the originating environment and requiring a coordinator to track status and obtain/record the return information. They do not merely report the same vendor or connector issue.
- **Path A — cross-implementation recurrence evidence:** **PASS.** C-EMR/Visualutions and Epic implementations independently show coordinator-mediated external-referral tracking and documentation return after the referral exists in the originating system. UCSF further shows staff verification after an Epic-integrated automation step.
- **Path B — vendor-independent evidence, if cross-stack evidence is unavailable:** Not needed; Path A is the basis for this recommendation.
- **Evidence against generalization:** **FACT:** internal referral networks can use shared EHR workqueues and integrated products; centralized process/training and specialized referral platforms can materially improve the workflow. The evidence does not show that every external referral or organization retains a commercially material residual burden.
- **Structural-generalization gate result:** `PASS`

## Paid-human-role check

- **Recurring paid labor bridge:** **FACT:** referral/access coordinators are assigned to the workflow in the cited sources; the Asian Services in Action description is explicitly full-time and non-exempt.
- **Role and repeated work:** **FACT:** the role sends/records referrals, contacts patients and external offices, retrieves missing consult records, scans/uploads returned documents, and updates the originating EHR.
- **Persistence across implementations:** **FACT:** coordinator work is documented in C-EMR/Visualutions and Epic contexts, including after Epic-integrated automation at UCSF.
- **Structural versus judgment/control:** **HYPOTHESIS:** status/documentation transfer across external organizations is a structural bridge. **FACT:** clinical triage, payer authorization, patient preference, and relationship management also occur in referral operations and may explain part of the labor; they are explicit falsification targets, not evidence of automatable work.

## Promotion gate

- [x] Narrow persona plus concrete recurring workflow.
- [x] At least three independent URLs across at least two source types, where available.
- [x] At least two attributable post-adoption signals with the same operational mechanism.
- [x] Direct link to paid software, paid labor, contractor/consultant work, or measurable economic cost.
- [x] Plausible user, selector, buyer, and payer hypothesis grounded in evidence.
- [x] Quick absorption check does not plainly explain the issue as an excluded or already-solved case.
- [x] Structural-generalization check passes through Path A or Path B.

**Product-specific handling:** This is an `AUTHORIZE_SCOUT` recommendation for required human review only. It does not select a persona, authorize Scout, establish a canonical Problem or Opportunity, demonstrate a residual paid job, or prove willingness to pay.

## Rationale

**FACT:** Multiple independent organizations describe paid coordinator labor operating alongside different EHR/referral configurations to manage external-referral status and returned documentation. The cited configurations differ, while the narrow external-loop mechanism recurs.

**ESTIMATE:** None. This CFD pass does not estimate prevalence, staffing cost, patient impact, market size, or willingness to pay.

**ASSUMPTION:** A separately authorized Scout could independently access operator accounts across provider organizations, community clinics, EHR/referral implementation discussions, and public employment/process materials without relying on this card.

**HYPOTHESIS:** For a narrow subset of multi-site outpatient providers with substantial external referral volume, external-loop closure may remain an operational bridge after competent EHR/referral-tool adoption, distinct from clinical decision-making and payer-authorization judgment.

**Decision rationale:** `AUTHORIZE_SCOUT` is warranted only as a recommendation for human review because the seven v2 triage conditions pass. A later, separately authorized Scout must independently test whether the narrow bridge remains after competent use of Epic/Cerner/eCW/referral platforms; separate status/documentation transfer from clinical, insurance, relationship, and ordinary-care coordination; and seek direct buyer/payer plus separate-payment evidence.

## Rejected signals encountered during the broad pass

- **FACT:** Vendor certificate-of-insurance tracking showed real manual work and dedicated staff, but NetSuite, Sage, Acumatica, and specialist compliance products offer documented tracking, expiry, and notification coverage. The remaining work appeared largely compliance review or configuration-specific. See [NetSuite Community](https://community.oracle.com/Netsuite/english/discussion/4482937/is-there-a-way-to-track-vendor-cois), [Sage Community](https://communityhub.sage.com/us/sage_construction_and_real_estate/f/sage-300-construction-and-real-estate/155109/proper-use-of-insurance-certificate-tracking-in-sage-300-cre), and [Acumatica Community](https://community.acumatica.com/construction-120/how-do-you-track-certificates-of-insurance-16606?sort=mostRecentFirst). It was not retained.
- **FACT:** Medical credentialing has paid in-house and outsourced roles, but the evidence tied the labor to regulated credentialing, payer rules, and professional review. It did not isolate a non-judgment structural bridge and was not retained.
- **FACT:** Chargeback/fraud review has paid internal and outsourced analyst labor after risk-software adoption, but the manual queue is explicitly risk judgment and liability allocation rather than a structurally unserved administrative handoff. It was not retained.
- **FACT:** B2B EDI operations showed paid platforms, testing fees, manual invoices, and mapping work, but detailed accounts concentrated on SPS/TrueCommerce support, partner-specific implementations, or provider-switching. The mechanism did not clear structural generalization or incumbent-absorption review. See [r/EDI — SPS Commerce](https://www.reddit.com/r/edi/comments/1jp3gv1/thoughts_on_sps_commerce/) and [r/EDI — ERP integration](https://www.reddit.com/r/edi/comments/1cf6u6g/edi_for_nonedi_people/).

## Process safeguard

**PROCESS NOTE:** This pass chose generic paid-human bridge mechanisms and public-source territories without using user memory, prior chats, professional background, known projects, or personal interests. Healthcare referral coordination emerged only from that mechanism-first search; no user-context input selected it.

## Later outcome (complete only after authorized downstream work)

- **Later outcome tag:** `SCOUT_NO_PROBLEM`
- **Later rejection pattern:** `insufficient post-competent-adoption persistence; incumbent/process adequacy; necessary human/relationship work; mixed patient/payer/clinical coordination; insufficient mature cross-stack residual recurrence; buyer/payer/WTP uncertainty`
- **Linked canonical records, if independently created later:** `PER-013; OBS-000220–OBS-000240; no Problem promoted`

## Downstream learning (non-canonical)

**FACT:** The authorized Scout independently reproduced paid-human bridging, external-referral status/documentation work, and broad cross-platform workflow recurrence. **FACT:** The `manual-pilot-v2` Path A signal was directionally useful for locating a testable cross-organization workflow, but the stronger residual claim weakened under Scout and Clusterer review. The corpus did not establish that the same administrative residual persists after competent mature adoption across distinct stacks.

**FACT:** Coordinator labor includes status/documentation bridging as well as patient outreach, payer/authorization separation, clinical-information handling, and relationship-sensitive coordination. **FACT:** No formal structural Problem survived clustering. This is the first `manual-pilot-v2` candidate to pass CFD and reach Scout, and it ended `SCOUT_NO_PROBLEM`; one downstream result does not justify changing the CFD gate, taxonomy, or version.
