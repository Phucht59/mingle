# Phase 1 local runtime verification — 2026-09-26

Runtime source commit: `eb0dcc169c64813fa8d08aa715eb65073b2f33fe`

## Environment

- Windows 11 25H2
- Python 3.12.10
- PostgreSQL 18, SCRAM authentication
- Flutter 3.32.8, Dart 3.8.1
- Microsoft OpenJDK 17.0.20.1 LTS for Gradle
- Android SDK 35 / build tools 35.0.0
- Android emulator 37.1.11 with AEHD 2.2
- Chrome 153

No password, token, or complete private connection URI is stored in evidence.

## Results

| Boundary | Result | Evidence |
|---|---|---|
| Backend lock/package | PASS | Canonical `.venv`, `pip check` clean; locked requirements retained |
| Ruff | PASS | `backend/backend-lint-20260926T100322Z.log` |
| Focused backend tests | PASS: 9; 7 skipped | `backend/backend-unit-20260926T100322Z.{log,xml}`; six DB tests run separately, Windows symlink test requires privilege |
| PostgreSQL integration/concurrency | PASS: 6/6 | `postgres/postgres-20260926T100322Z.{log,xml}` |
| Migration | PASS repeat-safe | `postgres/postgres-migrate-20260926T100322Z.log` reports no pending migration after the initial application |
| Durable worker | PASS | `worker/worker-*-20260926T100322Z.log`; enqueue, completion and healthcheck exit 0 |
| API real process | PASS: live 200, ready 200 | `api/api-http-smoke-20260926T100338Z.json`, matching process log |
| Local object storage | PASS | `backend/storage-smoke-20260926T100322Z.log` |
| Learner analyze/test/APK | PASS | latest `flutter/learner/*-20260926T100348Z.log` |
| Learner actual Android boot | PASS | APK streamed successfully; API 35 cold start status `ok`; PID present; UI text assertions pass; screenshot/XML/log under `flutter/learner/android-*20260926*` |
| Staff analyze/test/Web build | PASS | latest `flutter/staff/*-20260926T100348Z.log` |
| Staff actual browser boot | PASS | Flutter Chrome debug service connected; HTTP 200; Chrome render screenshot under `flutter/staff/web-*20260926*`; raw DOM kept in ignored diagnostics |

## Local limits

The Windows symlink escape test is skipped because this user token lacks symlink privilege;
the assertion remains enabled and must execute on capable hosted Linux CI. Flutter doctor
reports irrelevant Windows desktop C++ components and cannot identify the newly released
Android Studio metadata, while the Android toolchain itself, licenses, build, emulator and
runtime all pass.

This report does not claim original V3.2 verification or hosted/clean reproduction status.

Initial failed analyze/build/debugger commands and their resolutions are documented in
`flutter/diagnostics/README.md`. Android boot PASS refers to adb and visible UI evidence;
the earlier `flutter run --no-resident` command returned 2 on debugger disconnection.
