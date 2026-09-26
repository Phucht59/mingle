# Project State — 2026-09-26

| Area | Status | Evidence / note |
|---|---|---|
| Phase 0 — Architecture & Contract Baseline | DONE | V3.2 remains the implementation source of truth |
| Q1–Q18 scientific resolution | DONE | `03_research/phase1/06_SCIENTIFIC_RESEARCH_RESOLUTION.md` |
| Phase 1 product/scientific specification | DONE | Active product material under `02_product/` |
| Phase 1 overall | **DONE — GATE PASSED** | Every mandatory Phase 1 foundation check has observed evidence |
| Repository organization | DONE | Canonical responsibility-based layout retained |
| Python/backend | **PASS local** | Python 3.12.10, locked install, pip check, Ruff, 9 focused unit/security/storage tests |
| PostgreSQL | **PASS local** | PostgreSQL 18; role `mingo_app`; DBs `mingo` and disposable `mingo_test`; 6/6 integration/concurrency tests pass |
| API | **PASS local** | Real Uvicorn process: liveness 200, readiness 200 against migrated `mingo` |
| Durable worker | **PASS local** | Durable enqueue, claim, persisted effect/completion, heartbeat healthcheck pass |
| Learner Flutter | **PASS local** | Flutter 3.32.8; analyze/test/debug APK; API 35 emulator cold boot, process, UI assertions and screenshot pass |
| Staff Flutter Web | **PASS local** | Analyze/test/Web build; actual Chrome render and screenshot pass |
| Exact V3.2 original 115+22 | **PASS** | Owner supplied exact package; 102 files preserved; 115 contract + 22 original PGlite SQL checks rerun unchanged |
| Hosted CI | **PASS, all jobs** | Run `36252349822` at `d4165e8`: backend, both Flutter jobs and originals all PASS |
| Clean reproduction | **PASS full runtime** | Fresh clone, virtualenv, DB cluster, object store, Pub/Gradle caches, Android AVD and Chrome profile; actual client boot inspected |
| Clean handoff | **PASS** | Tracked-source ZIP integrity and exclusion checks; credentials excluded |
| Phase 2 | **ELIGIBLE TO START; not started** | No Phase 2 implementation performed |
| Phase 3 onward | DEFERRED | Existing roadmap and future acceptance gates remain |

## Canonical local database convention

- Application role: `mingo_app`
- Primary application database: `mingo`
- Disposable automated-test database: `mingo_test`
- No database split by development phase

This is an implementation/development convention and does not reopen V3.2 architecture.
No Change Request is required.

## Closure and scope

II-01 is resolved by exact source intake; II-03 by original command/telemetry mapping;
II-06 by fully successful hosted CI. No mandatory Phase 1 blocker remains. II-02 is a
non-blocking reminder to keep product hypotheses separate from frozen contracts.

This is completion of the implementation foundation. Full learning/auth/offline flows,
domain concurrency, trained ML and pilot/production acceptance belong to later phases
in the existing roadmap. Imported reference DDL is not a new applied migration.

Latest verified source revision: `d4165e8acdffa4e0a747b11ac3e1c3c852674293`.
Full runtime clean reproduction: `4cdecb4`, with unchanged `05_code/` at `d4165e8`;
original verification independently reproduced from a clean clone of `d4165e8`.
See `06_quality/evidence/ci/PHASE1_PASS_20260926.md` and
`06_quality/evidence/v3_2/INTAKE_AND_VERIFICATION_20260926.md`.
