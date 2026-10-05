# Canonical reorganization record — 2026-09-24

Parent source revision: `0cb8e3271d80d0e016ab66c1bcd505e64ba2a8ba`.

Purpose: convert the Phase 1 delivery into a developer-oriented canonical repository without changing runtime business logic or claiming new Phase 1 verification.

## Mapping

| Previous location | Canonical location |
|---|---|
| `docs/` | split across `01_governance/`, `02_product/`, `04_architecture/`, `06_quality/`, `07_operations/docs/` |
| `apps/` | `05_code/apps/` |
| `backend/` | `05_code/backend/` |
| `compose.yaml`, `.env.example` | `05_code/` |
| `contracts/v3_2/` | `04_architecture/contracts/v3_2/` |
| `evidence/` | `06_quality/evidence/` |
| `scripts/` | `07_operations/scripts/` |
| comprehensive historical handoff | `99_archive/Adaptive_Learning_Phase1_Full_Pack_2026-09-23/` |

## Integrity notes

- Backend runtime source bytes were preserved during move.
- Learner/staff Flutter source bytes were preserved during move.
- Previous comprehensive Full Pack is preserved as an exact copy in `99_archive/`.
- Scripts and hosted-CI paths were intentionally updated to target the new canonical locations.
- Current status/backlog/onboarding documents were refreshed to remove obsolete “repository absent” wording.
- No V3.2 rule, scoring behavior, permission rule, learning policy or production-ML behavior was changed by this reorganization.
- Phase 1 remains ACTIVE / GATE NOT PASSED.
