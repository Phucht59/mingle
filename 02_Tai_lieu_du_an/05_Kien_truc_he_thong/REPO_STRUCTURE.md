# Canonical repository structure — 2026-09-24

The project is separated by responsibility so implementation work cannot be confused with research or historical handoff material.

- `02_Tai_lieu_du_an/`: current state, decisions, issues, change requests, backlog, roadmap.
- `02_Tai_lieu_du_an/04_Thiet_ke_san_pham/`: active Product Charter, MVP PRD and learning/product specs.
- `02_Tai_lieu_du_an/03_Nghien_cuu/`: scientific research package and completed resolution; legacy thesis context.
- `02_Tai_lieu_du_an/05_Kien_truc_he_thong/`: V3.2 baseline summaries, compatibility mapping, contract boundary, data/ML guardrails.
- `01_San_pham/backend/src/all_foundation/`: API, worker, config, logs, DB migrations, storage, separate command/telemetry ports.
- `01_San_pham/backend/tests/`: 10 unit/security/storage cases plus six real-PostgreSQL integration/concurrency cases.
- `01_San_pham/apps/learner` and `01_San_pham/apps/staff`: Flutter shell source, widget tests and boot tests.
- `01_San_pham/compose.yaml` and `01_San_pham/backend/Dockerfile`: local foundation stack.
- `03_Kiem_thu/`: gate definitions, standards and runtime evidence.
- `04_Van_hanh/`: CI/env/migration docs and executable setup/verification scripts.
- `02_Tai_lieu_du_an/08_Ban_giao/`: source provenance.
- `99_Luu_tru/`: exact historical packages; not implementation authority.
- `.github/workflows/foundation.yaml`: canonical hosted-CI workflow.

`02_Tai_lieu_du_an/05_Kien_truc_he_thong/contracts/v3_2/source/` preserves the exact owner-supplied V3.2 package, with immutable-byte Git attributes and provenance under `02_Tai_lieu_du_an/08_Ban_giao/provenance/v3_2/`.
