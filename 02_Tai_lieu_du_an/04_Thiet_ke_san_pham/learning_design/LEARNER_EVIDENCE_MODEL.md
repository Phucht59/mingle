# Learner Evidence Model — MVP logical specification

Version 0.1 working policy, 2026-09-23; status/terminology reconciliation 2026-10-05. This document defines semantics, not V3.2 database/API fields or a calibrated mastery formula. Exact-source compatibility mapping is completed; implementation must still follow those contracts.

## 1. Typed states and their permitted uses

| State | Example | Allowed use | Forbidden shortcut |
|---|---|---|---|
| Raw observation | First answer wrong on item revision X, retry correct after hint, audio played twice | Immutable audit and assessment | Infer distraction, intelligence or root cause |
| Short-term derived | Due review, repeated error, assisted success, insufficient evidence | Explain provisional scheduler choice | Claim final mastery or CEFR level |
| Curriculum | Objective, domain, task dimension, provisional prerequisite graph, eligibility | Restrict candidate content | Confuse a selected level with certification |
| User intent | Focus Listening, goal TOEIC, target one cycle | Choose examples inside eligible pool | Treat preference as competence |
| Engagement | Streak day, target reached, milestone | Encourage return and track UX | Score mastery/proficiency |
| Future intelligence | Mastery/risk model, knowledge tracing, policy weights | Phase 9+ evaluated extension | Hard-code as Phase 1 truth |

## 2. Raw observation lifecycle

Every scored task has a logical attempt identity, pinned content/item/feedback revision, objective, domain and task type, practice/Check/placement context, first response with its assistance condition, and server-scored correctness. Later retries, hint exposure and replay are separate observations. Skip is its own action, not an attempt marked correct. For the first response, an opened hint or transcript must mark the observation as assisted; never present it as unaided. Event time, receipt/availability time and source/provenance permit honest historical reconstruction. Active duration is nullable, measured only during foreground interaction, with interruption/quality flag and no effect on MVP competence.

Command operations that change score, progress, completion or rewards require server validation and idempotency. Telemetry like view/play can be delayed, lost or client-reported; it cannot silently become canonical score. The Check UI may offer two plays as a provisional experience rule; the backend scores the answer independently. Record separately the *presented play policy*, *client-reported playback*, and *assessment-condition quality*. A missing replay event means *unknown*, not zero; even a reported count does not prove the physical number of listens. Do not certify a standardized listening condition, promote mastery or issue a level from client playback telemetry alone. Exact V3.2 command/telemetry authority is mapped in `02_Tai_lieu_du_an/05_Kien_truc_he_thong/V3_2_COMPATIBILITY_MATRIX.md`; **II-03 is resolved**. Audio events remain analytics/ML-candidate observations, while new assessment-condition fields require explicit versioned contracts in later implementation. Content metadata includes legitimate license/source/attribution and revision pin; do not copy license text into every interaction record.

## 3. Derived signals and evidence thresholds

Derive signals from known-at observations available before a decision, with a named `policy_version`, supporting event IDs, evaluation time and missingness. Initial working defaults:

- `DUE_REVIEW`: prior eligible objective has scheduled review time ≤ decision time. Scheduling cadence is provisional, not an optimized SRS formula.
- `RECENT_ERROR`: recent unaided wrong answer in the same objective, never an error diagnosis.
- `REPEATED_ERROR`: at least two different items in the objective answered wrong unaided; skip and interrupted item excluded.
- `ASSISTED_SUCCESS`: correct after hint/feedback/retry, distinguish first unaided success.
- `RECENT_UNASSISTED_SUCCESS`: a distinct item answered correctly before assistance, tagged by recognition/recall/listening/transfer.
- `INSUFFICIENT_EVIDENCE`: too few comparable independent items, skipped domain or inconsistent accessibility/assessment condition.

These defaults support wording and routing, not final mastery cut scores. A single hint, fast answer, replay or skip cannot be translated into a stable psychological trait. Due flags can be recomputed; preserve policy version and evidence references for auditable decisions. A late event may change *future* state but must not rewrite the evidence available at an earlier decision.

## 4. Independence and uncertainty

Different items under the same objective provide more credible evidence than retrying the same answer. Recognition, recall, listening and contextual use are different dimensions. Practice with hints, a standardized Check and placement differ in support and stakes; their outcomes must remain distinguishable. Record `not_observed`, `observed_provisional`, or `needs_review` as qualitative availability states. User-facing messages cite count/time of underlying observations and allow correction; no calibrated percentage or diagnostic label.

## 5. Logical minimal event dictionary

These names are conceptual and MUST be mapped to original V3.2, not blindly turned into SQL columns.

| Record | Minimum logical fields | Purpose |
|---|---|---|
| Interaction/attempt | pseudonymous actor, idempotency/attempt ID, session ID, item/content/feedback revisions, objective, domain, task type, mode, first response/result, retry index/result, event/known time, source | Canonical scoring and replay audit |
| Assistance | attempt/item reference, hint type and timing, play policy offered, client-reported audio count/event, practice/Check mode, accessibility condition, provenance/quality | Separate aided evidence and assessment conditions; playback telemetry never authorizes score |
| Skip/exposure | exposure ID, revision, objective, reason, event/known time, skip | Distinguish offered from acted upon |
| Recommendation decision | decision ID, policy version, eligible-pool reference, reason code, supporting evidence IDs and time cutoff, selected item/revision | Explain and reproduce selection |
| Execution/outcome | exposure/decision link, execution/attempt link, eventual/independent result | Separate decision, offer, action and learning result |
| Learner intent | focus, stated goal, target cycles, edit time | Respect preference without altering competence |
| Engagement projection | qualifying action ID/day/timezone, streak and target counters, reward rule/version | Idempotent engagement only |

Do not collect contacts, location, microphone recordings, biometric/sensor traces, fine-grained taps, or unrestricted free text for this model. Establish retention TTL, access control, deletion/export and notice before pilot; no invented legal duration. Restrict raw response availability to necessary learning/QA purposes.

## 6. Invariants and verification examples

1. First wrong → feedback → retry correct: raw first wrong remains, assisted/eventual result is true, independent Check remains absent.
2. A skip/exposure without answer: no progress, no mastery or qualifying streak.
3. Audio replay telemetry lost offline: play count unknown; server may still score the answer, but cannot declare a clean one- or two-play listening measurement. A client-reported count is not independently verified.
4. Event at T1 received T3 after decision T2: T2's audit snapshot includes only knowledge available by T2; later scheduling can use T1 after T3.
5. Published revision changes: old attempt remains tied to old revision and old scoring key.
6. ML disabled: raw evidence and deterministic due/current-objective selection remain usable.
7. Profile with one ambiguous item: displays insufficient evidence, not a precise weakness.

Sources: `03_PHASE1_SCIENTIFIC_RESEARCH_RESOLUTION.md` (historical source name), Q1–Q7, Q11–Q12, Q15 and sections 4/9; V3.2 handoff invariants. The [exact-source compatibility matrix](../../05_Kien_truc_he_thong/V3_2_COMPATIBILITY_MATRIX.md) is completed. Later implementation acceptance remains separate from the verified specification boundary.
