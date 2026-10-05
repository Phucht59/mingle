# Adaptive Language Learning & Early Intervention Platform — Project Handoff Package

Snapshot date: 2026-09-23

This package reconstructs the project state from the shared project history and the currently available project memory. It is intended as a **continuation/handoff pack**, with special emphasis on the transition from the original graduation thesis (KLTN) into a practical learning product.

## What this ZIP contains

- Current project state and frozen decisions.
- Architecture/contract baseline summary for V3.2.
- Product and learner-experience constraints that have been discussed and retained.
- Full roadmap from Phase 0 to Phase 17.
- Phase 1 implementation-foundation scope, gates, and readiness checklist.
- Learning-design hypotheses and evidence requirements for the short-session experience.
- Data/analytics/ML boundaries and production guardrails.
- QA/security/operations principles.
- Legacy KLTN context that remains relevant to the product.
- A handoff prompt for continuing the project in another chat/session.
- A list of source artifacts that are referenced historically but are not physically available in the current runtime.

## Important limitation

The project memory states that **V3.2 is the implementation source of truth**, with **115 contract checks and 22 SQL checks passing**. However, the full original V3.2 specification, verification code, schemas, diagrams, and repository files are not physically present in the current runtime. This package therefore **does not fabricate those missing contracts**. It preserves their status, authority, and integration rules, and explicitly marks the original artifacts as required references.

## Recommended use

1. Read `00_overview/MASTER_PROJECT_SNAPSHOT.md` first.
2. Use `02_architecture/` when an implementation decision could affect contracts or business rules.
3. Use `04_phase_1_foundation/` to continue the current active phase.
4. Use `08_handoff/CONTINUE_PROJECT_SUPER_PROMPT.md` when moving to a new chat.
5. Add the original V3.2 files/repository into `source_materials/` if they become available.
