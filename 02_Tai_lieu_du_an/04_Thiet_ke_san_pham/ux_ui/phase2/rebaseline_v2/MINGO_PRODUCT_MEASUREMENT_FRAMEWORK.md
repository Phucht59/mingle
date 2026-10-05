# Product measurement framework — learning first

Updated 2026-10-02. Metric definitions and research plan, **not measured results**. All Mingo baselines, numerical targets, human data and production collection below are **UNSET / HUMAN VALIDATION PENDING**. Fixture events/counts and automated UI tests are excluded from product outcome metrics. Phase 3 HOLD.

Goal: meaningful learning, delayed retention, comprehension, autonomy, appropriate challenge, task success and trust with less unnecessary friction, time, privacy cost and device cost. Engagement is a diagnostic; increasing it cannot compensate for worse learning, pressure or misleading progress. This is an adapted [HEART goal → signal → metric framework](https://research.google/pubs/measuring-the-user-experience-on-a-large-scale-user-centered-metrics-for-web-applications/) with Learning and Safety/Trust. Research limitations and hypotheses: [RE01–RE20, RE26](MINGO_RESEARCH_EVIDENCE_REGISTER.md).

## Three primary decision metrics — targets unset

Metric owner roles are proposed responsibilities, not appointment or approval. Content reviewer validates tasks; research lead manages study evidence; Product Owner decides product tradeoffs; engineering owner validates runtime/capture.

| Metric | Decision supported | Unit, numerator and denominator | Window/source/owner | Known limitations |
|---|---|---|---|---|
| **Delayed independent retrieval** | Does a candidate session support later recall under declared conditions? | Unit: participant × objective × assessment occasion. Numerator: fresh first unaided correct responses at the specified delay. Denominator: eligible administered fresh independent prompts under that same condition. Report scheduled/due prompts, actually observed prompts, unavailable prompts and non-return separately | Predeclared protocol interval and objective/revision; validated assessment record joined to exact content/attempt provenance; content reviewer + research lead | Conditional observed success is biased by who returned. Report coverage as its own count; do not silently remove missing/assisted observations or count them as wrong. Baseline prior knowledge and tasks matter; no causal learning gain from a single post-check |
| **Changed-context transfer** | Can evidence extend beyond the practiced prompt? | Unit: participant × objective × new-context assessment occasion. Numerator: correct first unaided answers on reviewed changed-context tasks. Denominator: eligible administered tasks with the same declared response/assistance conditions. Identify near vs broader transfer and task modality | At planned immediate/delayed assessment, not a universal transfer window; reviewer-approved fresh item records; content reviewer + research lead | Narrow recognition transfer does not prove spontaneous speaking or broad language competence. Different tasks cannot be pooled without a defensible mapping |
| **Intended-task success without moderator help** | Is the core journey understandable and recoverable? | Unit: participant × predefined task. Report counts unassisted / assisted / failed / not attempted with reason. Moderator intervention makes completion assisted; a skip is not task success unless intentionally completing a skip/navigation task | Day 0 moderated session and subsequent retest; coded observation sheet and optional consented recording; research lead + product reviewer | Five participants support issue discovery, not population percentages, statistically powered comparisons or guaranteed saturation |

No “82% mastery” or “learning gain” is inferred from these definitions. If gain is studied later, define appropriate pre/post tasks, prior exposure, assessment equivalence, follow-up and comparison design before data collection. A post-test result alone cannot distinguish prior knowledge from gain caused by Mingo. The two learning metrics remain separate from completion.

## Adapted HEART + Learning + Safety/Trust

| Family | Goal and signal | Proposed diagnostic definition | Source / window | Review decision and evidence level |
|---|---|---|---|---|
| Happiness | Helpful, understandable, calm experience; optional learner report | Verbatim optional helpfulness/ease/confidence comments and small-study response counts; retain negative/counterexample cases | Consented task debrief / end-pilot interview | Investigate wording/support/pressure; E1/E3. Confidence is reported perception, not measured competence |
| Engagement | Meaningful practice or review by choice | Observed eligible learning activity, optional review, explicit voluntary next-session start; record intended objective and assistance separately | Valid runtime activity/accepted records with optional purpose-limited telemetry, pilot window | Test whether time supports learning, or indicates friction; E3. Screen time/clicks/streak never primary target |
| Adoption | Reach first meaningful activity | First activity with a learner response under known conditions; keep opening, setup and activity stages distinct | Day 0 observation; future consented first-use window | Remove avoidable start friction; E1. First screen view is not meaningful adoption |
| Retention | Return at useful intervals for the learner and objective | Describe actual return intervals, reason/context and whether meaningful task occurred; non-return reasons and missing observation recorded separately | Days 1–14 diary + reliable eligible-use timestamps | Assess fit with circumstances; E3. Not “daily active” by default; no universal daily quota or five-user population retention |
| Task success | Complete intended task with comprehension | Primary task counts; wrong taps, hesitations, terminology errors, recovery and moderator assistance | Usability sheet / real TalkBack journey / retest | Prioritize core blockage and misleading status, including minority accessibility issues; E1 |
| Learning | Independent recall, retention, transfer with declining required support | Primary learning metrics plus fresh-item assistance trajectory and reviewed misconception resolution | Valid assessment occasions and content review | Revise task/content/support; E2. Hint decline without comparable fresh tasks is not learning |
| Safety/Trust | Honest recommendation, progress, save/sync and permissions | Confirmed lost-data/wrong-status incidents; mismatch between reason and decision; comprehension of local vs server state; complaints about pressure | Future fault/runtime evidence plus human readback | Stop or fix misleading claims/loss; E1/E4. Client telemetry alone cannot certify durability or acceptance |

## Diagnostic drivers and guardrails

Two initial diagnostic drivers: **start/recovery friction** (time or steps to the intended action, errors, help, unavailable media) and **support dependence** (hints/retries with later fresh independent evidence). Interpret them beside Context; latency alone is not emotion or ability.

| Guardrail | Definition and decision |
|---|---|
| Content validity / curriculum coverage | Exact revised objective/task/evidence and reviewer record; no easier-only feed or same-stem success inflation. Invalid tasks cannot support outcome claims |
| Truthful assistance and status | Keep first unaided, supported, skipped, unavailable and acknowledged evidence distinct. Investigate any false-complete/false-synced/false-mastery instance before celebrating usage |
| Learner autonomy | Recommendations can be declined; capture voluntary action separately from reminders/moderator instruction. Do not enforce daily use, streak repair or leaderboard pressure |
| Privacy | Optional study participation/recording/telemetry purpose, minimization and approved retention; no raw answer text/voice or sensitive context by default. A privacy regression blocks collection |
| Accessibility | At least 48dp mobile targets, appropriate contrast, 200% text without critical loss, semantics, reduced motion, keyboard/focus; real TalkBack/core journey remains a human gate |
| Technical reliability/performance | Actual save/ack outcomes and error recovery; physical profile/release measurement for frame/startup/memory/image/energy costs. Technical numbers describe tested device/mode/refresh only |

Guardrail limits and SLOs require the corresponding technical/privacy/product owners and measured baseline. This document sets no invented hardware benchmark or numeric product uplift threshold.

## Time, grain and missingness rules

1. Preserve **event time**, **availability/knowledge time** and **source capture**. Use only information available at the decision being evaluated. Late offline arrivals may improve the current history but cannot justify a past decision retroactively.
2. Duration fields: `estimated_duration` is content metadata; `actual_duration` needs active vs wall time, paused/background intervals and measurement quality. Sum active intervals only when reliable; uncertain clocks/interruptions stay flagged. “Khoảng 5 phút” is not a cut-off or performance goal.
3. Keep completion, abandon stage, resume, assistance, voluntary next session, actual return and delayed retrieval distinct. A backgrounded app is not automatically abandonment. Predeclare the inactivity/window rule later and preserve unknown/censored observations.
4. Deduplicate study/session/attempt/assessment occasions using suitable pseudonymous identifiers; do not count retransmission as a new learning event. Client `answer_submitted` does not mean the server accepted or scored it.
5. Scope every response to exact objective/content/item revision, assessment condition, first attempt, assistance and media availability. Do not merge practice retries into independent-check denominators.
6. Missing observation, task not offered, media unavailable, withdrawal and non-return are different states. Show denominators and coverage, never substitute missing = incorrect or missing = no motivation.
7. Prototype/pilot/production and fixture/human/runtime sources must be labeled. Separate learner counts, tasks and repeated occasions to avoid treating many clicks by five people as many independent participants.

## Research readout and decision cadence

Use [Day 0 usability](PHASE2_USABILITY_TEST_PROTOCOL.md) and the [five-person diary pilot](PHASE2_DIARY_PILOT_PLAN.md). During the pilot review critical integrity/accessibility problems immediately, a midpoint case review for unexplained behavior, and final case-level evidence with missingness/counterexamples. No p-values, population percentages, A/B superiority, ML validity or causal efficacy conclusion from this five-person design.

Each readout records question → evidence level → source/date/build/revision → observed result → alternative explanations → severity → correction → retest or further research needed. Keep proposed target, baseline, observed value and owner decision as separate fields. All are blank/PENDING until actual collection and human review. Metric definitions may be refined before a later approved study, with version and reason; do not move denominators after seeing a favorable result.

Collection is only a future proposal in [TELEMETRY_PURPOSE_REGISTER](TELEMETRY_PURPOSE_REGISTER.md); current runtime does not collect research/analytics data. E0–E3 and E5 remain unsatisfied by this framework. Automated verification can support a particular E4 claim, never all product gates.
