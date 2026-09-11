# MUD Historical Recall Backtest

## Method and firewall

This retrospective simulation replays the approved nine-condition MUD gate against the fixed CFD-calibration portfolio and fixed cutoffs. Only evidence labeled `PRE_CUTOFF_DIRECT` or `PRE_CUTOFF_INDIRECT` affects a decision. Later launch success, funding, adoption, valuation, and shutdown evidence is labeled and excluded. This is non-canonical; it creates no live MUD candidate, persona, observation, or downstream authority.

## Case comparison

| Case | Opportunity class | CFD result | MUD result | Channel that should catch it |
|---|---|---|---|---|
| Expensify | Expense-report workflow residual | HOLD | REJECT | CFD_NATIVE |
| Bill.com | AP workflow residual | REJECT | REJECT | CFD_NATIVE |
| Zapier | Cross-app automation/access | HOLD | HOLD | BOTH |
| Procore | Construction coordination residual | REJECT | REJECT | CFD_NATIVE |
| Shopify | Merchant e-commerce access | REJECT | HOLD | MUD_NATIVE |
| Square | Micro-merchant card-acceptance access | REJECT | HOLD | MUD_NATIVE |
| Airtable | Nontechnical structured-data access | HOLD | HOLD | MUD_NATIVE |
| Homejoy | Fragmented home-service market control | REJECT | REJECT | NEITHER/OTHER |

The simulation cards provide case-level persona/outcome/barrier, gate replay, source ledger, falsification, and excluded hindsight. The most important special-focus finding is narrow: Shopify and Square are credible MUD-shaped hypotheses, but the fixed early public corpus does not satisfy the full authorization bar.

## Metrics

Among seven historical positives: `AUTHORIZE_SCOUT` **0/7 (0%)**; `HOLD` **4/7 (57.1%)**; `REJECT` **3/7 (42.9%)**. MUD-native/BOTH positives are Zapier, Shopify, Square, and Airtable: `AUTHORIZE_SCOUT` **0/4 (0%)**. Recorded CFD decisions also authorized **0/7**, so combined historical authorization coverage is **0/7**.

This is not evidence that no historical case deserved investigation. It says the current MUD gate, when literally applied to the retained pre-cutoff public record, did not have sufficient auditable evidence to spend Scout resources. MUD adds complementary **recognition**—three MUD-native cases moved from CFD `REJECT` to MUD `HOLD`—but not authorization recall in this small historical corpus.

## Control and negative probes

Homejoy is `REJECT`: the pre-cutoff corpus does not establish an unlockable access barrier rather than service-supply/quality execution.

| Negative probe (not a portfolio case) | MUD result | Reason |
|---|---|---|
| Technology-first excitement: “AI can build a personal business adviser,” with no attributable desired outcome or attempts | REJECT | Fails demand chain, consequence, buyer, barrier, and falsification. |
| Low-value convenience: a cosmetic one-click shortcut for an already adequate free workflow | REJECT | Fails meaningful consequence, barrier causality, and incumbent falsification. |
| Aspirational claim: “people would love personal drone delivery,” with no paid substitute, repeated attempt, or avoided consequence | REJECT | Fails observed behavior, latent demand, and economic plausibility. |

All three probes reject. No control/probe generated a `HOLD` or `AUTHORIZE_SCOUT`; the backtest therefore found no obvious idea-generator false positive.

## False negatives and public-evidence limitation

The missed MUD-native/BOTH cases are `HOLD`, not substantive rejection. Shopify failed source breadth, two independent causal chains, and barrier generalization. Square passed breadth and had one lost-sale chain, but lacked a second attributable merchant chain and generalization. Airtable was concentrated in one community and did not establish consequence or buyer evidence. Zapier lacked a second nontechnical access chain and generalization.

The dominant limitation is public observability: early customer acquisition, buyer roles, and economic consequences are rarely documented in durable independent sources. This differs from a finding that MUD’s conceptual model is wrong. It is not yet a basis to relax any gate: the same missing evidence is what protects Scout from speculative promotion.

## Interpretation

**Does MUD complement CFD?** Yes at hypothesis classification: it recognizes Shopify, Square, and Airtable as access-barrier cases instead of treating them as failed residual-work candidates. **Does it improve historical authorization coverage?** No, not in this retained source corpus. **Does it duplicate CFD?** No; Expensify, Bill.com, and Procore remain CFD-native. **Does it introduce obvious false positives?** No; the control and all negative probes reject.

## Conclusion

`MUD_BACKTEST_INDETERMINATE`

The evidence is strong enough to show a complementary conceptual lens and false-positive resistance, but too weak to establish authorization-level recall. The backtest cannot responsibly support implementation as designed, gate relaxation, or abandonment.

## Recommendation and one next action

`EXPAND_CALIBRATION_BEFORE_DECIDING`

Conduct a separately authorized expanded historical calibration using later-era, pre-success cases with independently attributable public user evidence and pre-registered controls. Do not implement, pilot, or run MUD first.
