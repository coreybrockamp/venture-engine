# Historical Recall Calibration of `manual-pilot-v2`

## Scope and method

This is a retrospective, non-canonical backtest. It uses only source material labeled `PRE_CUTOFF_DIRECT` or `PRE_CUTOFF_INDIRECT` for the simulated decision; later evidence validates chronology/outcome only. No live CFD card, canonical entity, gate, threshold, controller, or downstream pipeline state was used or changed. Cases were selected for operational-workflow variety—not user context—and before individual review: five strong commercial positives, two harder positives, and one failed control.

The threshold replay is literal. `AUTHORIZE_SCOUT` requires every v2 condition, including three independent URLs across two types, two attributable post-adoption signals, paid linkage, buyer/payer evidence, absorption, and Path A or B structural generalization. A missing historical public record is recorded as missing; it is not filled with later company success.

## Portfolio

| Case | Category | Class | Cutoff | Selection rationale | Simulated result |
|---|---|---|---|---|---|
| Expensify | SMB expense reporting | strong positive | 2009-12-15 | Recurring finance workflow; cards, bookkeeping, and incumbent expense tools | HOLD |
| Bill.com | SMB accounts payable | strong positive | 2010-06-30 | Paid finance labor plus invoice/approval/payment handoff | REJECT |
| Zapier | app-to-app automation | strong positive | 2012-08-01 | Cross-system manual bridge across paid business apps | HOLD |
| Procore | construction document control | strong positive | 2010-06-08 | Vertical multi-party RFI/submittal coordination | REJECT |
| Shopify | SMB storefront creation | strong positive | 2007-10-20 | Paid web-development/incumbent-displacement workflow | REJECT |
| Square | micro-merchant card acceptance | harder positive | 2010-06-01 | New access/technology category rather than incumbent residual | REJECT |
| Airtable | spreadsheet/database collaboration | harder positive | 2015-03-26 | Spreadsheet-layer workflow with early public operator discussion | HOLD |
| Homejoy | on-demand cleaning | control | 2013-12-04 | Paid service category that did not produce a durable standalone outcome | REJECT |

## Simulated results and gate causes

| Case | Persona / narrow workflow | Failed or incomplete gates | Key usable evidence | Key falsification | Excluded hindsight |
|---|---|---|---|---|---|
| Expensify | submitter/bookkeeper; receipt-to-reimbursement report | 2, 3, 5 partial, 6 unknown, 7 | paper/Excel and cards/bookkeeping context | may be no-incumbent access problem | paid 1.0, later scale/funding |
| Bill.com | controller/bookkeeper; bill-to-payment reconciliation | 2, 3, 4 partial, 6, 7 | manual-check documentation | controls/approval are ordinary accounting | all later company proof |
| Zapier | operator/developer; app event handoff | 3 partial, 4 partial, 5 partial, 6 unknown, 7 | public launch, HN user integration, 60-app/developer-time report | APIs/custom integration could absorb it | later adoption/scale |
| Procore | GC PM; RFI/submittal/document routing | 2, 3, 4 partial, 5 partial, 6 unknown, 7 | pre-cutoff product announcement | contracts/process/configuration may absorb | later customers/IPO |
| Shopify | merchant; create/manage storefront | 2, 3, 4 partial, 6, 7 | hosted-vs-custom e-commerce availability | category access, not post-adoption residual | later merchant/pricing/ecosystem proof |
| Square | micro-merchant; accept a card | 2, 3, 4 partial, 6, 7 | early card-reader demonstration | new-payment access/underwriting category | later demand/volume |
| Airtable | team owner; structured shared records | 2, 3, 4 partial, 5 weak, 6 unknown, 7 | HN evidence of Sheets fragility and Airtable structure | concentrated community evidence; no paid residual account | later adoption/valuation |
| Homejoy | household; arrange cleaner | 2–4, 6, 7 | none before cutoff sufficient for gate | marketplace supply/quality risk | early scale/funding/shutdown |

Full source ledgers, actor maps, incumbent reconstruction, and hindsight exclusions are in the eight simulation cards in this directory. Source labels in those cards intentionally distinguish direct evidence from indirect context.

## Recall metrics

There are seven historical positives. `AUTHORIZE_SCOUT`: **0/7 (0%)**. `HOLD`: **3/7 (42.9%)**. `REJECT`: **4/7 (57.1%)**. The control received `REJECT`, so the exercise does not show indiscriminate promotion. The near-miss rate is 3/7: Expensify, Zapier, and Airtable had identifiable workflows but lacked one or more evidence conditions.

This is not a statistical estimate: the sample is small, archival public evidence is uneven, and several cases predate modern public operator communities. It is nevertheless a useful falsification result: a literal residual-post-adoption CFD gate would not have authorized Scout for these known later successes based on the reconstructed record.

## False-negative analysis

| Blocking dimension | Positive cases affected | Interpretation |
|---|---:|---|
| Evidence breadth/source types | 6 | Historical public material often consists of launch coverage or a single community, not independent practitioner accounts. |
| Two attributable post-adoption signals | 7 | The dominant blocker. Several successes solved first-adoption, access, or broad workflow problems rather than an observed residual after incumbent use. |
| Paid linkage specific to mechanism | 5 | Paid category context existed more often than mechanism-specific labor/cost proof. |
| Buyer/payer evidence | 6 | Early public sources rarely name the actual economic decision maker. |
| Absorption check | 5 | Custom development, normal controls, contracts, or traditional providers remained plausible. |
| Structural generalization | 7 | Early evidence did not establish Path A/B; in several cases the required cross-implementation record only became publicly visible later. |

The most important separation is causal: Bill.com and Procore are chiefly **public-evidence/reconstruction insufficiency**; Shopify and Square are principally **category-creation/access** cases; Expensify, Zapier, and Airtable are **detected but incomplete** `HOLD`s. A `REJECT` therefore does not always mean the gate mistakenly judged an observable residual job to be false.

## Post-adoption, structural, and public-evidence bias

**Post-adoption bias:** yes. Shopify and Square would correctly sit outside a residual-paid-friction detector because their early value was access/displacement/new capability. That is a systematic blind spot only if the engine expects CFD to find category-creation opportunities; it is not a defect in a narrowly scoped residual-friction gate.

**Structural-generalization:** the v2 test correctly prevents one-stack anecdotes from becoming live Scout work. The calibration does not show that it rejected a well-observed, cross-stack historical residual; it shows that early public records rarely supplied the needed proof. It should therefore not be weakened on this test set.

**Public-evidence bias:** material. Pre-cutoff procurement, labor, and buyer information was private or absent from durable public communities for Bill.com and Procore. The recurring lack of source diversity and attributable post-adoption accounts is an observability limit, not evidence that every historical workflow was adequately absorbed.

## Comparison with live CFD

Live `manual-pilot-v2` rejections have commonly failed because the available mechanism was implementation-specific, ordinary process, professional judgment, or did not structurally generalize. The historical replay produces many of the same terminal failures, but with a different root cause in several cases: early-source scarcity and category type. This supports the current system’s precision behavior while warning that a run of live `REJECT`s cannot by itself establish that the real discovery universe lacks opportunities.

## Calibration conclusion and proposal

**Conclusion:** current CFD appears **high precision / low recall for the broader opportunity universe**, while its calibration for the narrower residual-paid-friction universe remains indeterminate. The portfolio contains no evidence that the v2 gate should be relaxed; it does show that v2 alone will systematically miss category-creation and poorly publicized early workflow opportunities.

**Recommendation:** `ADD_SECOND_DISCOVERY_CHANNEL`.

The proposed complementary channel should be designed and reviewed separately for category-creation, access, or technology-shift opportunities. It must have its own anti-hindsight controls and must not promote a persona, alter `manual-pilot-v2`, or substitute for canonical Scout evidence. This is a proposal only.

## One proposed next step

Review this calibration and explicitly decide whether to authorize design of a separate, bounded discovery-channel proposal; otherwise continue existing CFD unchanged. Do not change a gate or begin live discovery from this report.
