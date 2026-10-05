# Developer Handoff — Rework R1

## Status and authority

This is a **Phase 2 rework candidate**, not a final gate pass. V3.2 remains architecture/contract authority. Production `05_code/` and original V3.2 are intentionally unchanged by this rework.

The independent audit is preserved under `06_quality/phase2/audits/2026-09-27_independent/`. Do not delete or overwrite it.

## Required read order for implementation

1. `PHASE_2_SPEC.json` + `SCREEN_INVENTORY.csv`
2. `15_COMPLEX_SCREEN_INTERACTION_CONTRACTS.md`
3. `07_UI_STATE_CATALOG.md`
4. `11_OFFLINE_SYNC_UX_SPEC.md`
5. `16_ACCESSIBILITY_FOCUS_LIVE_REGION_SPEC.md`
6. `SCREEN_STATE_QA_TRACEABILITY.csv`
7. `DESIGN_TOKENS.json`
8. exact V3.2 contracts for backend/business semantics

## Stable identifiers / test hooks

Keep screen IDs. Recommended keys:
- `screen-L-024`
- `action-L-024-submit`
- `action-L-029-retry`
- `audio-check`
- `field-S-031-prompt`
- `action-S-036-confirm`

Visual restyling must not force automation IDs to change.

## Assessment interaction state

For required-response surfaces keep distinct UI state fields such as:
- `selected`
- `firstResponse`
- `retryResponse`
- `retryCount`
- `assisted`
- `skipped`
- `submitting`
- `result`
- `final`

Do not encode assistance as a transient feedback string. Do not let Retry mutate first-response evidence.

## Offline binding

Flutter Phase 6 must map the UX states to the durable command engine; do not copy the mock transition implementation as backend truth. Connectivity, local durability, sync attempt, server receipt and canonical state are separate facts.

## Accessibility

HTML ARIA is reference evidence only. Flutter/Flutter Web must implement equivalent Semantics/focus behavior and be tested with TalkBack/keyboard/screen-reader workflows. Whole-app live regions are prohibited.

## Content authoring

Phase 4 backend fields remain future work, but the UI interaction contract is now explicit: author/edit, preview, provenance/license gate, review, publish confirmation, immutable published revision and new-draft flow.

## Prototype

`prototype/index.html` is a self-contained state/behavior reference. It contains test controls for first-use, offline recovery and publication flow. It is intentionally mock-only and must not be shipped as production logic.

## Before implementation is accepted

Use `SCREEN_STATE_QA_TRACEABILITY.csv` and the 94-case QA suite. A screen is not done if mandatory error/loading/offline/disabled/accessibility states are omitted.
