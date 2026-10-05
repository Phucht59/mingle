# Phase 1 Implementation Roadmap — completed 2026-09-26

Sequence is dependency-driven. Source existence does not equal runtime completion.

| Slice | Deliverable | Current status | Exit evidence |
|---|---|---|---|
| 1. Product/scientific foundation | Charter, PRD, Evidence Model, Feed spec, Q1–Q18 resolution | **DONE** | Active specs under `02_product/`, research resolution under `03_research/` |
| 2. Authority intake | Exact V3.2 sources, DDL/OpenAPI/original checks, compatibility mapping | **DONE** | All 102 files hashed; original 115+22 PASS; exact compatibility mapping recorded |
| 3. Developer bootstrap | Canonical repo, FastAPI/worker source, Flutter shells | **DONE** | Documented source layout and clean runtime reproduction |
| 4. Data/runtime foundation | PostgreSQL migrations, durable worker execution, object storage | **DONE** | Real migration + six native integration/concurrency tests + worker/API ready=200 |
| 5. Flutter foundation | Learner Android and staff Web shells | **DONE** | Analyze/test/build plus actual Android/Web boot |
| 6. Boundaries and quality | Command/telemetry separation, logs/errors, tests, CI | **DONE** | All hosted jobs PASS; unchanged original suites and separate adapter guards |
| 7. Phase 1 audit | Clean reproduction, evidence report, issue/CR register, gate | **DONE** | Mandatory Phase 1 gate PASSED; Phase 2 eligible, not started |

Phase 1 must not implement full later-phase learning/scoring/ML features merely to appear complete. Product policies are documented now to prevent drift; contract-dependent implementation waits for exact authority when required.
