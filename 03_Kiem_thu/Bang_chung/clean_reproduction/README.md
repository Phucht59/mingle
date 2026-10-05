# Full runtime clean reproduction — PASS, 2026-09-26

Source: `4cdecb426d33b2996f4a3a72cc78da6a276b713f`, cloned with
`git clone --no-local C:\Mingo C:\Mingo\.local\clean-reproduction-20260926`.
The initial working tree was clean. Only committed source was cloned; no existing
virtualenv, client build, Dart state, pytest cache, object store or database was copied.

## Isolation

- New Python 3.12.10 virtualenv; locked dependencies and installed backend package.
- New PostgreSQL 18 cluster initialized with `initdb`, SCRAM authentication and newly
  generated credentials; localhost port 55432. Same canonical names `mingo_app`,
  `mingo`, `mingo_test`; `mingo_app` is not a superuser. No `foundation` schema existed
  before migration. The existing local application's data was not used.
- Runtime environment explicitly configured after clearing inherited DB/Python/app
  variables. New object store, Pub cache and Gradle cache.
- Installed pinned toolchains and Android system image reused as toolchains only.
  Flutter hosts were regenerated; authored source/manifests/locks stayed unchanged.
- New AVD `mingo_clean_20260926`; learner package absent before first installation.
- New Chrome profile; staff release output served on localhost port 8132.

## Observed results

| Check | Result |
|---|---|
| Locked installation / pip check / Ruff | PASS |
| Backend-only path with no `.env` | PASS; live=200 / intentionally degraded ready=503; storage smoke PASS |
| Unit/security/storage | 9 PASS; Windows symlink privilege skip; 6 DB skips covered separately |
| Real PostgreSQL integration/concurrency | 6 PASS / 0 FAIL / 0 SKIP |
| Blank DB migration + repeat | PASS; repeat applies nothing |
| API and worker running simultaneously | PASS; live=200, ready=200, worker heartbeat healthy |
| Durable probe queried directly from DB | state=done, exactly 1 persisted effect |
| Learner pub/analyze/test/debug APK | PASS |
| Learner actual fresh Android boot | PASS; cold start 4,984 ms, PID present, both visible strings asserted in UI XML, screenshot inspected, no app startup crash in captured log |
| Staff pub/analyze/test/Web release build | PASS |
| Staff actual Chrome render | PASS; HTTP 200, screenshot inspected: `Learning workspace` and `Content and learner tools will appear here.` |
| Authored source after bootstrap and runs | Unchanged (`git diff --exit-code HEAD -- 05_code 07_operations .github`) |
| Original V3.2 checker | BLOCKED; actual exit 1, not part of the runtime PASS claim |

## Evidence

`run-4cdecb4/commands/` contains setup/install/process logs, environment metadata,
concurrent runtime JSON, Android XML/PNG/logcat and Web PNG/HTTP/Chrome logs.
The sibling directories contain the canonical verifier outputs. `harness/` records
the one-time orchestration used on this Windows host; credentials are generated at
runtime and not embedded. Normal developer commands are in the root README and
`07_operations/docs/LOCAL_RUNTIME.md`.

The fresh PostgreSQL server, API, worker, Web server and emulator were stopped after
verification. No production deployment occurred. SDK metadata/font warnings did not
prevent builds or the inspected UIs. AVD creation logged an optional `devices.xml`
warning, but generated the device and its actual boot succeeded.

**Phase 1 remains ACTIVE.** This reproduction proves the supplied runtime foundation;
the exact V3.2 source and original contract/SQL verification remain the external blocker.
