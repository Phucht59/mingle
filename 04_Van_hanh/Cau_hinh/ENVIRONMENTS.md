> Updated 2026-09-26: active source is under `01_San_pham/`; Phase 1 is DONE / GATE PASSED. Current status: `02_Tai_lieu_du_an/07_Tien_do_du_an/PROJECT_STATE.md`; current runtime evidence: `03_Kiem_thu/Bang_chung/clean_reproduction/README.md`. Exact V3.2 originals are preserved; their separate local, clean-clone and hosted suites pass.

# Environment Strategy

| Environment | Use | Data and deployments | Gate |
|---|---|---|---|
| Local dev | Fast repeatable boot of API, worker, PostgreSQL, object storage emulator/adapter, Flutter shells | Seed synthetic/test data; secrets outside git | Fresh clone follows one documented setup path |
| CI | Isolated checks on each change | Ephemeral DB and disposable object store; no production credentials | Lint/type/contract/SQL/tests and migration smoke pass |
| Staging / internal alpha (later) | Integration, offline/sync, permissions, operator flows | Separate storage/DB, masked or synthetic data | Reproducible deploy, rollback and observability |
| Pilot (later Phase 15) | ~5 consented users, usability/technical validation | Clear consent, retention/access policy, backup/recovery | Failures/quality reviewed; no efficacy claim |
| Production (later Phase 16) | Real service | Isolated credentials, monitoring, migrations and DR | Separate launch gate |

Configure non-secret values through a typed config object, documented examples and fail-fast validation. Never put real user/credential data in test fixtures. Capture app version, policy version, content revision, environment and request/decision correlation IDs in diagnostics without logging raw answers or secrets by default. Exact production deployment/orchestration choices remain deferred; current Phase 1 local/CI behavior must stay compatible with V3.2 and avoid premature infrastructure.
