# PER-013 Scout Checkpoint — External Referral-Loop Closure

**Stage:** Scout complete; no clustering performed.
**Scope:** FACT-based public-source review only. No Problem, competitor, Opportunity, score, experiment, offer, landing page, or automation record was created.

## Coverage and quality controls

| Measure | Result |
|---|---:|
| Observations added | 21 |
| Independent URLs | 10 |
| Source types | 5 |
| Largest single-URL contribution | 4 observations (19%) |

| Source type | Observations | Share |
|---|---:|---:|
| Health-system/public workflow materials | 9 | 43% |
| Practitioner or EHR-user communities | 6 | 29% |
| Employer job description | 2 | 10% |
| Reddit practitioner discussion | 2 | 10% |
| Referral-platform case material | 2 | 10% |

The normal-batch source-diversity target is met and no URL exceeds the 25% concentration rule. Public health-system materials establish actual operating processes but are not necessarily adverse customer accounts. The referral-platform and Cerner materials are vendor-published or vendor-associated case studies and are retained primarily as incumbent/process counterevidence. The Reddit source includes a later promotional reply and is treated cautiously.

| Evidence tier | Count |
|---|---:|
| Tier 1 — behavioral/spend or paid use | 3 |
| Tier 2 — active intent | 0 |
| Tier 4 — problem or contradictory evidence | 18 |

| Source-role classification | Observations |
|---|---:|
| Internal operator / practitioner or identified internal role | 13 |
| Vendor / case-material source | 6 |
| Role unclear | 2 |

## Observed themes (not formal Problem clusters)

- **External status and returned-record bridge work (8 observations):** C-EMR participants report missing electronically returned specialist reports, daily open-referral lists, calls, future-dated reminders, and faxed requests for notes; an Epic-role description includes scanning outside records that are not integrated into Epic ([OBS-000220](../../data/observations.jsonl)–[OBS-000222](../../data/observations.jsonl), [OBS-000227](../../data/observations.jsonl)). One Epic user reports manual re-entry of outside referrals ([OBS-000235](../../data/observations.jsonl)).
- **Coordinator labor alongside paid systems (5 observations):** coordinator roles are documented in C-EMR, Epic, NextGen, and a ReferralMD/Epic customer case, including a full-time job description and a 52-FTE referral center ([OBS-000221](../../data/observations.jsonl), [OBS-000226](../../data/observations.jsonl), [OBS-000232](../../data/observations.jsonl), [OBS-000239](../../data/observations.jsonl)). This is paid-labor evidence, not proof that the labor is reducible or that a new buyer exists.
- **Post-adoption exception work, but uneven recurrence (4 observations):** UCSF retained coordinator verification/correction after Kofax OCR was integrated with Epic; the Epic outside-message account reports manual re-entry; the Asian Services in Action role scans external records into Epic ([OBS-000227](../../data/observations.jsonl), [OBS-000229](../../data/observations.jsonl), [OBS-000235](../../data/observations.jsonl)). The detailed direct evidence remains concentrated in Epic and C-EMR contexts; it does not yet prove that the same residual survives competent use across every mature stack.
- **Incumbent and process absorption (11 observations):** Visualutions is reported to improve tracking; Epic workqueues and CareLink support tracking through completion; NextGen documents agreements for return reports; Cerner Direct Referrals plus process/training materially improved a referral cycle; ReferralMD reports throughput improvement using Epic integration, alerts, waitlists, and communication ([OBS-000223](../../data/observations.jsonl), [OBS-000225](../../data/observations.jsonl), [OBS-000230](../../data/observations.jsonl)–[OBS-000234](../../data/observations.jsonl), [OBS-000236](../../data/observations.jsonl), [OBS-000238](../../data/observations.jsonl), [OBS-000240](../../data/observations.jsonl)).

## Recurring workflow, paid stack, and workaround evidence

**FACT:** Named systems and services in the corpus include C-EMR, Indx Logic, Visualutions, Epic, Epic CareLink, Epic Care Everywhere, Kofax, Luma Health, NextGen, Cerner Direct Referrals, and ReferralMD. These establish paid-stack adoption or existing system use; they do not establish separate willingness to pay for a new workflow change.

**FACT:** Reported administrative practices include daily SQL/Excel worklists, external-office calls, one-month future flags, faxed letters to request notes, manual scan/upload of outside records, workqueues, care-coordination agreements, patient messaging, and alerts. The operational task is heterogeneous: some elements are status/documentation bridging; others are legitimate patient communication, clinical information collection, or payer work.

**FACT:** Direct paid-human signals include a full-time referral-coordinator job description and a vendor-published account of 52 FTE coordinators. The source set does not supply comparable wage, hours-per-referral, or allocation data across organizations.

## Cross-platform recurrence and structural assessment

**FACT:** C-EMR/Indx Logic practitioners describe fax/scan return, SQL/Excel worklists, and coordinator follow-up. Epic sources describe external-record scanning, referral workqueues, coordinator roles, and a post-OCR exception-review step. NextGen documents the process requirement for specialist reports returning to the referrer. Cerner documents external-referral intake before and after a dedicated-referral-product/process change.

**INFERENCE:** The Scout independently reproduces a cross-platform *category* of external referral tracking and return work. It does **not yet establish** the same recurring residual administrative mechanism after competent adoption across two non-identical mature EHR/referral stacks. Epic itself offers Care Everywhere, CareLink, workqueues, and related tracking; Cerner and ReferralMD case materials show that centralization, training, and referral technology can materially absorb parts of the workflow.

## Buyer and payer evidence

**FACT:** Referral coordinators, access coordinators, clinic managers, medical directors, clinic administrators, and referral-center staff appear in the sources. UNC assigns clinic medical directors and administrators responsibility for referral process compliance and tracking. Baptist Memorial’s vendor case identifies a referral center and management needs for reports and partner-network management.

**UNKNOWN:** No independent source establishes a selection process, budget owner, contract price, or separate willingness to pay for a residual external-loop workflow. Provider organizations demonstrably fund EHRs, referral tools, and coordinator labor, but current spend is not evidence of a new buyer gap.

## Incumbent adequacy and negative evidence

- **FACT:** A Visualutions user reports improved tracking and clearing old orders ([OBS-000223](../../data/observations.jsonl)).
- **FACT:** UNC’s Epic/CareLink workqueues, metrics, process requirements, and electronic-referral functionality provide substantial process coverage ([OBS-000224](../../data/observations.jsonl)–[OBS-000225](../../data/observations.jsonl)).
- **FACT:** UCSF combined Epic with Kofax, a custom interface, Patient Connect, and Luma Health to reduce manual intake and support scheduling; staff still review exceptions ([OBS-000229](../../data/observations.jsonl)–[OBS-000230](../../data/observations.jsonl)).
- **FACT:** NextGen documents agreements for bidirectional report flow; UI Health Care documents Epic tracking and configurable workqueues ([OBS-000231](../../data/observations.jsonl), [OBS-000233](../../data/observations.jsonl)).
- **FACT:** Cerner and ReferralMD case material reports material process/throughput improvement after centralized or dedicated referral-platform adoption ([OBS-000238](../../data/observations.jsonl), [OBS-000240](../../data/observations.jsonl)).

## Structural-versus-relationship/judgment assessment

**FACT:** Missing status and returned records across independent organizations are distinct administrative tasks in the corpus. **FACT:** appointment scheduling requires direct patient dialogue in UNC’s process; sources also include clinical information collection, payer authorization, and patient choice.

**INFERENCE:** The evidence supports a narrow structural administrative hypothesis—external status/documentation return—but does not support treating all coordinator labor as reducible or as a product gap. Clinical triage, authorization, patient adherence, and necessary relationship work must remain separate in any later clustering.

## CFD hypothesis check (non-canonical traceability)

**Independently reproduced:** paid coordinator labor; external-referral workqueues and manual follow-up; external records not automatically returned to the originating EHR; and a cross-platform category spanning C-EMR, Epic, NextGen, and Cerner-related workflows.

**Weakened:** Path A is materially less conclusive at Scout level than at CFD triage. The strongest detailed adverse accounts are C-EMR and Epic. NextGen supplies process/capability guidance rather than a persistent post-adoption adverse account, while Cerner and ReferralMD show significant absorption through tooling, centralization, training, and alerts.

**Absorption check:** strengthened. Competent EHR configuration, interoperability, dedicated referral systems, staff ownership, external-provider agreements, and workflow redesign can cover substantial parts of the narrow loop.

**Paid-human classification:** mixed. Some labor directly bridges missing status/documentation, while other labor is clinical, payer, patient-choice, or relationship work that this project must not collapse into an automation premise.

## Evidence-quality constraints and gaps

- Direct adverse operator evidence after competent adoption of two different mature stacks remains limited.
- Public sources do not consistently distinguish internal versus external referral volume, referral complexity, system configuration, adoption maturity, or task allocation by role.
- Job descriptions prove roles exist but not the economics, cadence, or residual buyer gap; vendor case studies may be selective.
- No source establishes a formal Problem, residual paid job, separate willingness to pay, a new buyer/payer, opportunity, or market attractiveness.

## Next permitted action

Review this PER-013 Scout checkpoint with the user. Do not start Problem Clustering without separate authorization.
