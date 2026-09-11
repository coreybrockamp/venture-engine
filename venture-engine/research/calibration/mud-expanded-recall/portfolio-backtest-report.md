# Expanded MUD Historical Calibration Report

## Method, scope, and decision lock

This expanded calibration replays the unchanged nine-condition MUD gate over the separately frozen 13-case portfolio. It is retrospective and non-canonical. Only pre-cutoff evidence in the cards affects official decisions; later outcomes are excluded. The official decisions were locked before the sensitivity calculation. No CFD replay was run for new cases because this is a MUD-only diagnostic; previously recorded CFD results remain historical.

## Portfolio and decisions

| Positive case | Primary class | Richness | Official result | Principal reason |
|---|---|---:|---|---|
| Warby Parker | access/affordability | MEDIUM | HOLD | public source breadth, two chains, and generalization unavailable |
| Kiva | access/minimum scale | MEDIUM | HOLD | same public-evidence gaps; finance/intermediation falsification mixed |
| Kickstarter | access/business-model mismatch | HIGH | AUTHORIZE_SCOUT | three attributable sources, repeated pledge behavior, broad project contexts |
| Wix | complexity/expertise | MEDIUM | HOLD | early record does not independently document users’ causal chains |
| Codecademy | complexity/expertise | HIGH | AUTHORIZE_SCOUT | public sign-up behavior, independent reporting, credible instructional enabler |
| Twilio | complexity/expertise | HIGH | AUTHORIZE_SCOUT | manual-labor and multi-organization implementation chains |
| Canva | complexity/expertise | MEDIUM | HOLD | source breadth/two chains/generalization absent from early public record |
| Dropbox | new feasibility/capability | MEDIUM | HOLD | direct product framing but insufficient independent behavioral chains |
| Netflix streaming | ambiguous/boundary | LOW | REJECT | convenience/format shift, not a demonstrated access barrier |
| Slack | ambiguous/boundary | LOW | REJECT | workflow improvement, not a demonstrated excluded outcome |

### Recall

- **Overall positives:** `AUTHORIZE_SCOUT` **3/10 (30.0%)**; `HOLD` **5/10 (50.0%)**; `REJECT` **2/10 (20.0%)**.
- **MUD-native/BOTH:** eight cases (Warby Parker, Kiva, Kickstarter, Wix, Codecademy, Twilio, Canva, Dropbox): **3/8 (37.5%) AUTHORIZE_SCOUT**, **5/8 (62.5%) HOLD**, **0/8 REJECT**.
- **HIGH-richness subset:** Kickstarter, Codecademy, and Twilio: **3/3 (100.0%) AUTHORIZE_SCOUT**, **0 HOLD**, **0 REJECT**.

## Control behavior and false-positive resistance

| Control | Risk tested | Result | Why |
|---|---|---|---|
| Google Glass | technology-first | REJECT | no evidenced recurring blocked valuable outcome or payer chain |
| Color | aspirational demand | REJECT | attention/funding do not supply desire-attempt-consequence behavior |
| Juicero | convenience/segmentation | REJECT | conventional juicers/prepared juice already cover the outcome |

Controls were **3/3 REJECT**; no simulated false-positive authorization or HOLD occurred.

## Gate-blocker frequency — positives only

Counts identify a condition that prevented authorization in at least one positive case. Classification counts are condition-level, not case-level; a case can contribute to several blockers.

| Gate condition | Blocked cases | SUBSTANTIVE_FAIL | OBSERVABILITY_FAIL | MIXED |
|---|---:|---:|---:|---:|
| 1. Narrow persona/outcome/barrier | 2 | 2 | 0 | 0 |
| 2. Three URLs/two source types | 7 | 0 | 7 | 0 |
| 3. Two independent causal chains | 7 | 0 | 7 | 0 |
| 4. Meaningful effort/cost/consequence | 2 | 0 | 0 | 2 |
| 5. Barrier rather than weak desire | 2 | 2 | 0 | 0 |
| 6. User/beneficiary and buyer/payer | 0 | 0 | 0 | 0 |
| 7. Barrier generalization/vendor independence | 7 | 2 | 5 | 0 |
| 8. Credible mechanism enabler | 0 | 0 | 0 | 0 |
| 9. Falsification passes | 7 | 2 | 0 | 5 |

**Diagnostic:** observable-source failures are the most common blockers (19 condition-level failures across 2, 3, and the observability portion of 7), versus 8 substantive and 8 mixed failures. The HIGH cases all passed; five of the eight MUD-native/BOTH cases held principally because early public sources cannot establish breadth, two independent causal chains, or generalization. The two boundary successes rejected for substantive fit reasons. This is evidence that source observability—not a demonstrated philosophical error in the gate—is dominant, while falsification remains legitimately mixed for several access cases.

## Sensitivity analysis — diagnostic only

Counterfactual: treat only condition 2 (source breadth) and condition 3 (second independent causal chain) as evidence-confidence flags, without changing any other condition. **Canva and Dropbox** would move from `HOLD` to **provisional** authorization: **2/10 positives**. Warby Parker, Kiva, and Wix remain `HOLD` because condition 7 and/or 9 still fails or is mixed. Netflix streaming and Slack remain `REJECT` for substantive reasons.

This does not modify an official result, gate, policy, or recommendation. It shows that merely relaxing evidence breadth would not convert most unresolved cases and would weaken the audit protection that prevents speculative promotion.

## Comparison with initial calibration

The initial calibration produced **0/7 AUTHORIZE_SCOUT**, **4/7 HOLD**, **3/7 REJECT**, with **0/4** MUD-native/BOTH authorizations. This deliberately evidence-richer portfolio produced **3/10 AUTHORIZE_SCOUT**, **5/10 HOLD**, **2/10 REJECT**, and **3/8 (37.5%)** MUD-native/BOTH authorization. In the pre-registered HIGH subset, authorization was **3/3**. Controls remained **3/3 REJECT**.

Recall therefore improved materially when comparatively rich contemporaneous evidence was available. The same early-public-record limitations still block most otherwise plausible MUD cases, and the controls remain filtered. The evidence supports neither gate relaxation nor a live implementation decision.

## Conclusion and recommendation

`MUD_SOURCE_MODEL_NEEDS_REFINEMENT`

`REFINE_MUD_SOURCE_STRATEGY`

The frozen gate distinguishes three evidence-rich MUD-shaped cases from three plausible controls and authorizes meaningful historical coverage without a relaxed rule. Its limiting factor is the discoverability and corroboration model required to find durable contemporary source breadth and two independent causal chains—not demonstrated systematic substantive false negatives. Before any implementation, separately design and review a bounded source strategy that can obtain attributable multi-source pre-Scout evidence while preserving the current gate. Do not implement, pilot, or run MUD from this calibration.
