# Commercial Friction Discovery Candidate Card

**Date:** `2026-09-29`  
**CFD version:** `manual-pilot-v2`  
**Decision:** `AUTHORIZE_SCOUT` — recommendation for human review only; not approval.

## Candidate

- **Candidate persona:** Authorization operations lead at a multi-payer outpatient medical practice.
- **Existing persona ID, if any:** None confirmed. Proposed persona ID: `NEW` (assign only after human review).
- **Proposed persona slug:** `outpatient-prior-authorization-operations-lead`.
- **Narrow workflow:** Route, assemble, submit, and follow up prior-authorization requests across EHR, ePA tools, and payer portals; exclude clinical appropriateness and appeal judgment.
- **Trigger/context:** A clinician orders a medication or service that requires a payer authorization.
- **Operational mechanism:** Staff must move case details, documentation, and status across independent payer channels even after adopting EHR/ePA tools.

## Commercial-friction evidence

- **Paid incumbent or paid labor already present:** EHR/ePA and payer portals are in use; the AMA reports 40% of surveyed physicians employ staff dedicated solely to PA tasks. This is staffing spend, not proof of willingness to pay for another product.
- **Existing workaround:** Dedicated authorization staff, payer-portal logins, manual chart assembly, status checks, and workflow specialization.
- **Economic consequence or labor burden:** AMA's 2025 physician survey reports an average 13 physician/staff hours per week on PA and 40% with dedicated PA staff. These are survey estimates, not candidate-specific spend.
- **Post-adoption friction summary:** An MA using CoverMyMeds still consolidates chart documents; another MA describes multiple payer portals despite an EHR and CoverMyMeds. MGMA's practice-leader polling describes EHR-to-portal switching and re-entry.

| Source type | Direct source link | Attributable evidence | Post-adoption mechanism | Paid/labor or economic link | Notes / limitations |
|---|---|---|---|---|---|
| Public practitioner discussion | [MedicalAssistant: Prior authorizations](https://www.reddit.com/r/MedicalAssistant/comments/1ue49ru/prior_authorizations/) | Original MA reports ~15 cases on a busy day, follow-up next day, and using CoverMyMeds while manually downloading and consolidating chart documents. | Documentation assembly and follow-up after tool adoption. | Staff labor; no wage or separate-product spend measured. | One self-report; medication cases only. |
| Public practitioner discussion | [MedicalAssistant: Prior Auths efficiency](https://www.reddit.com/r/MedicalAssistant/comments/1lh5aai/prior_auths_how_can_we_make_this_more_efficient/) | MAs describe payer-specific channels, multiple portal accounts, and outsourced/dedicated PA labor; one describes 60 authorizations daily. | Routing and follow-up despite EHR and CoverMyMeds availability. | Dedicated MA role and outsourced imaging-center work, but no contract price. | Multiple commenters on one URL count as one independent URL. |
| Medical-practice association analysis | [MGMA: payer portals](https://www.mgma.com/mgma-stat/how-many-payer-portals-is-too-many-most-practices-already-know-their-answer) | MGMA reports a 252-response poll: 61% of practices access at least seven payer portals weekly; it describes auth submission/status steps that cannot be completed through EHR or standard files. | Payer-channel fragmentation after EHR/clearinghouse adoption. | Staff time; no incremental vendor spend established. | Association article mixes poll data with illustrative workflow; the vignette is not treated as a sampled case. |
| Medical-practice association survey | [AMA: 2025 PA survey](https://www.ama-assn.org/practice-management/prior-authorization/only-1-3-doctors-trusts-insurers-prior-authorization) | Of 1,000 physicians surveyed, 27% report EHR/e-prescribing PA requirement information rarely/never accurate; reported average is 40 PAs and 13 staff/physician hours weekly; 40% employ dedicated PA staff. | Incomplete EHR information plus continuing manual PA labor. | Direct staffing signal at survey level. | Not a measure of residual burden specifically among competent ePA adopters. |

## Actor map

| Role | Evidence-backed assessment | Unknowns |
|---|---|---|
| User | PA coordinator/MA; firsthand MA accounts and MGMA practice-staff poll. | Exact division between clinical and administrative tasks. |
| Selector | Practice manager or authorization lead is a plausible workflow selector. | Who chooses technology in each practice. |
| Buyer | Practice administrator/owner is a plausible economic buyer, given staffing and RCM-tool decisions. | Procurement authority and incremental budget. |
| Payer | Practice/employing medical group funds staff and incumbent systems. | Whether any practice would pay separately for this residual workflow. |

## Quick absorption check

- **Relevant incumbent, service, free-tool, or normal-process coverage:** EHR/ePA, CoverMyMeds, clearinghouses, payer portals, dedicated staff, and outsourcing cover important portions. MGMA says clearinghouse consolidation can reduce logins; role specialization and process guides help. AMA notes insurer standardization/ePA efforts. These may absorb some or all of the residual task in better-implemented practices.
- **Could this be isolated defect, poor implementation, clinical/professional judgment, or ordinary process?** Some chart/rationale work is clinical and must stay outside this candidate. A four-file CoverMyMeds limit is product-specific; it is not the general mechanism. The administrative routing/status bridge is cross-payer and not plainly one broken implementation, but Scout must test competent-adoption alternatives.
- **Contradictory evidence:** In a separate [FamilyMedicine discussion](https://www.reddit.com/r/FamilyMedicine/comments/1vgj307/prior_auths_make_me_want_to_pull_my_hair_out/), a small practice says Athena handles much of its PA work and describes the remainder as simple; other clinicians use CoverMyMeds or visit-based process. This is a substantial absorption counterexample. Separate willingness to pay is unknown.

## Source limitations

- **Independent URL count:** 5, including the contradictory FamilyMedicine URL; four supporting URLs.
- **Source-type count:** 2 — practitioner forums and professional-association reporting/survey. Multiple subreddits do not create additional source types.
- **Concentration or access constraints:** Each of five URLs contributes at most one independent source. Two practitioner threads are Reddit; MGMA and AMA provide the other type. No gated source used.
- **Persona-fit / prevalence limits:** MGMA/AMA surveys are broad across practices; the narrow outpatient buyer segment and post-adoption prevalence remain unverified. Public forum accounts are self-selected.

## Structural-generalization check

- **Independent organizations represented:** At least two self-reported practitioner contexts plus MGMA/AMA multi-practice survey populations; identities and overlap are not independently verified.
- **Distinct incumbent stacks / implementations represented:** CoverMyMeds plus unspecified EHR/portal stacks in practitioner accounts; MGMA covers diverse practices without naming each stack. A true Path A cross-stack proof is **not** established.
- **Same operational mechanism across contexts?:** Administrative data/status transfer between practice systems and payer-specific channels appears in the MA accounts and MGMA reporting. Clinical rationales and denials are related but not conflated with the administrative bridge.
- **Path A — cross-implementation recurrence evidence:** `UNKNOWN`; named distinct stacks with directly comparable workflows were not established.
- **Path B — vendor-independent evidence:** `PASS` provisionally. MGMA's 252-response practice-leader poll and qualitative responses attribute repeated re-entry, status checking, and portal use to payer-specific channel fragmentation; this exists across practices and is not one vendor connector defect. AMA's physician survey corroborates continuing PA labor and incomplete EHR information. Scout must test whether competent EHR/ePA adoption or clearinghouse services remove the bridge in the target segment.
- **Evidence against generalization:** Athena counterexample; 2027 payer API/ePA changes may reduce the job; some accounts are medication-specific while MGMA describes both medication and service auths.
- **Structural-generalization gate result:** `PASS` via Path B only, provisional for Scout triage.

## Promotion gate

- [x] Narrow persona plus concrete recurring workflow.
- [x] At least three independent URLs across at least two source types.
- [x] At least two attributable post-adoption signals with the same administrative bridge mechanism (MA with CoverMyMeds; MGMA practice accounts with EHR/portals).
- [x] Direct link to paid labor/economic cost (AMA dedicated-staff survey and practitioner staffing accounts).
- [x] Plausible user, selector, buyer, and payer hypothesis grounded in staffing and practice workflow evidence.
- [x] Quick absorption check does not plainly show a single defect or normal process universally resolves the bridge; major counterexamples are retained.
- [x] Path B structural-generalization check passes provisionally; Path A remains unproven.

## Rationale

**FACT:** The linked sources document repeated manual administrative PA work after tool adoption, payer-channel fragmentation, and dedicated staff.  
**ESTIMATE:** The AMA survey averages are population estimates, not a price or a practice-specific cost.  
**ASSUMPTION:** A practice administrator may control budget for reducing the administrative bridge; this must be checked in Scout.  
**HYPOTHESIS:** An administrative handoff job may remain across payer channels after competent EHR/ePA adoption. No separate product or willingness to pay is established.  
**OPINION:** This is worth canonical Scout falsification, not Market Analysis or product design.

**Decision rationale:** `AUTHORIZE_SCOUT` as a CFD recommendation only. The public evidence provisionally clears the seven-part v2 triage gate, with explicit absorption and source limitations. Human review is mandatory. Do not create a persona or begin Scout/Bundle 2 without separate approval.

## Later outcome (complete only after authorized downstream work)

- **Later outcome tag:** `NOT_YET_RUN`
- **Later rejection pattern:** `NOT_YET_RUN`
- **Linked canonical records, if independently created later:** None.
