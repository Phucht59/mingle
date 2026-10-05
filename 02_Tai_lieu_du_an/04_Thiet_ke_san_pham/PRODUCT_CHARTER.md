# Product Charter — Adaptive Language Learning & Early Intervention Platform

Original working charter: 2026-09-23. Status reconciliation: 2026-10-05. Mingo is the current product name. Exact preserved V3.2 is architecture/contract authority; its compatibility mapping is completed and the unchanged suites were rerun on 2026-10-05 (115 contract and 22 SQL checks passed). This is a specification/verification baseline, not a completed product.

Product Owner approval of the current GĐ1 conclusions is recorded for 2026-10-04 in the supplied audit instruction. Approved principles may guide implementation; duration, customer segment, categories and policy thresholds remain hypotheses. Customer discovery remains **VALIDATION DEBT**. GĐ1 internal consistency closure and Phase2 human/product acceptance are separate gates. See [GĐ1 closure notes](GD1_INTERNAL_BA_CLOSURE_NOTES_20261005.md).

## Problem and audience

Adults beginning or rebuilding English foundations often encounter fragmented content, forget vocabulary and lack a reliable answer to what to study next. The first audience includes learners who study without seeing progress, need systematic vocabulary review or need guidance on their starting level. This is a product problem statement, not a measured prevalence claim.

## Promise and success

Provide a short, coherent English-learning cycle with a visible objective, meaningful retrieval and feedback, sensible review, and an understandable reason for the next suggestion. The product may say what it has observed and what evidence is missing; it must not claim validated diagnosis, mastery percentage or learning efficacy before appropriate validation. Success in the five-user pilot means an understandable experience, correct scheduler and telemetry behavior, reliable offline reconciliation, appropriate content and trust. Learning efficacy requires a later adequately designed study.

## Scope and progression

- MVP domains: Vocabulary, Grammar, Listening. Speaking, unrestricted AI conversation and broad social features are deferred.
- Internal progression: A0 (internal; Pre-A1-like) → A1 → A2 → B1 → B2. TOEIC/work goals map to learner intent and content within the legitimate path; no claim of externally certified CEFR or TOEIC score.
- Finite Adaptive Learning Feed: approximately five minutes per default cycle, one objective, Review → Learn → Retrieve → Transfer → Check as functional roles, clear closure, learner explicitly continues. Five minutes is a low-friction UX hypothesis, not a pedagogical optimum.
- Curriculum and prerequisites bound eligibility. Review uses spacing and recent performance; feedback and delayed reassessment matter more than empty completion. Learner focus is respected inside the eligible pool, with a bounded and explained prerequisite/due-review insertion.
- Both translation word cards and explicit grammar explanations can support beginners, combined with meaning/audio/context and varied retrieval. Listening replay is learning support; assessment conditions are recorded separately.

## Distinct evidence streams

| Stream | Used for | Not evidence of |
|---|---|---|
| Learning | First unaided response, assisted attempts, transfer and delayed checks by objective/modality | Psychological cause from one click |
| Engagement | Streak, cycle completion, return behavior | Mastery or proficiency |
| UX/consumer | Entry friction, clarity, audio access, preferred duration | Retention of language knowledge |
| Product hypothesis | Five-minute unit, replay count, prompt sequence, reward mechanics | Proven universal learning gain |

Show a qualitative learner profile with evidence and uncertainty. Streak/reward/target are separate from mastery and do not unlock prerequisites. Explain recommendations with auditable reason codes; do not attribute unobserved mental states.

## Delivery and architecture commitments

V3.2 remains the implementation source of truth: Flutter Android-first learner and Flutter Web staff client; FastAPI/Python, PostgreSQL, Object Storage; modular monolith with API and durable worker processes; authoritative server scoring/progress/permissions; command separate from telemetry; durable offline queues; immutable published content and exact pinned revisions; event time and availability time; mastery distinct from risk; decision, exposure, execution and outcome separate; deterministic path when intelligence or recommendation is disabled. No new distributed infrastructure without measured need.

Content requires legitimate reuse rights, source/license/provenance and editorial checks. Public access alone is not permission to reuse. Development/pilot is free-first; a future Free/Premium path remains possible without shaping learning rules around monetization.

## Decision and validation boundaries

Research 'FREEZE NOW' principles are incorporated here as working Phase 1 guardrails. 'MVP HYPOTHESIS' values are configurable, versioned and subject to pilot observation. Final mastery formula, statistical CAT/cut scores, production risk model, ranking weights, adaptive path optimizer and reward optimization remain deferred. Any demonstrated contradiction with original V3.2 requires an Implementation Issue and, if the frozen rule must change, an explicit approved Change Request.

Charter acceptance: trace the promises to the MVP PRD and preserved V3.2 compatibility matrix. The 2026-10-04 internal product approval supplies no customer validation or learning-efficacy result. The GĐ1 audit must still reconcile the actual BA workbook and its traceability before declaring Internal BA Baseline Approved.
