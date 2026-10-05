# Adaptive Learning Feed — deterministic MVP policy

Working version: 0.1, 2026-09-23. Product-level algorithm, not an approved V3.2 implementation, mastery formula or ML ranking policy. Every provisional threshold is versioned and configurable.

## Inputs and output contract

Inputs: learner's current focus/goal/target; available curriculum objectives and prerequisites; published version-pinned eligible items; available evidence as of decision time; due review schedule; media availability and accessibility mode; policy configuration/version. Output: finite objective-bounded cycle plan with items/functional roles, one primary selection reason per item, source evidence references and a decision ID. Decision, exposure, execution and outcome are distinct; no invented exact API/schema.

## Selection procedure

1. Determine `known_at <= decision_at` evidence and consistent published content snapshot. If offline, use pinned local snapshot and mark policy/content versions. Filter unlicensed, unpublished, unavailable media and recently used same-stem items.
2. Eligibility: reviews of previously encountered objectives; one current objective whose prerequisites are satisfied by provisional, independent evidence; only safe preview for otherwise locked objectives. User-selected level/focus never rewrites evidence or bypasses prerequisite. A0 is internal and not certified CEFR.
3. Build candidate roles. A valid cycle must carry Review, Learn, Retrieve, Transfer and Check as functions. New learners may review a simple prior cue; review-only learners may get a corrective micro-explanation in Learn. Retrieve requires unaided attempt; Transfer changes cue/context/task; Check uses a distinct item before hint. If content cannot support the roles, choose another objective or show a content/unavailable state, not artificial completion.
4. Deterministic ordering: one due review or blocking prerequisite-gap item first when available; then items in chosen focus/current objective; use a recent-error remedial item different from the failed stem; then transfer or one-step challenge when the **same step-up predicate in step 5** holds. Due backlog beyond one item rolls forward. Tie-break by oldest exposure, then stable item ID; no opaque proficiency weights.
5. **Single step-up/challenge predicate (MVP hypothesis):** require at least two unaided correct first responses on two distinct item revisions in the same objective and current task band, with at least one from an independent Check item. A hint, retry, replay-dependent answer with *missing* assessment context, same-stem variant or preview cannot satisfy the predicate. For Listening, a captured UI play-policy context plus client-reported playback can support a **low-stakes provisional challenge**, not a verified listening assessment, mastery or level claim. When the predicate holds, offer **at most one** item from the next task band in the same objective as a `CHALLENGE`; do not raise the learner's level, mark mastery or unlock a new objective from this alone. One success can trigger a Transfer task in the current band, not a difficulty increase. If the predicate does not hold, continue current-band practice, feedback or remediation. Do not use time taken or streak/XP to raise difficulty. Progress between objectives uses a separately reviewed provisional curriculum rule; final thresholds are deferred.
6. Render one factual reason among `DUE_REVIEW`, `RECENT_ERROR`, `PREREQUISITE_GAP`, `CURRENT_OBJECTIVE`, `MODALITY_TRANSFER`, `CHALLENGE` with supporting IDs. Do not claim an error's psychological cause. If evidence is missing, show ordinary curriculum continuation.
7. Continue until the objective receives feedback and Check/next-review plan. ~5 minutes is a target, not a cutoff during an item. At closure show what was practiced, uncertainty and next step. Pause/resume preserves state. Only explicit user action starts another cycle; skip-only path is not completed.

## Reason priority and focus

| Situation | Reason | Behavior |
|---|---|---|
| Due item valid | DUE_REVIEW | Insert at most one in default cycle before focused content. |
| Missing prerequisite blocks chosen objective | PREREQUISITE_GAP | Show why, select prerequisite or offer preview-only chosen objective. |
| Recent unaided error in current objective | RECENT_ERROR | Remediate using another stem and feedback. |
| Eligible learner-selected domain | CURRENT_OBJECTIVE | Fill main portion of cycle with valid focus. |
| Adequate knowledge in familiar format | MODALITY_TRANSFER | Switch cue/context, e.g. written→audio or recognition→usage. |
| Two distinct unaided first-response successes in current band, including one independent Check | CHALLENGE | At most one next-band item within the objective; no level/mastery/prerequisite promotion. |

No fixed numeric weight allocation is claimed as evidence. The bounded one-item insertion and two-item step-up predicate are pilot hypotheses, not frozen scoring contracts. `MODALITY_TRANSFER` may occur within the current band before step-up; it is not synonymous with `CHALLENGE`.

## Fallback and failure handling

If ML disabled, stale or unavailable, use the exact deterministic procedure above. If the recommendation subsystem itself is disabled, expose the eligible curriculum next item and due-review list, enabling a usable manual cycle. If media unavailable offline, choose a valid alternative in the same objective and log `FALLBACK_MEDIA_UNAVAILABLE`; if no item can meet five roles, show honest content gap/sync action. Never bypass prerequisite, claim completed Check or fabricate selection evidence. Offline events arriving late change later decisions only; preserve earlier decision snapshots.

## Audit and tests

Persist policy version/config revision, decision time, eligible-pool reference, selected content revision, primary reason, supporting evidence IDs, exposure time, execution and outcome IDs. Validate:

- a due review and focus Listening yields at most one justified due item plus Listening-eligible plan;
- a blocked focus offers prerequisite with explanation/preview, not a false unlocked course;
- same-item post-feedback retry does not qualify as independent success or a challenge trigger;
- one unaided correct item does not trigger a harder band; two distinct unaided correct first responses in the same objective/band including an independent Check trigger at most one next-band challenge; neither case changes level or unlocks a prerequisite;
- two correct responses where one follows a hint or an assessment condition is unknown do not trigger step-up;
- wrong→hint→correct remains assisted;
- disabled ML/recommender and offline media loss have usable and auditable fallback;
- no valid transfer/Check content results in no fabricated cycle completion;
- late offline event cannot appear in an earlier decision's evidence set;
- duplicates/revision mismatch cannot duplicate progress, reward, exposure or score.

Research source: `03_PHASE1_SCIENTIFIC_RESEARCH_RESOLUTION.md`, Q1–Q18 and scheduler synthesis. Original V3.2 may define additional constraints; any conflict needs an issue and explicit CR if a frozen rule must change.
