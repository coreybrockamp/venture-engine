# Outpatient Referral-Operations Manager

## Persona ID

`PER-013` — stable; never reassign.

## Definition

Administrative owner at a multi-site outpatient provider organization responsible for tracking externally sent referrals through completion and capturing returned status or records across organizational and EHR boundaries. Excludes generic healthcare administration, clinical triage or diagnosis, payer-authorization judgment, patient-care decision-making, and general EHR interoperability outside this narrow referral-loop workflow.

## Core Context

**HYPOTHESIS:** A referral that leaves the originating organization may need ongoing administrative status and record follow-up before the originating provider can close its local referral record.

## Trigger Events

**HYPOTHESIS:** An external referral is sent; an appointment is not confirmed; a patient does not proceed; an outside office rejects or cannot schedule the referral; a consult result is missing; or the originating workqueue shows an aged referral.

## Candidate Jobs to Be Done

**HYPOTHESIS:** When a patient is referred outside the organization, maintain a reliable administrative record of the referral's disposition and returned documentation without conflating that work with clinical, authorization, or patient-choice decisions.

## Existing Spending Categories

**HYPOTHESIS:** EHR/practice-management systems, referral-management tools, interoperability/direct-messaging services, document/fax capture, patient engagement/scheduling tools, centralized referral operations, and referral-coordinator labor.

## Likely Information Sources

**HYPOTHESIS:** referral-operations practitioner communities, EHR user communities, public health-system workflow materials, employer job descriptions, public implementation/case materials, referral-management product reviews, and health-administration sources with attributable operator evidence.

## Research Search Themes

- "external referral loop closure coordinator EHR"
- "external specialist referral missing consult report workqueue"
- "Epic referral coordinator external referrals follow up"
- "eClinicalWorks referral tracking external records"
- "referral management platform coordinator workflow external providers"

## Candidate Problem Domains

**HYPOTHESIS:** external referral status visibility; returned-record capture; referral aging and closure; cross-organization referral handoff; referral-workqueue exception ownership.

## Possible Existing Solution Types

**HYPOTHESIS:** EHR referral modules/workqueues, referral-management platforms, interoperability and direct-messaging networks, centralized referral hubs, automated fax/OCR/document capture, patient-engagement scheduling, workflow redesign, and external-provider agreements.

## Research Risks and Biases

Do not treat clinical triage, specialist selection, payer authorization, patient refusal/nonattendance, necessary relationship work, a one-time interface failure, missing configuration, or generic EHR dissatisfaction as evidence of a structural administrative residual. Distinguish actual external-boundary status/documentation work from ordinary care coordination and from incumbent capability claims.

## Exclusion Criteria

Exclude: clinical judgment, authorization/coverage decisions, patient adherence as a standalone issue, internal-only referrals that remain within one shared system, generic EHR workflow complaints, initial implementation/migration, and product-specific defects without recurring external-loop evidence.

## Current Evidence State

**PARTIAL**

- Observation count: 21
- Problem count: 0
- Opportunity count: 0
- Last researched date: 2026-09-09

## Open Research Questions

- Does external-loop administrative work persist after competent use of referral modules, interoperability networks, and dedicated referral-management platforms?
- Which coordinator tasks are structural status/documentation bridging versus necessary clinical, payer, patient-choice, or relationship work?
- How frequently do external referrals remain open, and what attributable administrative labor or commercial consequence results?
- Who selects, funds, and would separately pay for any change beyond current EHR, referral, and operating-process coverage?

## Last Updated

2026-09-09T02:10:00Z
