# Project State — 2026-09-26

Repository organization was normalized on 2026-09-24. **This was a structure/provenance change only; Phase 1 gate status did not change.**

| Area | Status | Evidence / note |
|---|---|---|
| Phase 0 — Architecture & Contract Baseline | DONE | V3.2 remains the implementation source of truth; exact original verification sources are not present in the active package |
| Q1–Q18 scientific resolution | DONE | `03_research/phase1/06_SCIENTIFIC_RESEARCH_RESOLUTION.md` |
| Phase 1 product/scientific specification | DONE | Product Charter, MVP PRD, Learner Evidence Model and Adaptive Feed spec preserved under `02_product/` |
| Phase 1 overall | **ACTIVE — GATE NOT PASSED** | `06_quality/gates/PHASE_1_GATE.md` |
| Canonical repository layout | DONE | Reorganized by governance/product/research/architecture/code/quality/operations/handoff/archive |
| Backend package, health API, local storage | IMPLEMENTED; focused runtime checks PASS | Existing evidence records 10 tests, HTTP live=200/ready=503 without DB, local storage smoke |
| Windows backend rerun | FOCUSED PASS | Python 3.14.7: locked install, pip check, Ruff, 9 unit/security/storage tests and real API liveness. Windows storage portability issue II-09 resolved; 6 DB tests and 1 symlink test skipped. Windows PowerShell wrapper added and rerun. See `06_quality/evidence/PHASE1_RERUN_20260926.md` |
| Durable worker/migrations | IMPLEMENTED; RUNTIME BLOCKED | PostgreSQL 18 service is running, but no DB credentials/test database; six real-PostgreSQL tests and worker probe remain unexecuted |
| Flutter learner/staff | SOURCE AUTHORED; RUNTIME BLOCKED | Flutter and Android toolchain are absent; no analyze/test/build/device or Web boot evidence |
| Exact V3.2 original 115 contract + 22 SQL checks | BLOCKED | Original source/check suite absent from active repository; fail-closed gate retained |
| Hosted CI | AUTHORED; BLOCKED | `.github/workflows/foundation.yaml`; canonical `main` restored from the supplied bundle, but no hosted Git remote/run evidence |
| Full clean reproduction | NOT VERIFIED | Fresh Python venv/backend install rerun passes on Python 3.14; DB/worker/Flutter/hosted CI and exact originals remain incomplete |
| Phase 2 onward | DEFERRED | Not formally eligible until Phase 1 mandatory gate passes |

## Authority order

Explicit owner instruction > exact approved V3.2 > approved Change Request/latest approved decision > Phase 1 scientific resolution > current state/snapshot/register > older history.

## Current next work

1. Provide/access the PostgreSQL `postgres` role password and create/use a disposable `mingo_test` database; run migrations and six integration/concurrency tests, then boot worker and API with readiness=200.
2. Provide a supported Flutter/Android device or emulator environment; run pinned Flutter analyze/test/build and actual Android + Web boot verification.
3. Import exact V3.2 originals and the genuine 115+22 verification suite with provenance.
4. Run hosted CI from a clean checkout and complete full-stack clean reproduction.
5. Re-run the Phase 1 gate; only then can Phase 1 be marked DONE.

No architecture redesign is requested. A blocking implementation defect must be demonstrated before reopening V3.2 architecture.
