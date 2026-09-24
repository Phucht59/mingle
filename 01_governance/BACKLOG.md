# Prioritized Phase 1 Backlog — 2026-09-24

Labels: DONE = completed with appropriate artifact/evidence; ACTIVE = currently executable; BLOCKED = missing mandatory dependency/evidence; DEFERRED = intentionally later phase.

| ID | Priority | Task / output | Status |
|---|---|---|---|
| P1-01 | P0 | Trace Charter/PRD/Evidence/Feed to Q1–Q18 and resolve internal contradictions | **DONE** — approved product/scientific pack preserved |
| P1-02 | P0 | Acquire exact V3.2 spec/contracts/DDL/original checks; inventory hashes/versions | **BLOCKED external** — repository now exists, but exact originals remain absent |
| P1-03 | P0 | Requirement → exact V3.2 rule/contract → match/gap/conflict → tests | **ACTIVE/PARTIAL** — compatibility material exists; exact mapping waits on P1-02 |
| P1-03a | P0 | Resolve II-03: Check replay/client context vs exact command/telemetry contract | **BLOCKED** on exact V3.2 |
| P1-04 | P0 | Run original 115 contract + 22 SQL checks and capture environment/output | **BLOCKED** on P1-02; historical counts are not a rerun |
| P1-05 | P1 | Bootstrap modular-monolith API/worker and Flutter shells in canonical repo | **DONE (source)** — runtime gate handled separately |
| P1-06 | P1 | PostgreSQL migrations + object-storage foundation | **SOURCE DONE / RUNTIME BLOCKED** — real DB migration/concurrency proof outstanding |
| P1-07 | P1 | Env/config, secret boundary, structured logs, errors, health/readiness | **IMPLEMENTED / FOCUSED EVIDENCE PASS** |
| P1-08 | P1 | CI + unit/integration/concurrency test paths | **AUTHORED / HOSTED RUN BLOCKED**; original V3.2 CI gate intentionally fail-closed |
| P1-09 | P1 | Separate command/telemetry interfaces and offline queue boundaries | **FOUNDATION BOUNDARY DONE / DOMAIN MAPPING BLOCKED** on exact V3.2 |
| P1-10 | P1 | Licensing/source metadata + content-authoring readiness | **DEFERRED** to content work when needed |
| P1-11 | P1 | Privacy/retention/accessibility decisions before real-user pilot | **DEFERRED**; required before pilot, not Phase 1 runtime blocker |
| P1-12 | P0 | Phase 1 gate review and progress snapshot | **ACTIVE** — cannot pass until mandatory runtime/original-check evidence is green |
| P1-13 | P1 | Normalize repository structure and handoff provenance | **DONE 2026-09-24** |

Do not initialize another replacement project. Continue from `05_code/`; changes to frozen behavior follow Implementation Issue / Change Request control.
