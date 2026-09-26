# Implementation Issues — 2026-09-24

| ID | Issue | Status / resolution |
|---|---|---|
| II-01 | Exact V3.2 package, original DDL/OpenAPI and 115+22 verification source absent | **OPEN / BLOCKING exact mapping and gate**. Do not recreate or substitute the original suite |
| II-02 | MVP learning hypotheses could be mistaken for frozen scoring/architecture | **OPEN / NON-BLOCKING**. Keep domain/scoring implementation contract-driven |
| II-03 | Offline Check/placement audio replay authority | **OPEN / depends on II-01**. Playback telemetry is not canonical score evidence and cannot prove listens |
| II-04 | PostgreSQL/container runtime not yet evidenced | **OPEN / runtime blocker**. Six integration/concurrency tests exist; run on real disposable PostgreSQL |
| II-05 | Flutter runtime not yet evidenced | **OPEN / runtime blocker**. Authored shells/tests require supported pinned Flutter runtime and actual boot evidence |
| II-06 | No hosted Git CI evidence | **OPEN / verification blocker**. Workflow exists; remote run and full clean reproduction still required |
| II-07 | Previous delivery split active source outside the Full Pack while its index referred to `source/` inside the pack | **RESOLVED 2026-09-24** by canonical repository layout + preserved archive/provenance |
| II-08 | Previous source bundle exported only `HEAD`, causing detached-HEAD clone behavior | **RESOLVED 2026-09-24** in the new canonical handoff bundle with a named `main` branch |
| II-09 | Local immutable storage adapter used POSIX-only directory flags and mishandled Windows `\\?\` resolved paths; concurrent publication failed on the supplied Windows host | **RESOLVED 2026-09-26** in `05_code/backend/src/all_foundation/storage.py`; Windows backend unit suite now 9 passed. Symlink escape test is skipped only when Windows reports privilege error 1314. Evidence: `06_quality/evidence/PHASE1_RERUN_20260926.md`, `backend-unit-20260926.xml` |

No demonstrated V3.2 business-rule conflict. **No Change Request is opened by the repository reorganization.**
