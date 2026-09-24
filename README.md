# Mingo — Adaptive Language Learning & Early Intervention Platform

Canonical project repository reorganized on **2026-09-24** from the Phase 1 implementation handoff.

> **Current phase:** Phase 1 — Implementation Foundation / Product Build Kickoff — **ACTIVE, GATE NOT PASSED**.
> Phase 0 is DONE. Phase 2+ is DEFERRED until the Phase 1 mandatory gate passes.

This repository is deliberately organized by responsibility so a developer can distinguish current decisions, product/scientific material, research, architecture, executable code, verification evidence, operations, and historical handoff material.

## Start here

1. Read [`START_HERE.md`](START_HERE.md).
2. Check the current truth in [`01_governance/PROJECT_STATE.md`](01_governance/PROJECT_STATE.md).
3. Read the Phase 1 gate in [`06_quality/gates/PHASE_1_GATE.md`](06_quality/gates/PHASE_1_GATE.md).
4. Before implementing a business/domain rule, read [`02_product/MVP_PRD.md`](02_product/MVP_PRD.md), the V3.2 baseline material in [`04_architecture/`](04_architecture/), and the decision/change-control files under [`01_governance/`](01_governance/).
5. Runtime code is isolated in [`05_code/`](05_code/).

## Repository layout

```text
Mingo/
├── 01_governance/          # status, roadmap, decisions, issues, CRs, backlog
├── 02_product/             # charter, PRD, learning/product specifications
├── 03_research/            # scientific research, research resolution, KLTN context
├── 04_architecture/        # V3.2 baseline, boundaries, contracts, data/ML guardrails
├── 05_code/                # executable application/backend code only
├── 06_quality/             # gates, standards, tests/evidence
├── 07_operations/          # CI/CD, environments, bootstrap/verification scripts
├── 08_handoff/             # source provenance and handoff metadata
├── 99_archive/             # immutable historical packages; never use as current truth
├── .github/workflows/      # hosted CI definitions
├── START_HERE.md
├── PROJECT_MAP.md
└── REPO_RULES.md
```

## Phase 1 runtime workspace

Backend/API/worker and Flutter shells live under `05_code/`.

Backend clean setup:

```sh
bash 07_operations/scripts/clean_setup.sh
```

PostgreSQL/API/worker local stack:

```sh
cp 05_code/.env.example 05_code/.env
# Set a random local POSTGRES_PASSWORD in 05_code/.env.
cd 05_code
docker compose up --build -d
```

Flutter bootstrap on a supported machine with the pinned Flutter SDK:

```sh
bash 07_operations/scripts/bootstrap_clients.sh
```

## Important boundary

This reorganization changes **repository layout only**. It does not change V3.2 business rules, scoring semantics, permissions, learning logic, or Phase 1 gate status. Exact original V3.2 source plus the original **115 contract checks and 22 SQL checks are still absent from the active repository**, so the original-contract CI gate remains fail-closed until genuine sources are imported with provenance.
