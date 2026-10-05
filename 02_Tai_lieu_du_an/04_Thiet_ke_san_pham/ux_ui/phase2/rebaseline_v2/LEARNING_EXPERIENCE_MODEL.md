# Learning experience model — conceptual, evidence-gated

Updated 2026-10-02. This document formalizes the product model requested by the human directive. It does not add a database schema, scoring formula, curriculum, psychological classifier, or production adaptation engine. V3.2 retains authority. Phase 3 remains HOLD. E0–E3 human validation is PENDING.

The current Phase 2 implementation presents deterministic sample states. A rendered result, passing widget test, or sample progress count does not establish a learner's knowledge or a learning outcome. Scientific support and Mingo-specific hypotheses are separated in the [research register](MINGO_RESEARCH_EVIDENCE_REGISTER.md), particularly RE01–RE16 and RE20.

## Candidate core loop and existing screen responsibilities

**OPEN → NEXT BEST LEARNING ACTION → ACTIVITY → IMMEDIATE FEEDBACK → SESSION SUMMARY → CLEAR NEXT STEP** is the candidate primary journey. Home should offer one understandable learning action and a truthful reason; supporting progress must not obscure that action. Human comprehension and usefulness still require the [usability protocol](PHASE2_USABILITY_TEST_PROTOCOL.md).

The lesson's inner sequence remains **Review → Learn → Retrieve → Transfer → Check**. It supplies different evidence within the outer journey; it is not five new services or five mandatory equal-duration segments.

| Existing surface | Responsibility | Evidence boundary |
|---|---|---|
| Home L-010 | Resume or choose the next eligible action; state a human-readable reason and estimated time | A recommendation is a decision proposal, not proof that an algorithm understands the learner |
| Lesson introduction L-021 | Explain objective, approximate effort, available media and exit/resume expectations | “Khoảng 5 phút” is an estimate where appropriate, not an optimum or a deadline |
| Review L-022 | Retrieve previously introduced material when eligible | Exposure, hint use and repeated identical stems must remain visible in the evidence interpretation |
| Learn L-023 | Explain or demonstrate the target with useful support | Reading or hearing an explanation is opportunity to learn, not proof of recall |
| Retrieve L-024 | Ask the learner to produce or select an answer without an immediate answer reveal | First response, task type and assistance conditions matter |
| Transfer L-025 | Change the prompt or context while retaining the objective | One changed-context MCQ supports a narrow claim, not spontaneous conversational competence |
| Check L-026/L-027 | Gather fresh independent evidence under defined conditions | Current fixture prohibits hint, retry and skip; audio conditions remain explicit |
| Feedback L-028/L-029 | Explain the task-specific error or correct reasoning, support the next attempt | A supported correction never rewrites the original first response |
| Summary L-032 | Separate what was practiced, independently demonstrated, supported, skipped or not checked | Completion and habit cues do not imply mastery |
| Progress L-070 | Present observed facts and qualified evidence with scope/time | No invented mastery percentage; model estimates need later validated rules |

The catalogue remains the authority for route/state IDs. This model assigns meaning to current surfaces and does not expand screen scope.

## Three separate areas of learner state

These areas are conceptual inputs to future decisions. Each observation needs context and provenance. Missing evidence means **unknown**, not zero ability, absent motivation, or failure. A long response could reflect reading, interruption, media failure, assistive technology or task difficulty.

| Area | Possible observations | Interpretation and limits |
|---|---|---|
| **Knowledge** | Correctness; first unaided answer; assisted answer; repeated fresh retrieval; delayed retrieval; changed-context transfer; observed misconception; item/context coverage | Keep objective, item and revision scope. Distinguish recognition from production. A single wrong answer may be an ambiguous item; a single correct answer may be a guess. No latent mastery/risk label follows automatically |
| **Learning experience** | Active response latency; repeated errors; hints; skips; replays; abandonment; retries; resume; voluntary next session; optional self-report | Describe behavior. Do not label someone “bored,” “lazy,” “unmotivated,” or a “bad learner.” Self-report is what the person reported, not psychological ground truth. Consider task and context before interpretation |
| **Context** | Session time; connectivity; offline content/media availability; coarse device capability; accessibility settings voluntarily applied; content availability; interruption/resume | Use only what a decision needs. No precise location, health inference or sensitive disability diagnosis. Device capability may reduce decorative effects without changing assessment semantics |

Experience does not substitute for Knowledge: many hints can coexist with eventual independent learning; quick completion can coexist with little retention. Context does not substitute for either: offline absence from the server is not absence of learning.

## Observed fact, derived evidence, latent estimate

| Layer | Example | Safe presentation |
|---|---|---|
| **Observed fact** | An accepted first response on a pinned revision was correct; a hint was requested; a session was locally saved | State exactly the recorded condition and its authority. Client telemetry cannot certify server acceptance |
| **Derived evidence** | Two distinct first unaided responses for an objective within specified conditions; a fresh delayed check; a changed-context answer | Show scope, assistance, elapsed interval, assessment conditions and missing observations. Rules must be versioned and reviewable |
| **Latent model estimate** | Future inferred mastery or risk probability | Requires label definition, calibration, temporal evaluation, uncertainty and authorized UI rules. Not implemented or demonstrated by this task |

“3 sessions completed,” “topics practiced,” “independent retrieval observed,” and “review due” can be useful when true and qualified. Streak, exposure and completion do not establish mastery. **Mastery != Risk**; risk is only an optional input to a recommendation, never the learner's knowledge score. **Prediction != Recommendation Decision != Exposure != Execution != Outcome**.

## Minimum evidence envelope — conceptual only

For future analysis retain the exact objective/content/item revision, task type and context, first-response identity, assistance level, replay/assessment conditions, attempt/occasion identity, event time, availability/knowledge time and source capture. Join to server-authoritative acceptance/scoring rather than trusting an analytics event's score. For offline activity retain whether data was only saved locally, sent, rejected, or acknowledged by the server. Late arrivals must not retroactively become evidence available at an earlier decision.

Duration should distinguish wall time from active time and exclude background/paused intervals where instrumentation can do so reliably. Mark uncertain intervals unknown. Never compare different task/modality conditions as if they were the same assessment. Repeated same-stem practice is not fresh independent retrieval; a skipped task is not completed evidence.

## Scaffold → Observe → Fade

Support should be contingent on a difficulty, followed by observation and a later opportunity to act independently. The conceptual progression is: initial error → minimal hint; another difficulty → stronger contextual cue; continued difficulty → worked contrast/example; later → fresh independent task. This is a design principle, not authorization to add unlimited hints or retries to current fixtures.

Current presentation preserves the existing bounded practice hint/retry behavior and the no-hint/no-retry Check policy. The current two-play listening Check is a fixture assessment condition; it neither proves that audio reached a physical speaker nor validates listening competence. If media is unavailable, provide recovery or mark the check unavailable; do not invent an answer or completion.

Example: the first unaided answer is wrong; a hint and practice retry yield a correct answer. Record **first unaided wrong + assisted correct**. Later a fresh unassisted check may supply new evidence; it does not convert the first response into a correct unaided response. Supported success can be encouraging without overstating what has been demonstrated.

The existing adaptive-feed preview predicate—two distinct unaided first responses including Check, within the same objective/band—remains an **unchanged provisional fixture/product heuristic**. It permits a bounded optional challenge preview; it does not award mastery, change a level, or unlock a curriculum. It is not a scientifically validated threshold. See [adaptation principles](ADAPTATION_PRINCIPLES.md).

## Current capability and future validation

| Claim | Current machine-completable support | Remaining evidence |
|---|---|---|
| Core loop is understandable | Screens, routes, sample copy and behavior can be tested | Real first-use/think-aloud E1; owner product review |
| Support helps without creating dependence | Distinct assisted/unaided sample behavior and rubric | Fresh later retrieval, assistance trajectory, content review E2 |
| Short sessions fit real circumstances | Approximate duration and exit/resume concept | Actual active/wall duration, interruptions, diary and delayed evidence E1–E3 |
| Progress is meaningful | Qualified facts and evidence categories | Comprehension readback; valid tasks; authoritative future runtime |
| Adaptation improves learning | Explainable heuristic candidate and fallback | Comparison with rule baseline, valid outcomes and future E5 gates |

Use the [measurement framework](MINGO_PRODUCT_MEASUREMENT_FRAMEWORK.md), [content rubric](CONTENT_QUALITY_RUBRIC.md) and [five-person pilot protocol](PHASE2_DIARY_PILOT_PLAN.md). No human result or efficacy claim is supplied here.
