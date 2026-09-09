# Commercial Friction Discovery Candidate Card

**Date:** `2026-09-09`

**CFD version:** `manual-pilot-v2`

**Decision:** `REJECT`

## Candidate

- **Candidate persona:** IT identity-lifecycle or onboarding operations manager at a Workday/Okta organization.
- **Existing persona ID, if any:** None; no persona is created by this card.
- **Narrow workflow:** Resolving new-hire, offboarding, username, role, and exception cases that fall outside HRIS-to-identity-provider automation.
- **Trigger/context:** Public IT/identity practitioners describe Workday, Okta, Microsoft 365, and ServiceNow implementations with manual remediation or exception steps.
- **Operational mechanism:** Human intervention when source-of-truth data, timing, unique identifiers, or HR/legal exception policy conflicts with automated lifecycle rules.

## Commercial-friction evidence

- **Paid incumbent or paid labor already present:** FACT — practitioner accounts describe Workday, Okta, Microsoft 365, and ServiceNow; official documentation describes licensed HR/identity/provisioning products.
- **Existing workaround:** FACT — accounts describe manual remediation, custom hooks/field mappings, trigger forms/checklists, or alternative provisioning configurations.
- **Economic consequence or labor burden:** FACT — manual exceptions are described, but no independently verified recurring labor cost, loss, or separate willingness-to-pay evidence was found.
- **Post-adoption friction summary:** FACT — the public accounts concern collision, timing, source-of-truth, and exception-policy behavior after or during implementation.

| Source type | Direct source link | Attributable evidence | Post-adoption mechanism | Paid/labor or economic link | Notes / limitations |
|---|---|---|---|---|---|
| Public practitioner discussion | [r/okta: provisioning existing UPNs](https://www.reddit.com/r/okta/comments/1qv1j2t/how_are_people_handling_okta_provisioning_for/) | A Workday → Okta → Microsoft 365 user asks whether existing UPNs require manual remediation. | Username collision / provisioning failure. | Paid HRIS/identity/productivity stack. | Replies identify templates, hooks, and iterative automation. |
| Public practitioner discussion | [r/workday: IT offboarding triggers](https://www.reddit.com/r/workday/comments/1k04as7) | Practitioners describe HR/legal/manager holds and manual exception tracking around offboarding automation. | Exception policy and timing handling. | Paid Workday/Okta/ServiceNow or related stack. | Includes necessary human and policy judgment; not a general software gap. |
| Public practitioner discussion | [r/ITManagers: employee onboarding](https://www.reddit.com/r/ITManagers/comments/1sg3tc9/what_are_people_using_for_employee_onboarding_in/) | An organization using Okta Workflows and ServiceNow says setup was difficult but automation works reasonably; the thread recommends one intake, clear owners, and escalation. | Configuration and operational ownership. | Paid identity/ticketing tools plus IT labor. | One thread; some replies are vendor-adjacent. |
| Incumbent documentation | [Okta Workday provisioning](https://help.okta.com/en-us/content/topics/provisioning/workday/workday-provisioning.htm) | Okta documents automated lifecycle propagation from Workday to Okta, AD, and downstream applications. | Covers ordinary hire/update/termination flow. | Existing paid identity lifecycle platform. | Vendor documentation, retained as counterevidence. |
| Incumbent documentation | [ServiceNow new-hire integrations](https://www.servicenow.com/docs/r/employee-service-management/employee-journey-management/business-roles.html) | ServiceNow documents preconfigured Okta and Microsoft Entra onboarding integrations. | Covers onboarding provisioning flow. | Existing paid HR-service-management platform. | Vendor documentation, retained as counterevidence. |

## Actor map

| Role | Evidence-backed assessment | Unknowns |
|---|---|---|
| User | IT/identity administrator or onboarding operations worker manages exceptions. | Frequency and share of work after competent configuration. |
| Selector | HYPOTHESIS — IT/security and HRIS leadership select workflow design and vendors. | Decision authority in the cited organizations. |
| Buyer | HYPOTHESIS — employer IT/security or HR operations. | Separate budget beyond current identity/ticketing suites. |
| Payer | HYPOTHESIS — employer. | Separate willingness to pay for exception handling. |

## Quick absorption check

- **Relevant incumbent, service, free-tool, or normal-process coverage:** FACT — Okta documents automated Workday-driven lifecycle changes, and ServiceNow documents preconfigured onboarding integrations. Public practitioners name hooks, templates, provisioning groups, standard lifecycle settings, clear ownership, and escalation as remedies.
- **Could this be an isolated defect, poor implementation, clinical/professional judgment, or ordinary process issue?** YES — the cited cases are configuration, data-model, source-priority, role-policy, timing, legal/HR-hold, or security-control specific. Human handling can be necessary rather than residual avoidable work.
- **Contradictory evidence:** FACT — practitioners report that configured Workday/Okta lifecycle automation can handle normal deprovisioning and username behavior; official documentation describes the same normal-path automation.

## Source limitations

- **Independent URL count:** 5 (three practitioner URLs; two incumbent URLs).
- **Source-type count:** 2 (public practitioner discussions; incumbent documentation).
- **Concentration or access constraints:** Direct operator evidence is concentrated in Reddit; it does not quantify labor or establish a separate buyer/payment signal.
- **Persona-fit / prevalence limits:** Organization size, licensing, security policy, data quality, and implementation maturity differ substantially across accounts.

## Structural-generalization check

- **Independent organizations represented:** Three attributable practitioner accounts.
- **Distinct incumbent stacks / implementations represented:** Workday/Okta/Microsoft 365; Workday/Okta/ServiceNow; unspecified onboarding stack with Okta Workflows/ServiceNow.
- **Same operational mechanism across those contexts?:** FAIL — the accounts concern distinct edge cases (UPN collision, policy/timing holds, and implementation/ownership), not one stable residual operational job.
- **Path A — cross-implementation recurrence evidence:** FAIL — no same specific mechanism recurs across the implementations.
- **Path B — vendor-independent evidence, if cross-stack evidence is unavailable:** FAIL — the remaining work is materially tied to organization-specific identity, HR, legal, and security rules.
- **Evidence against generalization:** Normal-path automation and configured workflow/process ownership are repeatedly presented as sufficient for standard lifecycle work.
- **Structural-generalization gate result:** `FAIL`

## Promotion gate

- [x] Narrow persona plus concrete recurring workflow.
- [x] At least three independent URLs across at least two source types, where available.
- [ ] At least two attributable post-adoption signals with the same operational mechanism.
- [ ] Direct link to paid software, paid labor, contractor/consultant work, or measurable economic cost.
- [ ] Plausible user, selector, buyer, and payer hypothesis grounded in evidence.
- [ ] Quick absorption check does not plainly explain the issue as an excluded or already-solved case.
- [ ] Structural-generalization check passes through Path A or Path B.

**Product-specific handling:** The evidence is configuration and policy-specific, and structural generalization fails; `AUTHORIZE_SCOUT` is not available.

## Rationale

**FACT:** Public practitioners report manual remediation and exception handling after adoption of paid identity and HR systems.

**ESTIMATE:** None.

**ASSUMPTION:** None.

**HYPOTHESIS:** A residual lifecycle-exception job could exist only if future evidence identifies one vendor-independent recurring mechanism that remains after competent identity, ticketing, and policy design.

**Decision rationale:** `REJECT`. Current evidence explains the apparent work through implementation/configuration variance, necessary HR/legal/security judgment, and normal process ownership. It does not establish a separately payable, structurally recurring residual job. No canonical Scout resources are authorized.

## Later outcome (complete only after authorized downstream work)

- **Later outcome tag:** `NOT_YET_RUN`
- **Later rejection pattern:** `NOT_YET_RUN`
- **Linked canonical records, if independently created later:** None; this candidate was not authorized for downstream work.
