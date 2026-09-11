# Final Targeted MUD Public-Web Validation

## Scope and immutable exit rule

This is the final planned public-web calibration. It applies the committed Gate 6/8/9 refinement to Warby Parker, Dropbox, Kiva, and Juicero without changing cutoffs, prior outcomes, labels, or the MUD gate. The exit rule is fixed: proceed only if at least one close positive reaches `AUTHORIZE_SCOUT`, Juicero remains `REJECT`, and no requirement is waived. Otherwise stop public-web calibration.

## Replay results

| Case | Original | Refined replay | Gate 6 | Gate 8 | Gate 9 | Dominant gap |
|---|---|---|---|---|---|---|
| Warby Parker | HOLD | HOLD | PASS | FAIL | FAIL | enabler observability; alternative adequacy mixed |
| Dropbox | HOLD | HOLD | FAIL | FAIL | FAIL | payer/enabler observability; alternative adequacy mixed |
| Kiva | HOLD | REJECT | FAIL | PARTIAL | FAIL | regulated intermediary/risk is substantive |
| Juicero control | REJECT | REJECT | PASS | FAIL | FAIL | no access barrier; substitutes adequate |

No positive reached `AUTHORIZE_SCOUT`; Juicero remained `REJECT`; no gate changed. **The exit rule failed.**

## Gate 6 / 8 / 9 recovery

Warby Parker recovered a grounded consumer payer through contemporaneous direct purchase/price evidence but lacked an independent authoritative explanation for a barrier-specific economic change. Dropbox recovered published paid-plan availability but not payment behavior or authority; broadband context remained adjacent rather than causal. Both had accessible alternatives, but the bounded record could not establish either full adequacy or inadequacy. Kiva’s more complete actor map revealed a substantive underwriting/intermediation constraint. Juicero confirms the refined module still rejects a convenience claim when ordinary alternatives serve the outcome.

## Observability versus substantive gaps

- **Warby Parker:** Gate 8 `OBSERVABILITY_GAP`; Gate 9 `MIXED_GAP`; `OBSERVABILITY_HOLD` metadata.
- **Dropbox:** Gates 6/8 `OBSERVABILITY_GAP`; Gate 9 `MIXED_GAP`; `OBSERVABILITY_HOLD` metadata.
- **Kiva:** Gate 6/8 `MIXED_GAP`; Gate 9 `SUBSTANTIVE_GAP`.
- **Juicero:** Gates 3–5, 7–9 are substantive failures; control rejection is preserved.

## Research economics

`NOT_ECONOMICAL`

The first backtest, expanded calibration, five-case source validation, and this authorization-proximity mini-pass recovered some evidence but no authorization-grade positive. Routine discovery would repeatedly require deep source-family pivots and late-stage counter-searches while still leaving buyer/payer, authoritative enabler, and alternative-adequacy roles unresolved. Continuing public-web calibration is not proportionate to the observed yield.

## Final validation result and recommendation

`MUD_PUBLIC_WEB_VALIDATION_FAIL`

`PAUSE_MUD_PUBLIC_WEB_IMPLEMENTATION`

This does not show that MUD’s conceptual gate is wrong or that MUD itself failed. It shows that, under the current evidence model and bounded public-web economics, implementation is not justified. Do not automatically propose another historical calibration.

## One proposed next action

Review this final MUD public-web validation and formally record the pause of MUD public-web implementation. Do not implement MUD, run live MUD discovery, or initiate additional MUD calibration without separate authorization.
