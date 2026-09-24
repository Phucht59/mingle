# Project State — 2026-09-24

Repository organization was normalized on 2026-09-24. **This was a structure/provenance change only; Phase 1 gate status did not change.**

| Area | Status | Evidence / note |
|---|---|---|
| Phase 0 — Architecture & Contract Baseline | DONE | V3.2 remains the implementation source of truth; exact original verification sources are not present in the active package |
| Q1–Q18 scientific resolution | DONE | `03_research/phase1/06_SCIENTIFIC_RESEARCH_RESOLUTION.md` |
| Phase 1 product/scientific specification | DONE | Product Charter, MVP PRD, Learner Evidence Model and Adaptive Feed spec preserved under `02_product/` |
| Phase 1 overall | **ACTIVE — GATE NOT PASSED** | `06_quality/gates/PHASE_1_GATE.md` |
| Canonical repository layout | DONE | Reorganized by governance/product/research/architecture/code/quality/operations/handoff/archive |
| Backend package, health API, local storage | IMPLEMENTED; focused runtime checks PASS | Existing evidence records 10 tests, HTTP live=200/ready=503 without DB, local storage smoke |
| Durable worker/migrations | IMPLEMENTED; RUNTIME BLOCKED | Six real-PostgreSQL tests remain unexecuted; worker not proven against a real DB |
| Flutter learner/staff | SOURCE AUTHORED; RUNTIME BLOCKED | No successful analyze/test/build/device boot evidence yet |
| Exact V3.2 original 115 contract + 22 SQL checks | BLOCKED | Original source/check suite absent from active repository; fail-closed gate retained |
| Hosted CI | AUTHORED; NOT RUN | `.github/workflows/foundation.yaml`; no hosted-run evidence yet |
| Full clean reproduction | NOT VERIFIED | Backend-only evidence exists; DB/worker/Flutter/hosted CI remain incomplete |
| Phase 2 onward | DEFERRED | Not formally eligible until Phase 1 mandatory gate passes |

## Authority order

Explicit owner instruction > exact approved V3.2 > approved Change Request/latest approved decision > Phase 1 scientific resolution > current state/snapshot/register > older history.

## Current next work

1. Import exact V3.2 originals and the genuine 115+22 verification suite with provenance.
2. Run PostgreSQL migrations plus six integration/concurrency tests; boot worker and API with readiness=200.
3. Run pinned Flutter analyze/test/build and actual Android + Web boot verification.
4. Run hosted CI from a clean checkout and complete full-stack clean reproduction.
5. Re-run the Phase 1 gate; only then can Phase 1 be marked DONE.

No architecture redesign is requested. A blocking implementation defect must be demonstrated before reopening V3.2 architecture.
