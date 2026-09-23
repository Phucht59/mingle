# Adaptive Language Learning — Phase 1 implementation foundation

New greenfield implementation, authorized by owner on 2026-09-23. Product brand is undecided.
This repository adds executable infrastructure to the previously approved product/scientific specification.
**Phase 1 is ACTIVE; this source tree alone does not close the gate.** See `evidence/VERIFICATION_REPORT.md`.

## Boundaries

FastAPI API and durable worker share one Python package. PostgreSQL owns only the isolated `foundation` probe schema. Storage has an immutable local-development adapter. Learner and staff are separate Flutter shells. Command and telemetry interfaces are separate ports; learning/scoring/auth/sync contracts are not invented from missing V3.2 material.

Exact V3.2 package and original 115 contract + 22 SQL checks are absent. New tests are not substitutes. CI deliberately fails the `original-v3-2` job until the genuine suite is integrated with source provenance. No Change Request is asserted without a demonstrated conflict.

## Local backend

Python 3.12; Linux/macOS. From a clean extraction:

```sh
bash scripts/clean_setup.sh
```

This installs a fresh venv, lints, runs unit/security/storage tests and boots a real API subprocess. PostgreSQL tests are clearly skipped unless explicitly enabled. Without a DB, liveness is 200 and readiness is 503.

For PostgreSQL, API and worker together (Docker + Compose required):

```sh
cp .env.example .env
# Replace POSTGRES_PASSWORD with a random URL-safe local secret.
docker compose up --build -d
docker compose ps
docker compose run --rm migrate python -m all_foundation.cli enqueue-probe --key manual-smoke
docker compose logs worker
curl --fail http://127.0.0.1:8000/health/ready
```

Local ports bind loopback; no domain mutation routes are exposed. This is not a production deployment. Do not use the test database or demo service credentials for learner data. Keep `.env` out of source control.

To run real database tests, provision a **disposable DB whose name ends in `_test`**:

```sh
export TEST_DATABASE_URL='postgresql://USER:PASSWORD@localhost:5432/foundation_test'
RUN_POSTGRES=1 PATH="$PWD/.venv/bin:$PATH" bash scripts/verify_backend.sh
```

These tests DROP the `foundation` schema in that disposable DB. They verify migration checksum/atomic rollback, concurrent deduplication/claim, stale worker fencing, bounded retries and expiring heartbeats.

## Flutter

Pinned SDK baseline: Flutter 3.32.8, commit `edada7c56edf4a183c1735310e123c7f923584f1`; not a claim to the latest release. Requirements: Flutter SDK, Android SDK/device for learner; supported browser for staff.

```sh
bash scripts/bootstrap_clients.sh
cd apps/learner
flutter pub get
flutter analyze
flutter test
flutter run -d ANDROID_DEVICE_ID
# In another shell:
cd apps/staff
flutter pub get
flutter analyze
flutter test
flutter run -d chrome
```

Both are foundation shells. They do not manufacture placement results, learning evidence, reward balances or scoring state. Device boot requires `flutter test integration_test/boot_test.dart -d DEVICE_ID`; building an APK or a web bundle alone is not runtime boot evidence.

## Implementation limits

- Durable worker proof is scoped to transactional PostgreSQL probe effects. External side effects need a reviewed idempotency contract; no claim of universal exactly-once delivery.
- Local object adapter is for a trusted local filesystem, not a production S3 validation. S3/cloud integration and credential policy remain unverified.
- CI YAML is supplied, but no remote repository/CI run is claimed.
- New infrastructure decisions are provisional pending exact V3.2 mapping; approved learning product policies remain unchanged.

## Documentation and history

`docs/` holds current product specs, memory and gate. The comprehensive delivery ZIP also includes research resolution and original historical handoff files in `history/`. Current `docs/` status supersedes historical snapshots, with the authority order in MVP_PRD preserved.
