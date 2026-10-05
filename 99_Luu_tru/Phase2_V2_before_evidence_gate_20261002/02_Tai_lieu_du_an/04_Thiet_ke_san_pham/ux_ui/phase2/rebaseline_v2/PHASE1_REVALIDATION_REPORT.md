# Phase 1 revalidation

Phase1 remains DONE / GATE PASSED; current local regression PASS. Backend source and foundation configuration match pre-rework hashes. Ran verify_backend.ps1 -Python C:/Mingo/.venv/Scripts/python.exe -RunPostgres in the host PowerShell runtime. Ruff passes; unit run9 passed/7 skipped, native PostgreSQL run6 passed; worker persists/completes its durable probe, API live/ready200/200, local immutable storage smoke passes. No schema/business migration was added.

Flutter3.32.8 / Dart3.8.1 learner and staff analyze/widget tests pass; learner debug APK and both compiled Web apps build. Android emulator boots the V2 app and initializes the licensed audio adapter; Chrome runtime traverses learner and staff flows. Authored Flutter presentation changes are authorized Phase2 work; backend/domain implementation remains frozen.

Windows build uses repository-documented ASCII TEMP/TMP/java.io.tmpdir. A first PowerShell5 invocation treated a worker INFO line on stderr as a shell error; the complete host PowerShell rerun passed and both logs remain. Current hosted CI was NOT RUN. Prior hosted evidence is historical, not proof of this candidate. Windows privileged symlink test skips; native PostgreSQL cases run separately. See REGRESSION_REPORT.md for concrete logs and limitations.
