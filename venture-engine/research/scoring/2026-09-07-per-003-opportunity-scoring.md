# PER-003 Opportunity Scoring

## Method

**FACT:** This pass applied `config/scoring-rubric.yaml` unchanged: ten 1–10 dimensions, the configured weights, then `weighted_total × 10`, rounded to a whole number. Founder fit is a neutral 5 for every record because no founder-specific evidence is in the repository. Opportunity score measures commercial attractiveness; confidence measures confidence that the score is approximately correct.

## Ranked Results

| Rank | Opportunity | Score | Confidence | Readiness |
|---:|---|---:|---:|---|
| 1 | OPP-0007 Revenue Exception Intervention Queue | 43 | 48 | NOT READY |
| 2 | OPP-0008 FSM Implementation Readiness Service | 39 | 46 | NOT READY |
| 3 | OPP-0006 Dispatch Exception Decision Queue | 38 | 45 | NOT READY |

No record meets the rubric's 70-point experiment-eligibility band. No strategic decision, experiment, offer, landing page, or automation was created.

## OPP-0007 — Revenue Exception Intervention Queue

| Dimension | Score | Key evidence | Key counterevidence | Dimension confidence / missing evidence |
|---|---:|---|---|---|
| Pain severity | 6 | Estimate backlog and invoice rework can affect conversion/cash timing. | No verified loss, close rate, or days-to-payment. | Medium / economic magnitude. |
| Existing customer spending | 5 | Firms pay for FSM quote-to-cash capabilities. | This is bundled category spend, not the proposed queue. | Medium / standalone spend. |
| Willingness to pay | 2 | Active follow-up concern exists. | No request or payment for prioritization; Jobber already automates follow-up. | Low / buyer payment. |
| Frequency | 5 | Estimates, invoices, and payment review recur per job. | Frequency of unresolved intervention decisions is unknown. | Low / daily-weekly cadence. |
| Poor existing solutions | 3 | Backlog and mobile-invoice rework are observed. | All incumbents cover the core flow; Jobber reduced invoice chasing for one reviewer. | Low / post-implementation prevalence. |
| Customer reachability | 4 | Owner, FSM, and QuickBooks-adjacent communities are plausible. | No validated trigger-channel conversion path. | Low / reachable buyer economics. |
| Market size | 3 | Field service is a paid category. | No addressable niche or standalone category estimate. | Low / niche economics. |
| AI/software leverage | 5 | Prioritization could surface exceptions from status data. | Rules, reports, or automation may suffice. | Low / incremental outcome. |
| Speed to validate | 7 | A workflow audit or mocked queue could examine the decision before an integration. | Access to real exception data is unproven. | Medium / buyer access. |
| Founder fit / strategic interest | 5 | Neutral, per rubric policy. | No founder evidence recorded. | Low / founder input. |

**Overvaluation risk:** existing FSM automation and reporting already handle the relevant exceptions.
**Undervaluation risk:** a high-value intervention decision may be hidden inside generic FSM status data and not visible in public complaints.
**Confidence:** 48/100 — the underlying problem has six independent URLs and three source types, but opportunity-specific WTP, residual-pain frequency after competent setup, and measurable benefit are unverified.

## OPP-0008 — FSM Implementation Readiness Service

| Dimension | Score | Key evidence | Key counterevidence | Dimension confidence / missing evidence |
|---|---:|---|---|---|
| Pain severity | 4 | Setup, migration, and selection friction are documented. | Typical cost, disruption, and ROI are unknown. | Medium / consequence magnitude. |
| Existing customer spending | 6 | Vendor onboarding, paid migration, and professional services are documented. | Independent-service spending is unverified. | Medium / comparable engagements. |
| Willingness to pay | 3 | Existing vendor professional services make a payer plausible. | No evidence owners prefer a neutral third party. | Low / independent WTP. |
| Frequency | 2 | Switching happens at growth, renewal, or adoption triggers. | It is episodic, not a recurring operating decision. | Medium / purchase cadence. |
| Poor existing solutions | 3 | Setup complexity and fit concerns appear in public records. | Vendors already provide tiers, trials, onboarding, and migration. | Low / service gap. |
| Customer reachability | 4 | Search, advisors, and consultant referrals plausibly meet the switch trigger. | No verified efficient channel. | Low / channel economics. |
| Market size | 3 | A paid implementation category exists. | Addressable 5–25-person independent-service market is unknown. | Low / niche economics. |
| AI/software leverage | 2 | Workflow tools may support delivery. | The core offer is a service, not defensible software leverage. | Medium / delivery model. |
| Speed to validate | 8 | A fixed-scope service proposition can be evaluated without an integration. | Demand and delivery repeatability remain unknown. | Medium / buyer access. |
| Founder fit / strategic interest | 5 | Neutral, per rubric policy. | No founder evidence recorded. | Low / founder input. |

**Overvaluation risk:** vendor onboarding or internal implementation sufficiently solves the job.
**Undervaluation risk:** owners may value an impartial, bounded preparation engagement more than public vendor materials reveal.
**Confidence:** 46/100 — the problem has broad source support and direct vendor-service evidence, but the independent-service wedge, buyer preference, scope repeatability, and willingness to pay remain unverified.

## OPP-0006 — Dispatch Exception Decision Queue

| Dimension | Score | Key evidence | Key counterevidence | Dimension confidence / missing evidence |
|---|---:|---|---|---|
| Pain severity | 5 | Manual storm route ordering and a mobile field-view gap are concrete. | No quantified utilization, missed-job, or labor effect. | Low / economic magnitude. |
| Existing customer spending | 5 | Paid FSM use is documented. | No spend for exception decision support. | Medium / standalone spend. |
| Willingness to pay | 2 | Paid operational tools show category spend. | No separate demand for a decision layer. | Low / buyer payment. |
| Frequency | 4 | Dispatch is daily; disruptions are plausible. | Frequency of true exceptions is unmeasured. | Low / exception cadence. |
| Poor existing solutions | 3 | One Jobber user manually orders routes during storms. | All reviewed FSMs cover dispatch and some users report strong outcomes. | Low / post-implementation prevalence. |
| Customer reachability | 4 | FSM ecosystems and trade communities are plausible. | No tested route to owners at a disruption trigger. | Low / channel economics. |
| Market size | 3 | Dispatch is a broad paid workflow. | Narrow add-on niche and addressable economics are unknown. | Low / niche economics. |
| AI/software leverage | 5 | Constraints and exceptions may support decision assistance. | Deep, real-time access and human judgment may erase incremental value. | Low / better-than-rules outcome. |
| Speed to validate | 6 | A manual exception review can precede software. | Credible assessment needs real schedule data. | Medium / data access. |
| Founder fit / strategic interest | 5 | Neutral, per rubric policy. | No founder evidence recorded. | Low / founder input. |

**Overvaluation risk:** incumbent dispatch boards and human dispatcher judgment already work well enough.
**Undervaluation risk:** rare disruptions may have disproportionate capacity or customer consequences that public records do not quantify.
**Confidence:** 45/100 — the parent problem has six independent URLs and three source types, but this hypothesis rests on two opportunity-linked examples and lacks measured post-adoption frequency, ROI, WTP, or integration evidence.

## Comparison to PER-001

PER-003 shows clearer category spend and a more identifiable owner/operator buyer than the caregiver opportunities. It ranks weaker at opportunity-specific WTP and poor-existing-solution evidence because incumbents explicitly cover the three workflows. PER-003 add-ons have plausible operational recurrence but unproven residual frequency and integration dependence. The implementation service is fast to assess but episodic. By comparison, PER-001's best records scored 53–59 after targeted evidence closing; no comparison proves either persona commercially superior. On current evidence, PER-003 is less ready because every hypothesis depends on distinguishing an add-on/service from existing FSM capability.

## Scorer Critique and Evidence Needed

What worked: source-diverse upstream problem records, competitor analysis, and preserved contradiction made it possible to distinguish category spend from offer demand. Hardest dimensions: opportunity-specific WTP, post-implementation residual pain, narrow market size, and channel economics. Residual-pain uncertainty materially limited every score. Before any further stage, obtain direct owner/operator evidence on the exact decision that remains manual after competent FSM adoption, its weekly/monthly frequency, measurable consequence, current workaround, and whether the owner would pay beyond the incumbent subscription.
