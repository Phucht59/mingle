# Project Progress Snapshot — 2026-09-26

## Milestone

**PHASE 1 DONE — GATE PASSED.** Exact original V3.2 verification, every hosted job,
the local runtime and clean reproduction all pass. **Phase 2 is eligible to start,
but has not been started.** Phase 0 remains DONE.

## Component status

| Component | Result | Current evidence |
|---|---|---|
| Backend | PASS | `06_quality/evidence/backend/` |
| PostgreSQL | PASS | `06_quality/evidence/postgres/` |
| API | PASS, live=200 ready=200 | `06_quality/evidence/api/` |
| Durable worker | PASS | `06_quality/evidence/worker/` |
| Learner | PASS local build + actual Android boot | `06_quality/evidence/flutter/learner/` |
| Staff | PASS local build + actual browser boot | `06_quality/evidence/flutter/staff/` |
| V3.2 originals | PASS: 115 contract + 22 SQL | `06_quality/evidence/v3_2/INTAKE_AND_VERIFICATION_20260926.md` |
| Hosted CI | PASS, all four jobs | `06_quality/evidence/ci/PHASE1_PASS_20260926.md` |
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
- Subsequently received the owner's exact completed V3.2 ZIP; verified all 101 embedded
  manifest entries and preserved all 102 original files including its manifest.
- Wired the unchanged original programs through a checksum-verifying adapter; actual
  local, fresh-clone and hosted runs pass 115 contract plus 22 SQL checks. Nine separate
  adapter guard tests also pass. Historical failed/missing-source evidence is retained.
- Completed the exact-source compatibility matrix and resolved II-03 playback authority.
- Hosted run `36252349822` passes backend, learner, staff and original V3.2 together.

## Issues and limits

No mandatory Phase 1 blockers remain. II-01 and II-03 through II-14 are resolved.
II-02 remains non-blocking. Original SQL uses PGlite; native foundation tests are
separate. This milestone does not claim a complete learning application, native domain
submit/auth/offline acceptance, trained model or production deployment.

## Governance

- New frozen implementation convention: `mingo_app` / `mingo` / `mingo_test`, with no
  phase-specific database split.
- No frozen business rule changed; Change Requests remain NONE.
- Phase 2 is ELIGIBLE TO START; no Phase 2 work was begun.

Git verification baseline: `d4165e8acdffa4e0a747b11ac3e1c3c852674293`.
Hosted run: `36252349822`. Later handoff commits record evidence/governance; the ZIP
sidecar records the exact final packaged Git revision and SHA-256.
