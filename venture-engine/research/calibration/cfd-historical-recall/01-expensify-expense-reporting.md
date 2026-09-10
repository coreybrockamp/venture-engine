# Simulation 01 — Expensify expense reporting

**Historical-positive class:** strong operational-workflow positive  
**Founding / initial product period:** 2008  
**Cutoff:** 2009-12-15 (before the paid 1.0 announcement on 2009-12-16)  
**Simulated decision:** `HOLD`  
**Confidence:** medium

## Persona and workflow

**Persona:** employee, contractor, or small-business bookkeeper handling reimbursable card expenses. **Workflow:** capture receipts, categorize charges, prepare a report, route it to reimbursement/accounting, and reconcile it.

## Pre-cutoff evidence ledger

| Classification | Source | Evidence / limit |
|---|---|---|
| PRE_CUTOFF_DIRECT | [TechCrunch, 2008-09-16](https://techcrunch.com/2008/09/16/expensify-the-corporate-card-for-the-rest-of-us/) | Paper receipts and Excel spreadsheets were described as small-business alternatives; launch reporting, not an independent buyer account. |
| PRE_CUTOFF_DIRECT | [TechCrunch, 2009-03-11](https://techcrunch.com/2009/03/11/expensifys-free-expense-report-system-takes-the-hassle-out-of-reimbursements/) | Existing cards, reimbursement contacts, Concur, and Shoeboxed establish paid-stack context; same publication type. |
| UNUSABLE_HINDSIGHT | [TechCrunch, 2009-12-16](https://techcrunch.com/2009/12/16/expensify-expense-reports/) | Excluded from decision because it follows the cutoff. |

## Incumbents, actors, and falsification

**FACT:** Observable alternatives were paper receipts, Excel, regular credit cards, bookkeepers, Concur, and Shoeboxed. User: submitter; workflow owner: finance/bookkeeper; buyer/payer: SMB owner or finance owner. Buyer evidence is **plausible**, not attributable. The record shows a cumbersome job, but not two accounts with the same residual burden after competent incumbent adoption; smaller firms may instead have lacked an incumbent.

## Gate replay

| 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|
| PASS | FAIL — two trade-press URLs | FAIL — no post-adoption accounts | PASS — cards/bookkeeping/paid competitors | PARTIAL | UNKNOWN | FAIL — no Path A/B |

## Hindsight firewall and outcome

Excluded: paid launch/pricing and all later adoption, revenue, funding, and market-position information. **POST_CUTOFF_OUTCOME_ONLY:** Expensify later became commercially significant. That does not upgrade `HOLD`.
