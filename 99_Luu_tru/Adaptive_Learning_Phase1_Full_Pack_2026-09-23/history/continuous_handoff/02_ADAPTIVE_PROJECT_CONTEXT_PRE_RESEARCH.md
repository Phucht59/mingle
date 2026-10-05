# Condensed Context — Adaptive Language Learning Project

## Project
Adaptive Language Learning & Early Intervention Platform, evolved from Trần Hoàng Phúc's graduation-thesis work into a real product/startup-style system.

## Current status
- Architecture/contract baseline: V3.2
- V3.2 is the source of truth for implementation
- 115 contract checks passed
- 22 SQL checks passed
- Baseline assessed around 9/10
- Phase 0 — Architecture & Contract Baseline: DONE
- Phase 1 — Implementation Foundation / Product Build Kickoff: ACTIVE

## Frozen stack / architecture
- Flutter learner client, Android-first
- Flutter Web for staff/admin
- FastAPI / Python backend
- PostgreSQL
- Object Storage
- Modular monolith
- API process + durable worker process, same codebase
- Server authoritative for scoring, progress, permissions, canonical state
- Command channel separate from telemetry
- Offline durable command queue + telemetry queue
- Published content immutable/versioned
- Enrollment/attempt pin exact revisions
- Analytics uses event time + knowledge/availability time + source capture
- Mastery != Risk
- Risk is an optional input to recommendation
- Prediction / Recommendation Decision / Exposure / Execution / Outcome are separate layers
- Product must still work if ML/recommendation is disabled
- No Kafka/Kubernetes/microservices/warehouse/external feature store without a measured requirement

## Product direction
Target users include:
- English beginners / people who lost their foundation
- people who study but feel ineffective
- learners who need systematic vocabulary review
- learners who do not know what to study or review next

Internal proficiency progression:
A0 → A1 → A2 → B1 → B2

External goals such as TOEIC may map onto the learner profile, but should not replace internal progression.

MVP learning scope:
1. Vocabulary
2. Grammar
3. Listening

Speaking / unrestricted AI conversation are deferred.

Commercialization:
- development/pilot free-first
- future Free / Premium path should remain possible

Pilot:
- approximately 5 users due limited resources
- intended for usability, product behavior, technical validation and qualitative insight
- NOT enough to claim learning efficacy

## Learning experience direction
Core concept: Adaptive Learning Feed

Default consumption unit:
- ~5 minutes
- this is a UX / consumer-behavior constraint, not a claim that 5 minutes is pedagogically optimal
- session is finite and objective-bounded
- no infinite scrolling
- user may explicitly continue after completing a cycle

Five functional roles in a cycle:
1. Review
2. Learn
3. Retrieve
4. Transfer
5. Check

Modern content-consumption mechanics may be used for:
- fast start
- short interactions
- varied modality
- immediate feedback
- smooth continuation
- relevance/personalization

But pedagogy must be controlled by:
- curriculum
- prerequisites
- retrieval practice
- spacing
- feedback
- difficulty progression
- transfer
- delayed reassessment

Accepted principles:
- attempt-first when appropriate, but not dogmatically
- skip is allowed as an explicit learner action and logged as evidence
- skip is not mastery
- curriculum controls what is valid to learn next
- recommendation/ML cannot bypass prerequisites arbitrarily
- adaptive MVP is roughly "level 1.5": stable curriculum/prerequisites + personalized review/remediation/session composition, not unrestricted ML path reordering
- scheduler should be deterministic/rule-based and explainable first; ML can replace parts later
- suggested selection reasons include: DUE_REVIEW, RECENT_ERROR, PREREQUISITE_GAP, CURRENT_OBJECTIVE, MODALITY_TRANSFER, CHALLENGE
- every selected learning item should ideally have an auditable reason

## Engagement
Potential mechanics:
- streak
- daily target
- rewards

But:
- learning evidence must be separate from engagement metrics
- streak/XP must not equal mastery
- gamification supports consistency, not learning validity

## Content
Initial strategy:
- use OER / open-license material and properly licensed sources
- publicly accessible != legally reusable
- preserve source/license/provenance/content version
- content attempts must remain traceable to exact content revision

## Scientific/product philosophy
The product should feel like a learning companion:
- learns with the learner
- understands current ability over time
- notices weaknesses/forgetting
- selects suitable review/support
- adapts without hiding logic behind an opaque "AI" score

Key distinction:
- Consumer layer decides HOW learning is experienced
- Learning layer decides WHAT/WHEN/WHY content is shown

The current Phase 1 task is to scientifically resolve the Learner Evidence Model and associated interaction policies before freezing the Product Charter/MVP PRD.
