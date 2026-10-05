> Updated 2026-09-26: active source is under `05_code/`; Phase 1 is DONE / GATE PASSED. Current status: `01_governance/PROJECT_STATE.md`; current CI evidence: `06_quality/evidence/ci/PHASE1_PASS_20260926.md`. Exact original V3.2 sources are preserved and verified.

# CI/CD Baseline

The canonical workflow is `.github/workflows/foundation.yaml`. Its presence is not a claim of a successful hosted run; retain run evidence before marking CI PASS.

Observed run `36252349822` at `d4165e8` passes backend (10 unit plus 6 PostgreSQL
tests), both Flutter jobs, 9 adapter guards and the original 115 contract + 22 SQL
checks. See `06_quality/evidence/ci/PHASE1_PASS_20260926.md`. The table below
describes the intended verification boundaries; later domain behavior is not claimed
to exist merely because the Phase 1 infrastructure job passes.

| Stage | Check | Evidence to retain |
|---|---|---|
| Static | Python format/lint/type where configured, Flutter analyze, secret scan, dependency lock check | Tool version, command, exit status |
| Contract | Exact V3.2 115 contract checks and 22 SQL checks | Original suite version/checksum and results, not reconstructed tests |
| Backend | Unit tests of pure rules; FastAPI integration on ephemeral PostgreSQL; worker retry/idempotency harness | Tests and DB logs sanitized |
| Migration | Blank DB→head, supported previous head→head, forward/rollback plan | Migration IDs and dry-run output |
| Flutter | Android learner and Web staff build/boot smoke; offline queue test when implemented | Artifact hashes and test report |
| System | Health/readiness, object-store adapter, concurrent command replay, permission boundary, policy fallback | Trace IDs and deterministic results |

Run static/unit/contract on each pull request; run DB and build checks before merge, promote later through staging/pilot gates. Never automatically deploy to real users simply because CI passes. Do not use telemetry as authoritative score in fixture design. CI secrets are scoped read-only/ephemeral where possible; no test user data in logs. Deployment commands remain later-phase work; the Phase 1 hosted workflow must be executed from a clean checkout and its evidence retained.
