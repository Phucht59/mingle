# Mingo — Adaptive Language Learning & Early Intervention Platform

Mingo is one product developed across Phases 1–17. The current repository contains the
Phase 1 implementation foundation: a FastAPI modular monolith, durable worker, PostgreSQL
migrations, immutable local object storage, an Android-first Flutter learner shell, and a
Flutter Web staff shell.

> **Current state:** Phase 0 and Phase 1 are DONE; the Phase 1 gate is PASSED.
> Local runtime, clean reproduction, exact original 115 contract + 22 SQL checks and
> every hosted CI job pass. Phase 2 is ELIGIBLE TO START and has not been started.
> This milestone completes the implementation foundation; later product features and
> pilot/production acceptance remain in the Phase 0–17 roadmap.

## Start here

1. Read [`START_HERE.md`](START_HERE.md).
2. Check [`01_governance/PROJECT_STATE.md`](01_governance/PROJECT_STATE.md) and
   [`06_quality/gates/PHASE_1_GATE.md`](06_quality/gates/PHASE_1_GATE.md).
3. Use [`02_product/`](02_product/) for product rules and [`03_research/`](03_research/)
   for their research basis.
4. Use the exact original V3.2 package under
   [`04_architecture/contracts/v3_2/source/`](04_architecture/contracts/v3_2/source/)
   as implementation authority. Its provenance and hashes are preserved.
5. Runtime source is under [`05_code/`](05_code/); repeatable commands are under
   [`07_operations/scripts/`](07_operations/scripts/).

## Canonical database topology

One PostgreSQL server supports one Mingo system:

| Purpose | Name |
|---|---|
| Application role | `mingo_app` |
| Local application database | `mingo` |
| Disposable automated-test database | `mingo_test` |

Development phases never create separate application databases. Runtime reads
`DATABASE_URL`; destructive tests read `TEST_DATABASE_URL` and refuse a database whose
name does not end in `_test`.

Copy `05_code/.env.example` to ignored `05_code/.env`, generate a strong local password,
and replace `CHANGE_ME`. Never commit the resulting file. A PostgreSQL administrator can
provision the local roles once with:

```sql
CREATE ROLE mingo_app WITH LOGIN PASSWORD '<local-random-password>';
CREATE DATABASE mingo OWNER mingo_app;
CREATE DATABASE mingo_test OWNER mingo_app;
```

Docker users can set `MINGO_APP_PASSWORD` in `05_code/.env` and run:

```sh
cd 05_code
docker compose up --build -d
```

Compose creates `mingo` and initializes `mingo_test` on a fresh PostgreSQL volume.

## Backend setup and verification

The canonical Python is 3.12. On Windows PowerShell:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r 05_code/backend/requirements.lock
python -m pip install --no-deps .\05_code\backend
.\07_operations\scripts\verify_backend.ps1 `
  -Python .\.venv\Scripts\python.exe -RunPostgres
```

The PostgreSQL run migrates `mingo`, uses only `mingo_test` for destructive integration
tests, processes a durable worker probe, requires API readiness HTTP 200, and records
timestamped evidence under `06_quality/evidence/{backend,postgres,api,worker}`.

For persistent API/worker processes and client launch commands, follow
[`07_operations/docs/LOCAL_RUNTIME.md`](07_operations/docs/LOCAL_RUNTIME.md).

Linux/macOS CI uses:

```sh
RUN_POSTGRES=1 bash 07_operations/scripts/verify_backend.sh
```

## Flutter setup and verification

Use Flutter 3.32.8 with Dart 3.8.1. Bootstrap deliberately untracked Android/Web host
files while preserving authored `lib/`, `test/`, `integration_test/`, manifests, locks,
and analyzer policy:

```powershell
.\07_operations\scripts\bootstrap_clients.ps1 `
  -Flutter C:\path\to\flutter\bin\flutter.bat
.\07_operations\scripts\verify_flutter.ps1 `
  -Flutter C:\path\to\flutter\bin\flutter.bat
```

The verifier runs pub resolution, analysis, tests, learner debug APK build, and staff Web
build. Actual Android and browser boot evidence belongs under
`06_quality/evidence/flutter/{learner,staff}`.

## Repository layout

```text
01_governance/   current status, decisions, issues, CRs, backlog
02_product/      charter, PRD, learning and product specifications
03_research/     Phase 1 research and legacy KLTN context
04_architecture/ V3.2 baseline mapping, contracts, data/ML boundaries
05_code/         executable backend, apps, Compose and environment template
06_quality/      gates, standards and immutable run evidence
07_operations/   setup, migration and verification instructions/scripts
08_handoff/      provenance and canonical handoff metadata
99_archive/      historical packages only; never current implementation truth
```

## Original V3.2 verification

The owner-supplied package contains the genuine 115 contract and 22 SQL checks.
Follow [`V3_2_VERIFICATION.md`](07_operations/docs/V3_2_VERIFICATION.md) to install
the isolated verification lock and run them. The adapter validates original hashes,
executes unchanged programs on a copy and records fresh reports. SQL uses the original
PGlite engine; native PostgreSQL foundation tests remain separate.

Current closure evidence: [`Phase 1 hosted PASS`](06_quality/evidence/ci/PHASE1_PASS_20260926.md).
