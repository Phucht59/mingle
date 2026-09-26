# Project State — 2026-09-26

| Area | Status | Evidence / note |
|---|---|---|
| Phase 0 — Architecture & Contract Baseline | DONE | V3.2 remains the implementation source of truth |
| Q1–Q18 scientific resolution | DONE | `03_research/phase1/06_SCIENTIFIC_RESEARCH_RESOLUTION.md` |
| Phase 1 product/scientific specification | DONE | Active product material under `02_product/` |
| Phase 1 overall | **ACTIVE — GATE NOT PASSED** | Exact V3.2 originals absent; their hosted job fails closed |
| Repository organization | DONE | Canonical responsibility-based layout retained |
| Python/backend | **PASS local** | Python 3.12.10, locked install, pip check, Ruff, 9 focused unit/security/storage tests |
| PostgreSQL | **PASS local** | PostgreSQL 18; role `mingo_app`; DBs `mingo` and disposable `mingo_test`; 6/6 integration/concurrency tests pass |
| API | **PASS local** | Real Uvicorn process: liveness 200, readiness 200 against migrated `mingo` |
| Durable worker | **PASS local** | Durable enqueue, claim, persisted effect/completion, heartbeat healthcheck pass |
| Learner Flutter | **PASS local** | Flutter 3.32.8; analyze/test/debug APK; API 35 emulator cold boot, process, UI assertions and screenshot pass |
| Staff Flutter Web | **PASS local** | Analyze/test/Web build; actual Chrome render and screenshot pass |
| Exact V3.2 original 115+22 | **BLOCKED external** | Exhaustive active/archive/nested-ZIP/history/bundle search found historical claims and placeholders only |
| Hosted CI | **Foundation PASS / overall BLOCKED** | Run `36250667211`: backend and both Flutter jobs PASS; only original V3.2 job fails |
| Clean reproduction | **PASS full runtime** | Fresh clone, virtualenv, DB cluster, object store, Pub/Gradle caches, Android AVD and Chrome profile; actual client boot inspected |
| Clean handoff | **PASS** | Tracked-source ZIP integrity and exclusion checks; credentials excluded |
| Phase 2 onward | DEFERRED | Not eligible until every Phase 1 mandatory gate passes |

## Canonical local database convention

- Application role: `mingo_app`
- Primary application database: `mingo`
- Disposable automated-test database: `mingo_test`
- No database split by development phase

This is an implementation/development convention and does not reopen V3.2 architecture.
No Change Request is required.

## Remaining closure sequence

1. Obtain the exact V3.2 package and genuine original 115 contract + 22 SQL executable
   suites from an external source, preserve their bytes, and record provenance.
2. Complete exact contract mapping, invoke unchanged original suites, and rerun hosted CI.
3. Re-evaluate the gate. Do not begin Phase 2 while any item remains blocked.

Verified runtime Git revision: `4cdecb426d33b2996f4a3a72cc78da6a276b713f`.
Evidence: `06_quality/evidence/{ci,clean_reproduction}/README.md`.
