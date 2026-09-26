# Project Progress Snapshot — 2026-09-26

## Milestone

**Canonical local Phase 1 runtime is operational on Windows. Phase 1 remains ACTIVE and
the gate remains NOT PASSED because exact V3.2 executable originals are absent.
Hosted foundation jobs and full runtime clean reproduction now PASS.**

## Component status

| Component | Result | Current evidence |
|---|---|---|
| Backend | PASS | `06_quality/evidence/backend/` |
| PostgreSQL | PASS | `06_quality/evidence/postgres/` |
| API | PASS, live=200 ready=200 | `06_quality/evidence/api/` |
| Durable worker | PASS | `06_quality/evidence/worker/` |
| Learner | PASS local build + actual Android boot | `06_quality/evidence/flutter/learner/` |
| Staff | PASS local build + actual browser boot | `06_quality/evidence/flutter/staff/` |
| V3.2 originals | BLOCKED | `06_quality/evidence/v3_2/` |
| Hosted CI | Foundation jobs PASS; overall BLOCKED only by V3.2 | `06_quality/evidence/ci/` |
| Full clean reproduction | PASS for supplied runtime | `06_quality/evidence/clean_reproduction/` |
| Tracked-source handoff | PASS | `08_handoff/RELEASE_CHECK_20260926.md` |

## Completed in this milestone

- Installed and used Python 3.12.10; recreated the canonical `.venv` from the backend lock.
- Created/updated PostgreSQL role `mingo_app` with a generated local secret kept only in
  ignored `05_code/.env`; created `mingo` and disposable `mingo_test`.
- Preserved SCRAM authentication. The temporary administrator bootstrap rule was restored
  byte-for-byte and both databases were authenticated as `mingo_app` afterward.
- Passed Ruff, focused backend tests, all 6 real PostgreSQL integration/concurrency tests,
  repeat migration, storage smoke, durable worker probe/healthcheck, and API 200/200 health.
- Normalized Compose and CI to one Mingo database topology.
- Installed Flutter 3.32.8, Dart 3.8.1, Android Studio/SDK API 35, licenses, emulator,
  Microsoft JDK 17, and Android Emulator Hypervisor Driver.
- Fixed missing `flutter_lints` declarations exposed by the preserved-manifest bootstrap.
- Fixed Windows Unicode-profile Gradle verification by using an ASCII Java temp directory;
  used an ASCII AVD home for reliable emulator boot.
- Passed learner analyze/test/debug APK and actual Android cold boot with UI assertions.
- Passed staff analyze/test/Web build and actual Chrome render with screenshot.
- Confirmed `Mingo (2).zip` includes `.git`, `.venv`, `.local`, caches/build output and
  duplicate nested historical archives; it is not a clean canonical handoff.
- Exhaustively rechecked active files, archive, nested ZIPs, Git history, refs and bundles.
  Historical 115+22 claims exist, but executable original suites do not.
- Pushed main and verified hosted backend (10 unit plus 6 PostgreSQL tests) and both
  Flutter jobs. Fixed the runner's Docker health-command quoting issue.
- Reproduced the runtime from a clean clone with new virtualenv, database cluster,
  object store, Pub/Gradle caches, Android AVD and Chrome profile; inspected both UIs.
- Produced and validated a tracked-source ZIP; scanned prospective tracked files for
  known credentials and token patterns with no matches.

## Remaining blockers

1. **II-01 external artifact:** supply the exact approved V3.2 source and original
   executable 115 contract + 22 SQL suites.

The original hosted job remains blocked by the same artifact; other hosted jobs pass.
II-03 exact audio replay mapping also depends on II-01. II-02 remains non-blocking.
II-04/05/07/08/09/10/11/12/13/14 are resolved; II-06 foundation CI is resolved.

## Governance

- New frozen implementation convention: `mingo_app` / `mingo` / `mingo_test`, with no
  phase-specific database split.
- No frozen business rule changed; Change Requests remain NONE.
- Phase 2 remains DEFERRED.

Git runtime baseline verified: `4cdecb426d33b2996f4a3a72cc78da6a276b713f`.
Hosted run: `36250667211`. Later commits record evidence/governance without runtime changes.
