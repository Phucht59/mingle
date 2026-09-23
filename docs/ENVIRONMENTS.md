> Current implementation update — 2026-09-23: a new greenfield repository is now supplied under owner authorization; any older statement below that no source exists is historical. API/local storage and 10 tests have runtime evidence. Worker/PostgreSQL, Flutter boot, exact V3.2 checks, hosted CI and full-stack clean reproduction remain unverified. See PROJECT_STATE.md and ../evidence/VERIFICATION_REPORT.md. No original contract mapping is inferred from new infrastructure code.

# Environment Strategy

| Environment | Use | Data and deployments | Gate |
|---|---|---|---|
| Local dev | Fast repeatable boot of API, worker, PostgreSQL, object storage emulator/adapter, Flutter shells | Seed synthetic/test data; secrets outside git | Fresh clone follows one documented setup path |
| CI | Isolated checks on each change | Ephemeral DB and disposable object store; no production credentials | Lint/type/contract/SQL/tests and migration smoke pass |
| Staging / internal alpha (later) | Integration, offline/sync, permissions, operator flows | Separate storage/DB, masked or synthetic data | Reproducible deploy, rollback and observability |
| Pilot (later Phase 15) | ~5 consented users, usability/technical validation | Clear consent, retention/access policy, backup/recovery | Failures/quality reviewed; no efficacy claim |
| Production (later Phase 16) | Real service | Isolated credentials, monitoring, migrations and DR | Separate launch gate |

Configure non-secret values through a typed config object, documented examples and fail-fast validation. Never put real user/credential data in test fixtures. Capture app version, policy version, content revision, environment and request/decision correlation IDs in diagnostics without logging raw answers or secrets by default. Exact deployment/orchestration choices wait for repo and V3.2 source.
