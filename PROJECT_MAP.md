# Project map

## `01_governance/` — what is currently decided
Status, progress snapshots, backlog, decisions, implementation issues, change requests and roadmaps. This is the first place to check whether work is DONE/ACTIVE/BLOCKED/DEFERRED.

## `02_product/` — what the product is supposed to do
Product Charter, MVP PRD, learner evidence model, adaptive-feed specification and supporting learning-design constraints.

## `03_research/` — why product/learning decisions were made
Phase 1 research inputs, the 18-question research package, the completed scientific resolution, and legacy KLTN research context. Research supports decisions; it does not silently override frozen contracts.

## `04_architecture/` — technical boundaries and source-of-truth mapping
V3.2 baseline summaries, compatibility matrix, system boundaries, contract placeholder, decision test vectors and analytics/learning-intelligence guardrails.

## `05_code/` — executable implementation
Only runtime/application source and local stack files live here:

```text
05_code/
├── apps/learner/
├── apps/staff/
├── backend/
├── compose.yaml
└── .env.example
```

## `06_quality/` — how correctness is proved
Phase gates, coding/test/DoD standards and immutable run evidence. Never edit old evidence to make a gate look green; generate new evidence instead.

Current evidence is grouped by runtime boundary:

```text
evidence/
├── backend/
├── postgres/
├── api/
├── worker/
├── flutter/learner/
├── flutter/staff/
├── v3_2/
├── ci/
└── clean_reproduction/
```

## `07_operations/` — how to run, verify and deploy foundations
CI/CD docs, environment/config/migration docs and executable setup/verification scripts.

## `08_handoff/` — provenance
Previous source revision, original bundle, clean handoff metadata and source manifest. A
release ZIP is created from tracked canonical source, never from the polluted working
directory.

## `99_archive/` — history only
Exact previous delivery pack, old prompts and old package snapshots. It is retained for audit but is lower authority than active folders.
