> Canonical-layout update — 2026-09-24: active source is organized under `05_code/`; Phase 1 remains ACTIVE / GATE NOT PASSED. Current status: `01_governance/PROJECT_STATE.md`; observed runtime evidence: `06_quality/evidence/VERIFICATION_REPORT.md`. Exact original V3.2 verification sources remain absent.

# CI/CD Baseline

The canonical workflow is `.github/workflows/foundation.yaml`. Its presence is not a claim of a successful hosted run; retain run evidence before marking CI PASS.

| Stage | Check | Evidence to retain |
|---|---|---|
| Static | Python format/lint/type where configured, Flutter analyze, secret scan, dependency lock check | Tool version, command, exit status |
| Contract | Exact V3.2 115 contract checks and 22 SQL checks | Original suite version/checksum and results, not reconstructed tests |
| Backend | Unit tests of pure rules; FastAPI integration on ephemeral PostgreSQL; worker retry/idempotency harness | Tests and DB logs sanitized |
| Migration | Blank DB→head, supported previous head→head, forward/rollback plan | Migration IDs and dry-run output |
| Flutter | Android learner and Web staff build/boot smoke; offline queue test when implemented | Artifact hashes and test report |
| System | Health/readiness, object-store adapter, concurrent command replay, permission boundary, policy fallback | Trace IDs and deterministic results |

Run static/unit/contract on each pull request; run DB and build checks before merge, promote later through staging/pilot gates. Never automatically deploy to real users simply because CI passes. Do not use telemetry as authoritative score in fixture design. CI secrets are scoped read-only/ephemeral where possible; no test user data in logs. Deployment commands remain later-phase work; the Phase 1 hosted workflow must be executed from a clean checkout and its evidence retained.
