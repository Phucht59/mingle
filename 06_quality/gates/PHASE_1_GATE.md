# Phase 1 Gate — 2026-09-26

**Overall gate: NOT PASSED. Phase 1 ACTIVE; Phase 2 NOT ELIGIBLE.**

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
| Exact V3.2 source and original 115+22 | **BLOCKED external** | Executable originals absent; fail-closed adapter exits 1 |
| Hosted CI | **Foundation PASS / overall BLOCKED** | Run `36250667211`: backend and both Flutter jobs PASS; original V3.2 job fails closed |
| Full clean reproduction | **PASS runtime** | Fresh clone/venv/DB cluster/object store/Pub+Gradle caches/AVD/Chrome profile; both UIs inspected |
| Repository/secrets/handoff | **PASS** | Canonical tracked-source ZIP integrity/exclusion checks; no known credential matches |

## Interpretation

The runtime foundation is operational locally, from a clean clone and in hosted CI.
Linux runs all 10 unit/security/storage tests, including symlink escape, and separately
all 6 PostgreSQL tests. Both pinned Flutter builds pass. None of these substitute for
the absent original V3.2 contract suite.

## Closure rule

Phase 1 can become DONE only after:

1. exact V3.2 source and genuine original 115 contract + 22 SQL suites are supplied,
   hashed, invoked unchanged, and pass;
2. all hosted CI jobs, including the original suite, pass from the canonical revision.

Full runtime clean reproduction and clean tracked-source handoff are already recorded.

No architecture review is reopened. No Change Request exists. Phase 2 remains deferred.
