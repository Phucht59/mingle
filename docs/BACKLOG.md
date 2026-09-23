> Current implementation update — 2026-09-23: a new greenfield repository is now supplied under owner authorization; any older statement below that no source exists is historical. API/local storage and 10 tests have runtime evidence. Worker/PostgreSQL, Flutter boot, exact V3.2 checks, hosted CI and full-stack clean reproduction remain unverified. See PROJECT_STATE.md and ../evidence/VERIFICATION_REPORT.md. No original contract mapping is inferred from new infrastructure code.

# Prioritized Phase 1 Backlog

State as of 2026-09-23: P0 docs drafted, exact V3.2 and app repository absent. Labels: READY = can start with available material; BLOCKED = cannot responsibly claim implementation before named artifact.

| ID | Priority | Task and output | Dependencies | Status / acceptance |
|---|---|---|---|---|
| P1-01 | P0 | Trace Charter/PRD/Evidence/Feed to Q1–Q18, resolve internal contradictions | Research handoff | READY; section-by-section QA |
| P1-02 | P0 | Acquire exact V3.2 spec/contracts/DDL/check source and latest repo; inventory hashes/versions | Owner source | BLOCKED external; no recreated contract |
| P1-03 | P0 | Compatibility matrix: requirement → exact rule ID/contract → match/gap/conflict → tests | P1-02 | BLOCKED; any real conflict yields issue/CR proposal |
| P1-03a | P0 | Resolve II-03: map Check replay policy and client-reported context to exact command/telemetry contract; decide how assessment uncertainty is represented | P1-02/03 | BLOCKED exact V3.2; no telemetry-only scoring or certified listening condition |
| P1-04 | P0 | Run 115 contract and 22 SQL checks from original suite, record command/environment/output | P1-02 | BLOCKED; counts from handoff are historical |
| P1-05 | P1 | Identify existing repo conventions, bootstrap modular monolith API/worker and Flutter shells | P1-02/03 | BLOCKED until inspect repo; clean dev boot |
| P1-06 | P1 | PostgreSQL local and deterministic migrations; object storage interface | P1-02/03 | BLOCKED exact schema; reversible migration smoke |
| P1-07 | P1 | Set up env/config secrets, structured logs, errors, health/readiness | P1-05 | Partly READY planning; runtime evidence blocked |
| P1-08 | P1 | CI contract/SQL/lint/unit/integration path, database concurrency test harness | P1-05/06 | BLOCKED for execution; every job reproducible |
| P1-09 | P1 | Define separate command/telemetry interfaces and offline queue placeholders | P1-03/05 | BLOCKED for exact API; integration boundary test |
| P1-10 | P1 | Review licensing/source metadata and authoring readiness for five-role cycles | Content scope + later Phase 4 | READY to specify, implementation deferred |
| P1-11 | P1 | Complete privacy/retention/accessibility decision before five-user pilot | Product/legal review, Phase 15 | READY to log, pilot approval later |
| P1-12 | P0 | Phase 1 gate review and updated progress snapshot | P1-01..09 | ACTIVE; FAIL/BLOCKED until runtime evidence |

Implementation tickets P1-05..09 must be adapted after inspecting the actual repo; don't initialize an unrelated replacement project. Task owner may accept a different routine module naming while preserving V3.2 semantics.
