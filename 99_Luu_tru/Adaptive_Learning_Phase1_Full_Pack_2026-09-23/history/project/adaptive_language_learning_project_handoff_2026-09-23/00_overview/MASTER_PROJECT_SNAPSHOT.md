# MASTER PROJECT SNAPSHOT

## Project

**Adaptive Language Learning & Early Intervention Platform**  
Origin: productization and substantial redesign of Trần Hoàng Phúc's graduation thesis (KLTN).

## Product goal

Transform the research-oriented thesis system into a real, startup-style language-learning product that supports:

- learner study flows;
- content management and publishing;
- assessment;
- offline mobile usage;
- telemetry;
- analytics;
- learning intelligence;
- risk prediction;
- recommendation/intervention;
- staff/admin workflows;
- production deployment;
- continuous improvement.

## Current authoritative baseline

- Architecture/contract baseline: **V3.2**.
- V3.2 is the **source of truth for implementation**.
- Baseline quality assessment after revision: **9/10**.
- Verification status recorded in project memory:
  - **115 contract checks passed**.
  - **22 SQL checks passed**.
- V3.2 is a **specification + verification-code baseline**, not a complete application.
- No additional general architecture review is required before implementation.
- Architecture is reopened only if implementation uncovers a **specific blocking defect**.
- Foundational changes must go through an **Implementation Issue / Change Request**; business rules must not be silently changed in code.

## Phase status

- **Phase 0 — Architecture & Contract Baseline: DONE**.
- **Phase 1 — Implementation Foundation / Product Build Kickoff: ACTIVE**.

No later phase is considered completed merely because the architecture or database schema exists.

## Frozen stack

- Learner app: **Flutter, Android-first**.
- Staff/admin: **Flutter Web**.
- iOS: architecture-compatible, public release later.
- Backend: **FastAPI / Python**.
- Database: **PostgreSQL**.
- Binary/media storage: **Object Storage**.
- Architecture: **modular monolith**.
- Runtime: **API process + durable worker process**, same codebase.

## Core invariants

- Server is authoritative for **scoring, progress, and permission**.
- Commands are separated from telemetry.
- Offline client uses:
  - durable command queue;
  - telemetry queue.
- Published content is immutable/versioned.
- Enrollment/attempts pin exact content revisions.
- Analytics preserves:
  - event time;
  - knowledge/availability time;
  - source capture.
- **Mastery != Risk**.
- Risk is an optional input to recommendation, not the learning engine itself.
- UCI/OULAD remain research baselines; their historical feature weights are not production defaults.
- Production lifecycle separates:
  - Prediction;
  - Recommendation Decision;
  - Exposure;
  - Execution;
  - Outcome.

## Product-development philosophy

The project is intentionally avoiding premature complexity. Kafka, Kubernetes, microservices, a warehouse, or an external feature store are not default choices and require real requirements/load evidence.

The product must still function when ML or recommendation is disabled.
