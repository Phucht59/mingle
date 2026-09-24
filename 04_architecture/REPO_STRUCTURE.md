# Canonical repository structure — 2026-09-24

The project is separated by responsibility so implementation work cannot be confused with research or historical handoff material.

- `01_governance/`: current state, decisions, issues, change requests, backlog, roadmap.
- `02_product/`: active Product Charter, MVP PRD and learning/product specs.
- `03_research/`: scientific research package and completed resolution; legacy thesis context.
- `04_architecture/`: V3.2 baseline summaries, compatibility mapping, contract boundary, data/ML guardrails.
- `05_code/backend/src/all_foundation/`: API, worker, config, logs, DB migrations, storage, separate command/telemetry ports.
- `05_code/backend/tests/`: 10 unit/security/storage cases plus six real-PostgreSQL integration/concurrency cases.
- `05_code/apps/learner` and `05_code/apps/staff`: Flutter shell source, widget tests and boot tests.
- `05_code/compose.yaml` and `05_code/backend/Dockerfile`: local foundation stack.
- `06_quality/`: gate definitions, standards and runtime evidence.
- `07_operations/`: CI/env/migration docs and executable setup/verification scripts.
- `08_handoff/`: source provenance.
- `99_archive/`: exact historical packages; not implementation authority.
- `.github/workflows/foundation.yaml`: canonical hosted-CI workflow.

`04_architecture/contracts/v3_2/` is intentionally an explicit missing-source boundary until exact original V3.2 material is imported with provenance.
