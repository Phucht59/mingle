# MVP Product Requirements Document

Version: Phase 1 working PRD, 2026-09-23. This is testable product behavior, not a claim that the application exists. Exact API/schema field names remain open pending V3.2. Source of policy: completed Phase 1 research Q1–Q18.

## Authority and change precedence

Current explicit owner instruction takes priority; then exact approved V3.2 source, approved Change Requests/latest owner-approved decisions, completed scientific resolution, latest project snapshot/register, older context. This document is a product requirement translation, not authority to silently alter an exact V3.2 scoring, schema, offline or permission rule. If an owner instruction or research-derived default would change a frozen V3.2 contract, record the exact conflict and obtain an approved Change Request before implementing the contract change. When V3.2 is missing, keep the requirement provisional at the interface boundary and continue independent Phase 1 work.

## Actors and primary journeys

Learner on Flutter Android: optional goal → short/provisional placement or start immediately → finite learning cycle → feedback/closure → optionally continue → view qualitative profile/course map. Staff on Flutter Web later authors/reviews versioned content. Backend owns canonical scoring/progress, eligibility and reward; offline client queues commands separately from telemetry.

## Functional requirements and acceptance conditions

| ID | Requirement / default | Acceptance condition | Status |
|---|---|---|---|
| PRD-01 | Each task states an objective; finite cycle implements Review, Learn, Retrieve, Transfer, Check as functions with explicit endpoint and opt-in continuation. | Can finish a cycle without endless scrolling; no timer terminates an unfinished answer; no fake cycle if roles lack valid items. | Baseline; ~5m hypothesis |
| PRD-02 | Persist first response and authoritative correctness separately from each retry and eventual correctness. Practice permits one feedback-guided retry; Check retains unaided first outcome. | First wrong → retry correct keeps first wrong; content/feedback revisions remain pinned. | Freeze principle; retry count hypothesis |
| PRD-03 | Hints are typed by domain and available in practice; before-submit Check has no hint. Assisted correct is not unaided correct. | Hint shown then correct retains both facts; never upgrades independent Check. | FREEZE NOW |
| PRD-04 | Skip is explicit, logged and not completion/mastery. Two skips across distinct exposures of one objective trigger support or alternative, not a forced loop. | Skip alone leaves Check and mastery unaffected; a skip never earns cycle completion. | Freeze principle; threshold hypothesis |
| PRD-05 | Practice listening replay is flexible; Check/placement UI defaults to at most two offered plays, stated before start, with an accessibility mode recorded separately. Playback events from the offline client are client-reported and cannot alone authorize canonical score or certify the true number of listens. | Answer is server-scored independently; unknown/missing replay context remains unknown, and assessment comparability is qualified. Exact command/telemetry authority is mapped in `04_architecture/V3_2_COMPATIBILITY_MATRIX.md`; II-03 is resolved. Assessment-condition metadata remains a later versioned implementation task. | MVP HYPOTHESIS |
| PRD-06 | Vocabulary includes meaning/optional L1 gloss, audio, controlled context and recognition/recall/listening/application; grammar uses concise scaffold, practice, transfer and Check. | One translated card or rule-read does not by itself mark objective mastered. | Principle freeze; sequence hypothesis |
| PRD-07 | A next-band challenge within the same objective is eligible only after **two unaided correct first responses on distinct item revisions in the same current task band, including one independent Check**. Only one next-band item may be offered; one success may prompt current-band Transfer. For Listening, captured client-reported play context suffices only for this low-stakes provisional challenge. | A single success, same-item retry, assisted answer or *missing* Check condition cannot trigger step-up. Challenge does not mark mastery, raise level or unlock another objective; band, evidence IDs and policy version are logged. | MVP HYPOTHESIS |
| PRD-08 | Learner-selected focus selects eligible items; a due review or blocking prerequisite may contribute at most one justified item before focus in a default cycle. | Selection reason visible; no prerequisite bypass or hidden veto. | MVP HYPOTHESIS |
| PRD-09 | Placement optionally tests Vocabulary/Grammar/Listening in 6–9 short rule-branching items with provisional A0–B2 start and missing-domain state. Audio may be skipped; normal study continues calibration. | No mandatory 30–40 minute gate, no numeric CEFR/TOEIC certification; user can start with insufficient evidence. | MVP HYPOTHESIS |
| PRD-10 | Goal is optional, editable, influences examples within eligible path. Learner profile uses qualitative objective/skill state with evidence and uncertainty. | Missing evidence shown explicitly; no mastery percentage; goal change never rewrites measured skill. | Goal hypothesis; profile freeze |
| PRD-11 | Default target one ~5-minute cycle/day, optional multiple cycles; streak uses at least one scored retrieval with feedback per local day (right or wrong), separate from target. | Open-only, passive play and skip do not count; offline replay/timezone changes cannot double-award. | MVP HYPOTHESIS |
| PRD-12 | Reward only for genuine milestones/progress and server-idempotent activity; no click-farmed XP/leaderboard in MVP. | Rewards never change mastery, level, prerequisite or Check result. | MVP HYPOTHESIS |
| PRD-13 | Course map supports browse/review of open content and preview-only for locked objectives; recommendation has one short, actual evidence-backed reason with optional details. | Preview does not grant completion; explanation matches logged reason. | MVP HYPOTHESIS |
| PRD-14 | Content is licensed/attributed, published immutably and scored against the pinned revision. | Revised content does not reinterpret old attempts; failed license review blocks publication. | V3.2 baseline and content rule |
| PRD-15 | Canonical commands, telemetry, decision, exposure, execution and outcome remain distinct; offline queues replay idempotently, with event time and known-at time. | Late event cannot leak into earlier decision; duplicate sync cannot duplicate progress/streak/reward. | V3.2 baseline |
| PRD-16 | ML and recommendation can be disabled while curriculum and due-review fallback still work. | Usable cycle selected without ML; no eligible content produces honest empty state. | V3.2 baseline |

## Operational hypothesis configuration

Version a policy configuration with named parameters, not magic numbers: target cycles=1; desired cycle length≈5m; practice retry cap=1; Check UI play cap=2; repeated error threshold=2 distinct items; repeated skip threshold=2 distinct exposures; forced due/gap cap=1 per default cycle; **step-up evidence threshold=2 distinct unaided first-response successes in one objective/current band including one independent Check, challenge cap=1 next band**. Persist policy version and supporting evidence IDs on decisions/attempt contexts as relevant. Change thresholds via explicit review, test and pilot log; do not market them as validated. Exact config storage and API fields depend on original V3.2.

## Measurement and accessibility

Profile and instrumentation follow `LEARNER_EVIDENCE_MODEL.md`; stage/feedback wording follows uncertainty. Keep audio accessibility mode functional without diagnosing why it was used. Pilot with about five people measures usability, reliability and trust, not causal learning effects. Requirements affecting legal retention, identity, analytics storage and accessibility need review before external pilot.

## Out of scope and release gates

Out of MVP: speaking, unrestricted chat, production ML, final mastery/risk formula, calibrated CEFR cutoffs, large social mechanics, paid gate. This PRD is ready for owner/product review; contract-dependent implementation remains blocked pending exact V3.2. A Phase 1 gate PASS also requires runnable repo/runtime, tests and CI, not merely this document.
