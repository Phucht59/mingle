# Phase 1 Implementation Roadmap — canonical 2026-09-24

Sequence is dependency-driven. Source existence does not equal runtime completion.

| Slice | Deliverable | Current status | Exit evidence |
|---|---|---|---|
| 1. Product/scientific foundation | Charter, PRD, Evidence Model, Feed spec, Q1–Q18 resolution | **DONE** | Active specs under `02_product/`, research resolution under `03_research/` |
| 2. Authority intake | Exact V3.2 sources, DDL/OpenAPI/original checks, compatibility mapping | **BLOCKED/PARTIAL** | File hashes + exact rule IDs + original 115+22 suite runnable |
| 3. Developer bootstrap | Canonical repo, FastAPI/worker source, Flutter shells | **SOURCE DONE** | Clean documented source layout; runtime items continue below |
| 4. Data/runtime foundation | PostgreSQL migrations, durable worker execution, object storage | **ACTIVE / DB BLOCKED** | Real PostgreSQL migration + six integration/concurrency tests + worker/API ready=200 |
| 5. Flutter foundation | Learner Android and staff Web shells | **SOURCE DONE / RUNTIME BLOCKED** | Analyze/test/build plus actual Android/Web boot evidence |
| 6. Boundaries and quality | Command/telemetry separation, logs/errors, tests, CI | **PARTIAL** | Hosted CI green except no substituted original checks; exact V3.2 gate wired |
| 7. Phase 1 audit | Clean reproduction, evidence report, issue/CR register, gate | **ACTIVE** | Mandatory Phase 1 gate PASS |

Phase 1 must not implement full later-phase learning/scoring/ML features merely to appear complete. Product policies are documented now to prevent drift; contract-dependent implementation waits for exact authority when required.
