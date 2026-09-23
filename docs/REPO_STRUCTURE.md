# Actual repository structure

- backend/src/all_foundation: API, worker, config, logs, DB migrations, storage, separate command/telemetry ports.
- backend/tests: 10 unit/security/storage cases plus 6 real-PostgreSQL integration/concurrency cases.
- apps/learner and apps/staff: Dart shell, widget test, device boot test and pubspec. Platform host files need pinned Flutter bootstrap; not generated/verified here.
- scripts: clean backend setup, verification, actual HTTP smoke, Flutter host generation, fail-closed original-contract gate.
- .github/workflows/foundation.yaml: CI source, no hosted run.
- compose.yaml and backend/Dockerfile: provisional local stack, not executed here.
- contracts/v3_2: explicit missing-source boundary.
- docs: approved product specs and updated state.
- evidence: actual logs, reports and outcomes. Skipped checks are not pass evidence.

This is an owner-authorized greenfield implementation, not an inspected preexisting app repository. No external git remote is configured.
