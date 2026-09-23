> Current implementation update — 2026-09-23: a new greenfield repository is now supplied under owner authorization; any older statement below that no source exists is historical. API/local storage and 10 tests have runtime evidence. Worker/PostgreSQL, Flutter boot, exact V3.2 checks, hosted CI and full-stack clean reproduction remain unverified. See PROJECT_STATE.md and ../evidence/VERIFICATION_REPORT.md. No original contract mapping is inferred from new infrastructure code.

# Phase 1 Implementation Roadmap

Sequence is dependency driven; no date promise and no claim of runtime completion.

| Slice | Deliverable | Prerequisite | Exit evidence |
|---|---|---|---|
| 1. Product foundation | Charter, PRD, Evidence Model, Feed spec, decisions | Research handoff | Traceability review to Q1–Q18 and V3.2 summary |
| 2. Authority intake | Exact V3.2 sources and current repo, compatibility matrix | Owner-supplied original artifacts | Rule IDs, schema/API mapping, no unresolved blocking conflicts; original checks runnable |
| 3. Developer bootstrap | Monorepo layout, FastAPI and worker boot, Flutter Android/Web shells | Repo decision and exact relevant contracts | Fresh-clone documented boot and health/readiness checks |
| 4. Data/runtime foundation | PostgreSQL local, deterministic migrations, object storage abstraction | Exact DDL/migrations and ownership contracts | Up/down migrations on disposable DB, transactional smoke and storage smoke |
| 5. Boundaries and quality | Command vs telemetry interfaces, durable worker shell, logging/errors, test harnesses, CI | Contract mapping, bootstrap | Replayed command idempotency test skeleton; contract/SQL, integration and concurrency harness in CI |
| 6. Phase 1 audit | Checklist, evidence report, issues/CR, clean setup verification | Slices 1–5 | Gate PASS from observed runtime and tests; then Phase 2 |

Phase 1 must not implement the full Phase 5–11 learner/scoring/ML features to appear complete. Product policies are documented now to stop drift during later implementation. Missing V3.2 blocks slice 2 and contract-dependent portions of 3–5, but does not block independent documentation.
