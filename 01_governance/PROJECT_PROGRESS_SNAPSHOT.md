# Project Progress Snapshot — 2026-09-24

## Milestone

**Canonical repository reorganization completed. Phase 1 remains ACTIVE and its gate remains NOT PASSED.**

## DONE

- Phase 0 architecture/contract baseline recorded as V3.2 source of truth.
- Phase 1 research resolution Q1–Q18 completed and preserved.
- Product Charter, MVP PRD, Learner Evidence Model and Adaptive Feed MVP specification preserved as active product material.
- Greenfield FastAPI backend/API foundation, durable-worker source, PostgreSQL migration source and immutable local-storage adapter exist.
- Separate learner/staff Flutter shell source and tests exist.
- Command and telemetry boundaries remain separate in foundation code.
- Existing evidence preserves 10 backend unit/security/storage test passes, API liveness smoke and local-storage smoke.
- Canonical repo reorganized into governance, product, research, architecture, code, quality, operations, handoff and archive domains.
- Previous handoff pack and original source bundle preserved under `99_archive/` / `08_handoff/provenance/`.

## ACTIVE

- Phase 1 implementation foundation closure.
- Exact V3.2 contract/source mapping once original sources are supplied.
- Runtime verification on supported PostgreSQL/Flutter/hosted CI environments.

## BLOCKED

- Original V3.2 source and exact 115 contract + 22 SQL verification sources are absent.
- Real PostgreSQL migration/concurrency verification and successful durable-worker runtime are not yet evidenced.
- Flutter analyze/test/build plus actual Android/Web boot are not yet evidenced.
- Hosted CI and whole-stack clean reproduction are not yet evidenced.

## DEFERRED

- Formal Phase 2 UX/UI Product System start.
- Identity/Auth/Authorization and all later roadmap phases.
- Production ML/recommendation implementation and weights.

## Frozen decisions retained

Flutter Android-first learner; Flutter Web staff/admin; iOS-capable direction. FastAPI/Python, PostgreSQL, Object Storage, modular monolith, API + durable worker same codebase, server-authoritative scoring/progress/permission, command/telemetry separation, durable offline queues, immutable/versioned published content, exact revision pinning, event/knowledge/source time separation, Mastery != Risk, Risk optional for recommendation, Prediction/Decision/Exposure/Execution/Outcome separation, and product operation without ML/recommendation.

## Gate

Use `06_quality/gates/PHASE_1_GATE.md`. No folder cleanup, source existence, schema pass or authored test alone may be used to relabel Phase 1 DONE.
