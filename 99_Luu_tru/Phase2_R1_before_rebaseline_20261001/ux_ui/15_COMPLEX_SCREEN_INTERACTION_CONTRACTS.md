# Complex Screen Interaction Contracts — Rework R1

Status: **canonical Phase 2 interaction detail for complex surfaces**. V3.2 remains authority for backend/domain contracts. These contracts remove UX decisions from Phase 3–5 implementation without inventing backend fields.

## Common response state machine — L-022 / L-024 / L-025 / L-027

`READY → SELECTED → SUBMITTING → RESULT → CONTINUE`

Alternative explicit path where allowed: `READY/SELECTED → SKIP_CONFIRM/RECORDED → CONTINUE`.

Rules:
- Submit is disabled until a selection exists; no blank response can advance.
- Selection is local UI state and is not submission.
- `first_response` UX context is never replaced by retry response.
- `assisted=true` is independent of feedback/correctness and persists through result/summary.
- Current practice retry hypothesis allows one retry on Retrieve; Check has no pre-submit hint and no practice retry.
- Skip is explicit, non-shaming and does not create completion/mastery/reward.
- Every result has an explicit Continue transition; result and continue are not the same click.

Recommended hooks: `screen-L-022`, `screen-L-024`, `screen-L-025`, `screen-L-027`, `action-<screen>-submit`, `action-L-029-retry`, stable option IDs.

## L-005 Placement Question

**Anatomy:** domain label, progress, prompt, optional AudioControl, response options, validation, Submit, domain Skip only where policy allows, recorded-result message, Next.

**Validation:** Submit disabled until response; if a domain is explicitly skippable, Skip is a separate action. No global score or CEFR certification wording.

**State:** READY → SELECTED → RESULT → NEXT. Listening can enter MEDIA_UNAVAILABLE and expose explicit domain skip/return path rather than fabricated completion.

**Dependency boundary:** server scoring/placement policy arrives later. Phase 2 only locks the interaction and uncertainty language.

## L-024 Retrieve Item

**Anatomy:** objective context, prompt/stimulus, AnswerOptions, optional Hint action, explicit Skip, result panel, retry action, Continue.

**State data:** `selected`, `firstResponse`, `retryResponse`, `retryCount`, `assisted`, `skipped`, `result`, `final`.

**Invariant:** using a hint sets `assisted=true`; later correct submit never clears it. Retry count is bounded by versioned policy; first response remains visible in evidence context if surfaced.

## L-027 Independent Check

**Anatomy:** Check label, prompt/stimulus, optional AudioControl, AnswerOptions, disabled-until-selection Submit, final result, Continue.

**Forbidden actions:** Hint before submit; practice retry; blank submit. Listening UI may show offered plays but client playback does not authorize score.

## L-060 / L-061 Sync and Recovery

State transitions:

`OFFLINE_AVAILABLE → LOCAL_QUEUED → (network restored, still LOCAL_QUEUED) → SYNCING → SERVER_ACKNOWLEDGED/SYNCED`

Failure branches from SYNCING: `SYNC_PARTIAL`, `SYNC_FAILED_RETRYABLE`, `SYNC_REAUTH`, `CANONICAL_REFRESH`.

Rules:
- `network_online=true` never directly implies `SYNCED`.
- Retry reuses the same durable command identity in implementation.
- Re-auth preserves local queue; it does not grant local authorization.
- Canonical refresh replaces stale presentation with server-confirmed state, not the reverse.
- MEDIA_UNAVAILABLE blocks a media-required assessment path; it never fabricates completion.

## S-031 Content Draft Editor

**Required field/anatomy categories:** item type, domain/objective metadata, learner prompt/stimulus, canonical answer/distractors where applicable, feedback, optional hint, media reference where applicable, source/provenance/license, draft/revision status, reviewer note.

**Actions:** Save Draft, Preview, Submit for Review. Each is distinct. Preview has no publish side effect.

**Validation:** visible and programmatically associated labels; required field error appears adjacent and in targeted alert/status region. Source/license completeness is visible before review/publish.

**Permissions:** Phase 2 specifies UI capability only; Phase 3+ server authorization remains authoritative.

## S-032 Preview

Read-only rendering of the current draft. No learner progress, publication or immutable revision is created. Back returns to draft/review context.

## S-033 Source & License

Required: source reference, reuse/license status, validation/gate reason. Public availability alone is not permission. A verified state enables review approval; failed/unknown state keeps publish blocked.

## S-035 Review Detail

States: `LICENSE_BLOCKED`, `APPROVABLE`, `CHANGES_REQUESTED`. Approve remains disabled while license/provenance gate fails. Request Changes returns an actionable reviewer note to Draft Editor.

## S-036 Publish Confirmation

Modal/sheet with immutable-effect explanation, revision identifier, Cancel and Confirm Publish. Focus is contained while open and restored to Approve when canceled. Confirm creates the transition to S-037.

## S-037 Published Revision

Read-only immutable presentation. No Edit action. `Create new draft from revision` creates a new draft/revision lineage while historical attempts remain pinned to the prior revision.

## Test/evidence requirement

All gate-critical screen/state combinations are explicitly mapped in `SCREEN_STATE_QA_TRACEABILITY.csv`. Codex execution must preserve the stable screen/action identifiers in the prototype and future Flutter test semantics.

## Execution clarifications — 2026-09-27

- New mock responses are queued even while connected; only an explicit mock receipt/canonical refresh clears the queue. Practice retry feedback names the retry and preserves first-response context.
- Draft fields persist in the in-memory prototype across Save/Preview/Review. Publishing snapshots values; a new draft copies that snapshot. Empty prompt/answer blocks review. Changing source invalidates verification. Reload persistence is not implemented or claimed.
- Profile Edit goal returns to Profile after save/clear; it does not change learning evidence.
- Demo controls expose recommendation unavailable and nothing eligible; they are test scenarios, not production navigation.
- Missing-media practice Skip records a skip and shows Continue. Missing-media Check offers Leave cycle without a fabricated result.
- Dialog Tab/Shift+Tab is contained; Escape/Cancel restores its trigger. Selection preserves the selected control's focus. Text at 200% must be checked for ancestor clipping, not only document overflow.
