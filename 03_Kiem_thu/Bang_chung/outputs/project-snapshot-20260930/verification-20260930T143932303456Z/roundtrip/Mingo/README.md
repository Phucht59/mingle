# Mingo — Adaptive Language Learning & Early Intervention Platform

Mingo is one product developed across Phases 1–17. The current repository contains the
Phase 1 implementation foundation: a FastAPI modular monolith, durable worker, PostgreSQL
migrations, immutable local object storage, an Android-first Flutter learner shell, and a
Flutter Web staff shell.

> **Current state:** Phase 0 and Phase 1 are DONE; the Phase 1 gate is PASSED.
> **Phase 2 is ACTIVE — Candidate v1 FAILED independent QC/QA; Rework R1 fixes all 16 logged findings and is READY FOR CODEX EXECUTION + INDEPENDENT QC/QA RETEST. Gate remains NOT PASSED.**
> The canonical R1 UX/UI source is under `02_product/ux_ui/phase2/`. The 94-case retest control is under `06_quality/phase2/`; Codex starts at `08_handoff/phase2/CODEX_START_HERE.md`. Phase 3 remains DEFERRED until independent QC/QA + Tech Lead + Product/Owner signoff passes the Phase 2 gate.

## Start here

1. Read [`START_HERE.md`](START_HERE.md).
2. Check [`01_governance/PROJECT_STATE.md`](01_governance/PROJECT_STATE.md),
   [`06_quality/phase2/PHASE_2_GATE.md`](06_quality/phase2/PHASE_2_GATE.md), and the Phase 1 gate for historical foundation closure.
3. Phase 2 Rework R1 UX/UI source is [`02_product/ux_ui/phase2/`](02_product/ux_ui/phase2/). Codex must follow [`08_handoff/phase2/CODEX_EXECUTION_HANDOFF.md`](08_handoff/phase2/CODEX_EXECUTION_HANDOFF.md); independent QA uses the 94-case retest suite after Codex execution. Use the rest of [`02_product/`](02_product/) for product rules and [`03_research/`](03_research/) for research basis.
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

## Codex execution update — 2026-09-27

Phase 2 remains ACTIVE / GATE NOT PASSED. Canonical suite: 94/94 Codex PASS (44/44 P0); 30 supplemental browser checks PASS. Interactive screen-reader/TalkBack review is BLOCKED. All 20 findings await independent closure; Tech Lead and Product/Owner signoffs remain pending. Phase 3 is DEFERRED. See `08_handoff/phase2/QA_RETEST_HANDOFF.md` and `06_quality/phase2/PHASE_2_VERIFICATION_REPORT.md`.
