# Phase 2 Contract — UX/UI Product System

## Purpose

Turn approved product/scientific requirements and frozen V3.2 boundaries into a complete, testable and implementation-ready product experience. After this phase, a developer should not need to invent core navigation, interaction states, offline/error semantics, evidence language or content lifecycle UX.

## Inputs and authority

Authority order is unchanged: explicit owner instruction → exact approved V3.2 → approved Change Request/latest owner-approved decision → scientific resolution/Product Charter/MVP PRD → current governance → historical archive.

Primary inputs: V3.2.0, Product Charter, MVP PRD, Learner Evidence Model, Adaptive Feed MVP Spec, Q1–Q18 scientific resolution and Phase 1 verified runtime constraints.

## In scope

- Product information architecture for learner and staff surfaces.
- End-to-end learner/staff journeys.
- Screen inventory, routes, deep-link/back behavior and required states.
- Shared component/state catalog.
- UX reference visual system and semantic design tokens.
- Responsive and accessibility baseline.
- Evidence-honest microcopy/content rules.
- Offline/sync/loading/empty/error UX.
- Self-contained clickable prototype for core flows.
- PRD→UX→QA traceability.
- Developer handoff and QC/QA handoff package.

## Out of scope

- Production authentication/authorization (Phase 3).
- Content backend/publishing implementation (Phase 4).
- Learning/scoring/progress engine implementation (Phase 5).
- Offline synchronization engine implementation (Phase 6).
- Worker domain expansion (Phase 7).
- Production analytics/intelligence/risk/recommendation logic (Phases 8–11).
- Full staff business application implementation (Phase 12).
- Production security/performance hardening (Phase 13).

Prototype data is illustrative only and must not be mistaken for production logic or validated learning/risk 03_Kiem_thu/Bang_chung/outputs.

## Frozen boundaries that UX must respect

Server authority for scoring/progress/permissions; command != telemetry; immutable published content and revision pinning; event time/known time/source capture; completion != mastery; mastery != risk; risk optional for recommendation; decision/exposure/execution/outcome distinct; deterministic learning fallback when ML/recommendation is disabled.

## Versioned MVP hypotheses, not permanent truth

Approximate 5-minute cycle, one practice retry, up-to-two Check plays, two-evidence challenge predicate, bounded one due/prerequisite insertion, 6–9 item placement and one cycle/day default. UI uses semantic/configurable patterns rather than hard-coding these as permanent brand claims.

## UX principles

1. Correctness and learning integrity.
2. Clarity.
3. Accessibility.
4. Low friction.
5. Consistency.
6. Visual quality.
7. Delight/motion.

Visual direction: friendly, calm, lightweight, supportive and clear; avoid childish, casino-like, clinical, school-admin-heavy or AI-tech-demo presentation.

## Deliverables

All artifacts listed in `README.md`, plus QA control workbook under `03_Kiem_thu/QA_QC/phase2/`.

## Phase 2 exit gate

Phase 2 is DONE only when QC/QA reports: no open P0/P1 defect; all mandatory tests pass; PRD-01..16 traceability is complete; accessibility/responsive baseline passes; no V3.2 contradiction is found; developer handoff is accepted; owner and tech signoff recorded. Until then status is `DESIGN_COMPLETE_READY_FOR_QC_QA`.
