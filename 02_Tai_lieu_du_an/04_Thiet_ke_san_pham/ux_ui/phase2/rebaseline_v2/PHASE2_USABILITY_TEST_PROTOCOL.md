# Qualitative usability protocol — E1 HUMAN VALIDATION PENDING

Updated 2026-10-02. **NOT RUN**: no participant attendance, consent, quotes, task results or real TalkBack outcomes are supplied. This is the Day 0 first-use/core-loop protocol for the [five-person pilot](PHASE2_DIARY_PILOT_PLAN.md). Phase 3 HOLD. Fixture usability review may be scheduled with human approval; natural-use/learning research has additional readiness gates.

Question: can a real person find an appropriate next learning action, answer, interpret support/feedback/result, leave safely and recover without developer help? This tests E1 interaction, not E0 prevalence, E2 efficacy or E3 retention. Approximately five adults with relevant recent circumstances may reveal qualitative issues; they are not representative, statistically powered, guaranteed to find every problem, or synthetic users. Candidate recruitment and interview script: [discovery pack](INITIAL_WEDGE_RESEARCH_PLAN.md). Target user remains unfrozen.

## Before a session

Record actual build/commit, device/OS, screen/text/motion settings, content revision and moderator. Explain that Phase 2 sample states do not provide real accounts, accepted scoring, publication, durable sync or proven learning. Planned errors/offline/partial-sync views are scenarios, not a demonstration of a production runtime. Do not use real learner records or credentials. Do not describe the expected control or praise the candidate before the task.

Obtain separate consent for participation, optional recording and anonymized quotes; declining recording does not prevent participation. Explain voluntary stop/withdrawal/redaction, contact, access and retention. Organizer must approve the research privacy procedure before recruitment. Proposed recording ceiling is 30 days after the approved review window, subject to that approval and applicable requirements; it is not an implemented retention guarantee. Keep coded IDs and consent/contact separate, minimize free text, restrict storage/access and record actual deletion. No recruitment or message was sent by this task.

Session plan 40–50 minutes, adjusted for accessibility/fatigue: consent/context; first-use and core tasks; selected recovery tasks; debrief. Study-session length is not a learner lesson-duration target. Moderator: “Hãy nói bạn đang tìm gì và bạn nghĩ điều gì sẽ xảy ra.” Observe silently first; record an attempted path before a neutral prompt. If the moderator provides help, mark assisted completion. Let participants stop rather than force every task.

## Neutral tasks and observations

Present the scenario without pointing at a button. Wrong-answer/recovery probes can be introduced after the initial natural path; label them deliberate probes so they do not distort spontaneous-success counts.

| Task/scenario | Observe and ask for readback |
|---|---|
| Open Mingo and begin a useful first learning action | First click, hesitation, Home hierarchy and approximate time; does setup appear optional? |
| Choose a goal if useful, then find how to change it | Optional/reversible choice, terminology and navigation; not demographic/learning-style classification |
| See a suggested action and inspect its explanation | Can the participant explain RESUME/DUE_REVIEW/path/goal/fallback without “AI knows me” inference? |
| Work through Home → Lesson → Answer → Feedback → Result | Can the user answer/submit, understand state and decide a next action? Note Android system back, unintended taps and reading burden |
| After a deliberate wrong answer, use permitted support/retry | Distinguish first wrong unaided response from assisted correction; does feedback explain why without pressure? |
| Reach Check; leave if desired | Understand no hint/retry/skip in current Check; exit is not falsely marked complete |
| Interpret result, progress and course preview | Sessions/practice/evidence vs mastery; preview vs eligibility; what has and has not been demonstrated? |
| Resume a sample unfinished session | Expected position and preserved conditions; recognizes sample state boundary |
| Find an available downloaded lesson under a stated offline scenario | Ready asset vs missing media; local saved vs server accepted |
| Inspect partial sync, delayed acknowledgement or changed revision | Explain safe next action, pending/rejected state and pinned revision; no false “synced” conclusion |
| Recover from unavailable listening audio and an empty/error screen | Technical failure vs knowledge failure; can recovery be found without guessing an answer? |
| Use large text/reduced motion and back navigation | No lost critical action/content, focus confusion or decorative obstacle; note participant-specific access needs |

A separate small **staff task cohort**, if recruited, uses sample learner lookup → evidence/source/time → draft/revision/license/publishing status. Do not grow analytics/intervention/admin intelligence scope. Record real role familiarity and authorization assumptions; fixture role controls are not Auth/AuthZ.

## Real accessibility session — required human gate

A real tester uses TalkBack on Android through the full Home → Lesson → Answer → Feedback → Result journey, navigation/back, errors and offline states. Record device/OS/TalkBack version, actual traversal, labels, focus return, announcements, non-color state and any help. Include a tester familiar with the assistive technology where feasible. Staff web keyboard/focus review is separate. Automated semantics/contrast/48dp/200%/reduced-motion checks support technical evidence but do not sign this human gate. If no real test is conducted: **PENDING**, never PASS from a screenshot or semantics tree.

## Observation and analysis form

Blank fields: `participant_code | consent_ref | task/scenario_ID | build/device/settings | intended_goal | start/end (quality noted) | first_click | expectation | actual_path | wrong_taps/errors/hesitation | participant_readback | completion {unassisted, assisted, failed, not_attempted} | moderator_prompt | exact_optional_quote | context/technical_issue | severity | interpretation/alternative_explanation | proposed_correction | retest_owner | evidence_ref`.

Severity: P0 = data/permission/status integrity claim or potential loss; P1 = core task blocked or materially misleading; P2 = friction/misunderstanding; P3 = cosmetic issue. This is triage, not proof that the runtime has a reproduced P0 defect. Keep observations distinct from researcher interpretations. Preserve counterexamples and a single serious accessibility failure even if other participants succeed.

Debrief: What would you do next? What did the result mean? Which suggestion did you trust and why? What is stored here versus confirmed by the system? What was unclear or felt like pressure? What would you remove? How would this fit the recent circumstance you described? Ask effort/helpfulness only as optional reported perception, not a validated mental-state score. Describe mascot/tone without a leading “cute/calm” question.

Report actual attendance, task counts/denominators, assisted vs unassisted, unavailable/not attempted cases, evidence references and limitations. Do not convert five ratings or many clicks into population percentages. Prioritize issues, revise, and retest fresh tasks/paths with real people. Automated/golden evidence and human art-direction approval remain separate layers. No product gate is closed by this prepared protocol.
