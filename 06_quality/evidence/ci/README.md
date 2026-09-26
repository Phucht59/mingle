# Hosted GitHub Actions — 2026-09-26

Verified source revision: `4cdecb426d33b2996f4a3a72cc78da6a276b713f`.

[Run 36250667211](https://github.com/Phucht59/mingo/actions/runs/36250667211)
completed with these observed results:

| Job | Result |
|---|---|
| backend / Python 3.12 / PostgreSQL 16.10 | PASS: Ruff, 10 unit/security/storage tests including symlink escape; separately 6/6 PostgreSQL tests; migration, API ready=200, worker and storage |
| flutter (learner) / Flutter 3.32.8 | PASS: pub, analyze, test, Web build and Android debug APK |
| flutter (staff) / Flutter 3.32.8 | PASS: pub, analyze, test and Web build |
| original-v3-2 | FAIL CLOSED: exact approved sources and original executable suites absent |

**Overall CI: BLOCKED by II-01, not PASS.** Raw job logs and API metadata are
stored in `36250667211/`. Six PostgreSQL skips in the focused unit invocation are
covered by the separate six-test PostgreSQL invocation; Linux has no symlink skip.

The first pushed run, at `eb0dcc1`, exposed a Docker health-command quoting defect:
the runner interpreted `-U` as a Docker flag. `diagnostics/` preserves that failure.
Commit `4cdecb4` fixes the quoting; the subsequent backend job passed without
weakening or skipping its assertions (II-13).

These logs prove hosted builds and backend execution. Actual Android/browser boot
is recorded separately under `flutter/` and `clean_reproduction/`.
