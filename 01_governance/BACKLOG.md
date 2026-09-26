# Prioritized Phase 1 Backlog — 2026-09-26

| ID | Priority | Task / output | Status |
|---|---|---|---|
| P1-01 | P0 | Trace Charter/PRD/Evidence/Feed to Q1–Q18 | **DONE** |
| P1-02 | P0 | Acquire exact V3.2 spec/contracts/DDL/original checks; hash provenance | **BLOCKED external** — exact originals absent |
| P1-03 | P0 | Requirement → exact V3.2 rule/contract → match/gap/conflict → tests | **PARTIAL / waits on P1-02** |
| P1-03a | P0 | Resolve II-03 replay/client context against exact contract | **BLOCKED on P1-02** |
| P1-04 | P0 | Run original 115 contract + 22 SQL checks | **BLOCKED on P1-02**; historical counts are not a rerun |
| P1-05 | P1 | Bootstrap modular-monolith API/worker and Flutter shells | **DONE + local runtime PASS** |
| P1-06 | P1 | PostgreSQL migrations + object-storage foundation | **DONE + local runtime PASS** |
| P1-07 | P1 | Env/config, secret boundary, logs, health/readiness | **DONE + local runtime PASS** |
| P1-08 | P1 | CI + unit/integration/concurrency paths | **PASS hosted foundation**; original gate remains blocked on P1-02 |
| P1-09 | P1 | Separate command/telemetry and offline queue boundaries | **FOUNDATION DONE / exact domain mapping waits on P1-02** |
| P1-10 | P1 | Licensing/source metadata + content-authoring readiness | **DEFERRED** |
| P1-11 | P1 | Privacy/retention/accessibility before real-user pilot | **DEFERRED** |
| P1-12 | P0 | Phase 1 gate review and progress snapshot | **ACTIVE** |
| P1-13 | P1 | Normalize repository structure and provenance | **DONE** |
| P1-14 | P0 | Push canonical revision and collect hosted CI evidence | **DONE**; original job fail-closed documented |
| P1-15 | P0 | Full-stack clean reproduction from tracked source | **DONE / runtime PASS** |
| P1-16 | P1 | Produce clean tracked-source handoff ZIP | **DONE** |

Do not initialize a replacement project or start Phase 2.
