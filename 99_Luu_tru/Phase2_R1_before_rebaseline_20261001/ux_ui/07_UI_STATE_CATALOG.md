# UI State Catalog

Every production implementation must cover at least the states below before a screen can be considered complete. “Happy path only” is not implementation-ready.

| ID | Component | Required states | Invariant / UX rule |
| --- | --- | --- | --- |
| C-001 | AppShell | loading, ready, offline, sync-warning, access-required | Navigation shell never performs business authorization. |
| C-002 | PrimaryButton | default, pressed, focus, disabled, loading | One dominant action per view where possible; disabled reason exposed when important. |
| C-003 | AnswerOption | idle, selected, focus, disabled, correct, incorrect | Color is never the only correctness signal; selection is not submission. |
| C-004 | QuestionCard | ready, submitting, locked, audio-unavailable | Check mode can remove hint action without changing visual identity beyond clear context label. |
| C-005 | FeedbackPanel | correct, incorrect, retry-available, assisted, final | Retry result never rewrites first-response language/history. |
| C-006 | HintPanel | available, open, used, unavailable | Only in practice contexts; using it marks assisted evidence. |
| C-007 | CycleProgress | role-steps, item-progress, complete | Show finite scope; never mimic infinite feed. |
| C-008 | RecommendationCard | due-review, current-objective, prerequisite-gap, recent-error, transfer, challenge, unavailable | Reason must match auditable reason code; no inferred mental-state copy. |
| C-009 | SyncBanner | offline, queued, syncing, synced, partial, failed, reauth | Distinguish device-saved from server-synced. |
| C-010 | EvidenceCard | observed, building, needs-more-evidence, unavailable | No fake mastery percentage or diagnosis. |
| C-011 | ObjectiveCard | current, open, due, locked, preview | Preview cannot produce completion/unlock. |
| C-012 | AudioControl | ready, playing, paused, loading, unavailable, play-limit-reached | Client playback count is telemetry, never canonical score authority. |
| C-013 | EmptyState | nothing-due, no-content, no-search-results, no-data | Never fabricate recommendation/completion. |
| C-014 | ErrorState | retryable, non-retryable, reauth, canonical-refresh | Recovery action must not create duplicate business command. |
| C-015 | ContentStatusBadge | draft, in-review, approved, published, retired, revoked | Published is immutable; edit action creates new draft/revision. |
| C-016 | ContentEditor | clean, dirty, saving, saved, validation-error, conflict | Source/license completeness shown before publish. |
| C-017 | DataTable | loading, populated, empty, filtered, error | Keyboard accessible; row action permission checked server-side later. |
| C-018 | ModalOrSheet | open, processing, error | Destructive/irreversible actions have explicit confirmation and result. |

## Global state hierarchy

Prefer local component state over blocking whole-screen overlays. Use full-screen blocking only when the user cannot safely continue (bootstrap failure, re-auth, incompatible version). Offline/sync status is persistent but not panic-styled. Loading should preserve layout when possible; empty is not error; unavailable intelligence falls back to deterministic learning rather than “AI failed.”


## Rework R1 canonical interaction state clarifications

### Required-response item
`READY → SELECTED → SUBMITTING → RESULT → CONTINUE`; Submit cannot be active with no selection. Where allowed, Skip is an explicit separate result path.

### Practice evidence context
`firstResponse`, `retryResponse`, `retryCount`, `assisted`, `skipped` are independent. Feedback text may change; assistance/first-response context may not be erased.

### Offline authority
`LOCAL_QUEUED → SYNCING → SYNCED` requires an acknowledgement/canonical transition. Restoring network alone does not move to `SYNCED`.
