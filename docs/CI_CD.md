> Current implementation update — 2026-09-23: a new greenfield repository is now supplied under owner authorization; any older statement below that no source exists is historical. API/local storage and 10 tests have runtime evidence. Worker/PostgreSQL, Flutter boot, exact V3.2 checks, hosted CI and full-stack clean reproduction remain unverified. See PROJECT_STATE.md and ../evidence/VERIFICATION_REPORT.md. No original contract mapping is inferred from new infrastructure code.

# CI/CD Baseline

This is a required pipeline design, not a report of working jobs. Respect existing repository CI when it is provided.

| Stage | Check | Evidence to retain |
|---|---|---|
| Static | Python format/lint/type where configured, Flutter analyze, secret scan, dependency lock check | Tool version, command, exit status |
| Contract | Exact V3.2 115 contract checks and 22 SQL checks | Original suite version/checksum and results, not reconstructed tests |
| Backend | Unit tests of pure rules; FastAPI integration on ephemeral PostgreSQL; worker retry/idempotency harness | Tests and DB logs sanitized |
| Migration | Blank DB→head, supported previous head→head, forward/rollback plan | Migration IDs and dry-run output |
| Flutter | Android learner and Web staff build/boot smoke; offline queue test when implemented | Artifact hashes and test report |
| System | Health/readiness, object-store adapter, concurrent command replay, permission boundary, policy fallback | Trace IDs and deterministic results |

Run static/unit/contract on each pull request; run DB and build checks before merge, promote later through staging/pilot gates. Never automatically deploy to real users simply because CI passes. Do not use telemetry as authoritative score in fixture design. CI secrets are scoped read-only/ephemeral where possible; no test user data in logs. Actual workflow YAML and deployment commands require the real repository.
