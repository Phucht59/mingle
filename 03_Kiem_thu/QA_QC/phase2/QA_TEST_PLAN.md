# Phase 2 QA Test Plan — Rework R1

Test target: UX/UI Product System candidate dated 2026-09-27. Total canonical retest cases: **94** (87 original + 7 independent-audit regression/coverage cases). Canonical case inventory is `QA_TEST_CASES.csv` and the QA workbook.

## Objectives

Validate information architecture, learner/staff flows, business-rule UX integrity, offline/error semantics, responsive/accessibility baseline, prototype behavior, requirement traceability and developer-handoff completeness. QA must not validate future backend/ML correctness that Phase 2 does not implement.

## Test layers

1. **QC artifact review** — package completeness, source-of-truth consistency, no secret, no fake claims.
2. **IA/navigation** — top-level structure, deep-link/back principles, no phase leakage.
3. **Learner flow** — onboarding, cycle, retry/hint/skip/Check, course, profile/fallback.
4. **Staff flow** — learners, content lifecycle, future intervention/analytics/admin boundaries.
5. **Business integrity UX** — completion/mastery, assisted/unaided, revision, reason copy, ML fallback.
6. **Offline/system** — queued vs synced, retry, canonical refresh, media unavailable, re-auth.
7. **Accessibility/responsive** — keyboard, focus, touch size, contrast, text scaling, reduced motion, core viewports.
8. **Handoff** — developer spec/tokens/test IDs/signoff readiness.

## Environments

- Static docs/CSV/XLSX on Windows/macOS/Linux office tooling where available.
- Prototype: Chromium/Chrome latest supported, viewport 390×844 learner and 1440×900 staff; include 360px and 1024px responsive checks.
- No network required for prototype; external requests are a defect.

## Entry criteria

Handoff manifest generated; prototype opens locally; QA workbook present; Phase 2 candidate commit/package identified; no missing P0 artifact.

## Severity

P0 Blocker: source-of-truth contradiction, core flow impossible, false canonical outcome, inaccessible critical action.  
P1 Major: mandatory flow/state missing or misleading business semantics.  
P2 Minor: non-blocking UX inconsistency or secondary accessibility/responsive issue.  
P3 Polish: cosmetic improvement with no task/meaning impact.

## Exit

Use `PHASE_2_GATE.md`. Zero open P0/P1; all P0 tests pass; ≥95% total pass with accepted minor remainder; Product/Owner + Tech Lead signoff.


## Rework R1 execution order

1. Verify package/manifest and R1 static checks.
2. Execute all P0 regression cases first, especially QA-LRN-021 and QA-OFF-007 plus the original learning-integrity cases.
3. Execute representative Grammar/Listening/onboarding and staff publication lifecycle cases.
4. Execute accessibility runtime/assistive-technology matrix.
5. Execute full 94-case suite.
6. Retest every P2-D001..P2-D016 defect and record evidence.
7. Sign off only under `PHASE_2_GATE.md`.
