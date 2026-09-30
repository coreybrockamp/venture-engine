# PER-014 Problem Clustering — 2026-09-29

## Decision

**ZERO_PROMOTED.** The administrative prior-authorization handoff remains an early workflow hypothesis, not a formal Problem. No `data/problems.jsonl` record was added. Scout's 16 observations come from eight independent URLs and three source types. The CFD card was not counted as evidence.

## Candidate mechanisms and independence

| Candidate mechanism | Supporting observations | Independent supporting URLs | Supporting source types | Assessment |
|---|---:|---:|---:|---|
| Documentation/portal handoff after some tool use (`OBS-000242`, `OBS-000244`, `OBS-000248`) | 3 | 3 | 2 | Concrete but heterogeneous: one CoverMyMeds attachment limit, one medication-versus-imaging channel split, and one MGMA aggregate spanning other payer tasks. Competent cross-stack recurrence is unproven. |
| Paid human/service PA handling (`OBS-000245`, `OBS-000246`, `OBS-000249`, `OBS-000251`) | 4 | 3 | 2 | Paid labor is real; these sources do not isolate a reducible administrative handoff after competent adoption or a separate payer for a new solution. |
| Epic ePA stall (`OBS-000253`) | 1 | 1 | 1 | New-build/transmission failure, contradicted by normal Epic use in the same discussion (`OBS-000254`). **SOURCE DIVERSITY GAP.** |

The counts above measure *supporting* observations only. Several findings share one discussion URL and are not independent confirmations. Industry reports aggregate PA with eligibility, claims, appeals, clinical work, and payer review; they do not identify a specific post-adoption stack. Confidence in the cross-stack mechanism is therefore low despite three nominal URLs.

## Falsification and boundary

- [A small Athena practice](https://www.reddit.com/r/FamilyMedicine/comments/1vgj307/prior_auths_make_me_want_to_pull_my_hair_out/) reports most PA handled through its existing service (`OBS-000252`); [the athenahealth/Availity/Humana case](https://www.athenahealth.com/sites/default/files/media_docs/Points-of-Light-2024-Case-Study-16.pdf) reports substantial manual-work reduction after integration (`OBS-000255`). The latter is vendor-selected, not universal proof, but shows the putative handoff can be absorbed.
- The [Epic discussion](https://www.reddit.com/r/EpicEMR/comments/1pq85bj/epic_electronic_prior_authorizations_for/) explicitly attributes the stall to a recent, broken deployment; other users report routine successful ePA operation (`OBS-000253`–`OBS-000254`).
- [CoverMyMeds' documented workflow](https://www.covermymeds.health/articles/provider-insights/quick-guide-to-covermymeds-prior-authorization-requests) includes electronic submission and status support (`OBS-000256`), even though one MA reports an attachment workaround (`OBS-000242`).
- Clinical rationale, treatment choice, medical necessity, payer decisions, and policy-mandated reviews were not converted into an administrative software problem. Paid staff time and broad PA burden were not treated as proof of a separately purchasable residual job.

## What reproduced and what did not

**FACT:** Independent Scout sources reproduced portal/channel fragmentation, manual document packaging in one CoverMyMeds workflow, dedicated labor, and mixed ePA availability. **HYPOTHESIS NOT ESTABLISHED:** The same specific administrative transfer persists after *competent* adoption across materially different EHR/ePA stacks. Epic evidence is configuration-specific; the strongest document-assembly example is product-specific; broad surveys lack implementation detail. **UNKNOWN:** Administrative minutes attributable to the narrow handoff, avoidable share, and separate buyer willingness to pay.

## Stop and next decision

No Market Analysis transition is authorized for PER-014 in this pilot. Preserve the 16 observations and this zero-promotion decision for human review. Targeted additional evidence would require separate authorization; it should seek first-person PA operators across multiple mature stacks, isolate the non-clinical handoff, and document incumbent/process adequacy. Do not infer a Problem from the approved CFD candidate or begin any downstream stage.
