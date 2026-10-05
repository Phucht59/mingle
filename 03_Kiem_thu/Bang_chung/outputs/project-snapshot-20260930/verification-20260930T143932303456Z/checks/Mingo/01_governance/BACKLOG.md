# Prioritized Project Backlog — updated 2026-09-27

| ID | Priority | Task / output | Status |
|---|---|---|---|
| P1-01 | P0 | Trace Charter/PRD/Evidence/Feed to Q1–Q18 | **DONE** |
| P1-02 | P0 | Acquire exact V3.2 spec/contracts/DDL/original checks; hash provenance | **DONE** — 102 unchanged original files; manifest verified |
| P1-03 | P0 | Requirement → exact V3.2 rule/contract → match/gap/conflict → tests | **DONE mapping**; later implementation gaps explicitly assigned to future phases |
| P1-03a | P0 | Resolve II-03 replay/client context against exact contract | **DONE authority mapping** |
| P1-04 | P0 | Run original 115 contract + 22 SQL checks | **DONE / PASS local, clean clone and hosted** |
| P1-05 | P1 | Bootstrap modular-monolith API/worker and Flutter shells | **DONE + local runtime PASS** |
| P1-06 | P1 | PostgreSQL migrations + object-storage foundation | **DONE + local runtime PASS** |
| P1-07 | P1 | Env/config, secret boundary, logs, health/readiness | **DONE + local runtime PASS** |
| P1-08 | P1 | CI + unit/integration/concurrency paths | **DONE / PASS all hosted jobs** |
| P1-09 | P1 | Separate command/telemetry and offline queue boundaries | **FOUNDATION + authority mapping DONE**; complete domain/offline implementation belongs to later phases |
| P1-10 | P1 | Licensing/source metadata + content-authoring readiness | **DEFERRED** |
| P1-11 | P1 | Privacy/retention/accessibility before real-user pilot | **DEFERRED** |
| P1-12 | P0 | Phase 1 gate review and progress snapshot | **DONE / PASSED** |
| P1-13 | P1 | Normalize repository structure and provenance | **DONE** |
| P1-14 | P0 | Push canonical revision and collect hosted CI evidence | **DONE**; all jobs PASS, prior fail-closed runs retained |
| P1-15 | P0 | Full-stack clean reproduction from tracked source | **DONE / runtime PASS** |
| P1-16 | P1 | Produce clean tracked-source handoff ZIP | **DONE** |

Do not initialize a replacement project or start Phase 2.


## Phase 2 QC/QA handoff backlog — 2026-09-27

| ID | Priority | Task | Status |
|---|---|---|---|
| P2-QA-01 | P0 | Verify Phase 2 package/artifact completeness and checksum manifest | READY |
| P2-QA-02 | P0 | Execute learner mandatory UX/business-integrity scenarios | READY |
| P2-QA-03 | P0 | Execute staff/content lifecycle scenarios | READY |
| P2-QA-04 | P0 | Execute offline/system and accessibility mandatory checks | READY |
| P2-QA-05 | P1 | Execute responsive, traceability and handoff checks | READY |
| P2-QA-06 | P0 | Triage/retest all P0/P1 defects | PENDING QA |
| P2-QA-07 | P0 | Product/Owner + Tech Lead signoff and Phase 2 gate review | PENDING QA |

Do not start Phase 3 implementation before P2-QA-07 passes.


## Phase 2 Rework R1 backlog — 2026-09-27

| ID | Pri | Work | Status |
| --- | --- | --- | --- |
| P2-R1-01 | P0 | Implement fixes P2-D001..D016 in prototype/spec/handoff | DONE IN CANDIDATE |
| P2-R1-02 | P0 | Run R1 static verifier + browser P0 regression in Codex environment | READY FOR CODEX |
| P2-R1-03 | P0 | Execute 94-case retest and accessibility runtime matrix | PENDING CODEX/QA |
| P2-R1-04 | P0 | Independent QC/QA retest + defect closure | PENDING QA |
| P2-R1-05 | P0 | Tech Lead + Product/Owner signoff, Phase 2 gate | BLOCKED UNTIL QA |

Do not start Phase 3 before P2-R1-05 passes.
