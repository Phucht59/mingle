# Phase 1 Gate — 2026-09-26

**Overall gate: PASSED. Phase 1 DONE; Phase 2 ELIGIBLE TO START, not started.**

## Current mandatory checks

| Check | Result | Evidence / limit |
|---|---|---|
| Python 3.12 locked setup | **PASS** | Python 3.12.10, locked install and `pip check` |
| Ruff + backend unit/security/storage | **PASS local** | 9 passed; 6 DB tests intentionally skipped in focused run; Windows symlink privilege test skipped locally |
| PostgreSQL `mingo` / `mingo_test` | **PASS local** | SCRAM role `mingo_app`; application and disposable test DB verified |
| Migrations | **PASS** | First application plus repeat run (`applied: []`) |
| PostgreSQL integration/concurrency | **PASS: 6/6** | Real PostgreSQL 18, destructive setup confined to `mingo_test` |
| API | **PASS** | Real Uvicorn process; live=200 and ready=200 |
| Durable worker | **PASS** | Enqueue, claim, durable effect/completion and heartbeat healthcheck |
| Learner analyze/test/APK | **PASS local** | Flutter 3.32.8 / Dart 3.8.1 / Android API 35 |
| Learner actual Android boot | **PASS local** | Emulator cold start, app PID, UI assertions and screenshot |
| Staff analyze/test/Web build | **PASS local** | Flutter 3.32.8 |
| Staff actual browser boot | **PASS local** | Flutter dev server + Chrome render screenshot |
| Exact V3.2 source and original 115+22 | **PASS** | Owner-supplied 102 original files preserved and hashed; unchanged 115 contract + 22 PGlite SQL checks pass locally, from a clean clone and on CI |
| Hosted CI | **PASS, all jobs** | Run `36252349822` at `d4165e8`: backend, learner, staff, original V3.2 |
| Full clean reproduction | **PASS runtime** | Fresh clone/venv/DB cluster/object store/Pub+Gradle caches/AVD/Chrome profile; both UIs inspected |
| Repository/secrets/handoff | **PASS** | Canonical tracked-source ZIP integrity/exclusion checks; no known credential matches |

## Interpretation

The runtime foundation is operational locally, from a clean clone and in hosted CI.
Linux runs all 10 unit/security/storage tests, including symlink escape, and separately
all 6 PostgreSQL tests. Both pinned Flutter builds pass. The original V3.2 suites now
also run unchanged, with fresh reports and source integrity verified. Nine adapter
guard tests are additional and not included in the original counts.

## Closure decision and scope

All mandatory foundation checks are now evidenced. See
`06_quality/evidence/ci/PHASE1_PASS_20260926.md`,
`06_quality/evidence/v3_2/INTAKE_AND_VERIFICATION_20260926.md` and the existing full
runtime clean reproduction. II-01/03/06 are resolved; II-02 is non-blocking.

PGlite results do not prove native domain concurrency. The current application remains
the Phase 1 foundation with learner/staff shells; full auth, learning, offline, ML and
pilot acceptance remain later-phase gates. Exact source mapping records those gaps.
No architecture review is reopened and no Change Request exists. Phase 2 is eligible
but has not been started.
