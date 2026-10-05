# Adaptation principles — heuristic first, action first

Updated 2026-10-02. Conceptual product rules and future evaluation gates; no new recommendation service, feature store, model, schema or production collection. Phase 3 HOLD. Current fixture predicates remain unchanged. Human/product effectiveness is PENDING.

Adaptation should improve meaningful learning, comprehension, appropriate challenge, autonomy and task success while limiting unnecessary time, privacy cost and technical friction. The directive's conceptual objective is not a numerical loss function. Evidence and limitations: [RE01–RE17, RE27–RE30](MINGO_RESEARCH_EVIDENCE_REGISTER.md). The [learning experience model](LEARNING_EXPERIENCE_MODEL.md) keeps Knowledge, Experience and Context separate.

## Decision boundaries

| Adaptable dimension | Legitimate inputs | Required boundary |
|---|---|---|
| What next | Unfinished eligible session, due review, curriculum position, declared goal, content availability | Server permissions/eligibility and exact pinned revisions remain authoritative |
| Difficulty | Repeated fresh independent evidence, task demands, misconception and context | No strong change from a single answer, latency, skip or replay; no automatic level/mastery/unlock |
| Support level | Observed task difficulty and support already used | Scaffold → Observe → Fade; retain first answer and assistance; later independence needs fresh evidence |
| Review timing | Valid prior evidence and a versioned scheduling policy | No universal optimal gap or schedule inferred from five users; event time and known-at time distinct |
| Modality | Objective/task requirement, accessibility need, explicit preference, available media | No visual/auditory/kinesthetic learner labels; modality preference is not a permanent ability type |

Positive listening observations do not justify listening forever. Preserve curriculum coverage and opportunities to transfer to other relevant contexts. Exploitation of known useful practice should be balanced with bounded exploration of eligible tasks. Exploration must remain optional where promised, understandable, accessible and reversible; it must not expose unpublished or inaccessible content.

## Explainable recommendation V1

Candidate Home priority: **unfinished session > due review > next curriculum item > goal-compatible item > fallback**. It must work when ML and risk input are disabled. Evaluate only eligible, licensed/published and available content under V3.2 permissions/revisions; if the first candidate is unavailable, choose an eligible alternative and state the actual reason. Do not fabricate a personalized diagnosis to justify a fallback.

| Human reason code | Example explanation | Evidence required |
|---|---|---|
| RESUME | “Bạn có một bài đang học dở.” | Resumable accepted/local attempt state with truthful acknowledgement status |
| DUE_REVIEW | “Ôn lại nội dung đã học khi đến lịch.” | Due status from a defined schedule and the relevant evidence available at decision time |
| NEXT_IN_PATH | “Tiếp tục nội dung tiếp theo trong lộ trình.” | Authoritative eligibility and curriculum position |
| GOAL_MATCH | “Bài này phù hợp với mục tiêu bạn đã chọn.” | Explicit goal, eligible content mapping; no hidden psychological label |
| FALLBACK | “Bắt đầu một bài phù hợp đang có sẵn.” | Eligible available option when other candidates are absent or uncertain |

These outer-loop reasons do not replace the existing inner lesson/feed reason codes in [ADAPTIVE_FEED_MVP_SPEC](../../../learning_design/ADAPTIVE_FEED_MVP_SPEC.md). Existing bounded challenge preview still requires two distinct unaided first responses, including Check, in the same objective/band. That exact predicate stays unchanged in this task; its threshold is provisional and requires validation. Preview does not imply entitlement, mastery, publication or progression.

Before later runtime changes, record policy version, inputs actually available, chosen/rejected candidates with minimal reason metadata, fallback and user override. Recommendation explanation must faithfully describe the decision; more persuasive copy is not evidence of a better decision. “AI understands you” is not an acceptable claim.

## Uncertainty, autonomy and safety

For an ambiguous observation, seek context or repeated relevant evidence before strong adaptation. For example, a replay can indicate careful listening, inaccessible audio, interruption or difficulty. A skip may be a choice, limited time, an unavailable task or unfamiliar terminology. Preserve a simple default path when evidence is missing. Allow the learner to decline a recommendation and choose another eligible task. Changes must be reversible and not punish non-return, offline use or use of support.

Use calm, task-specific feedback rather than ego labels, casino effects or streak threats. Habit cues may be optional aids, never the primary optimization objective. Accessibility settings are accommodation inputs, not labels for model segmentation or health inference.

## Future early intervention — define an action before prediction

The following are **proposed action hypotheses**, not runtime or validated risk rules. A useful decision needs an available actor and safe action. Without an actionable path, there is no reason to introduce a prediction model.

| Undesired state | Detectable evidence and uncertainty | Decision window | Actor | Possible action | Expected outcome hypothesis | Measurement and burden |
|---|---|---|---|---|---|---|
| An intended review remains unfinished | Due item and unfinished attempt; server silence may be offline/late capture | At next voluntary opening; no inferred emergency | Learner; staff only within authorized role | Offer resume or smaller eligible review; let learner dismiss | Lower friction and useful independent recall | Acceptance vs dismissal, completed task, fresh delayed check; minimal prompt, no coercive notification |
| Repeated fresh errors on one objective | Distinct first answers, conditions/assistance and content validity; not same-stem retries | Next eligible practice after content/technical causes considered | Learner; authorized content reviewer for suspect items | Minimal cue, worked contrast, later independent task; flag ambiguous content for review | Misconception resolves with less support | Fresh task success, assistance trajectory, misconception evidence; no “weak learner” label |
| Media failure prevents an activity | Asset availability/playback error and interruption context | Immediately at error/recovery | Learner and technical support if requested | Retry/download or offer an eligible alternative; keep assessment unavailable if necessary | Task resumes without false completion | Recovery success, lost-data incidents, accessibility; classify as technical friction, not knowledge risk |

Separate **Prediction → Recommendation Decision → Exposure → Execution → Outcome**. A model score is not an exposure; seeing a suggestion is not carrying it out; carrying it out is not a learning gain. Compare useful outcomes, learner burden and unintended harms against a simple rule baseline. Risk remains an optional recommendation input, distinct from mastery.

## Future intelligence lifecycle — gate sequence

**RULE BASELINE → PRODUCT TELEMETRY → LABEL DEFINITION → POINT-IN-TIME DATASET → TRAIN PAST → TEST FUTURE → CALIBRATION → SUBGROUP ANALYSIS → SHADOW MODE → LIMITED EXPOSURE → INTERVENTION OUTCOME → PRODUCTION**.

| Stage | Evidence required before moving forward |
|---|---|
| Rule baseline | Versioned simple decision policy, safe default, action and outcome definition, coverage/eligibility tests |
| Product telemetry | Approved purpose/minimization/consent, reliable capture, separate command queue and telemetry queue, missingness audit |
| Label definition | Valid learning/undesired-state label, horizon, censoring, authority, actionability; completion cannot become mastery by convenience |
| Point-in-time dataset | Event time, availability/knowledge time and source capture; exclude future information and labels from features; revision-aware provenance |
| Train past / test future | Temporal split, learner/item leakage control, realistic available data and rule comparison; document cohort shift |
| Calibration / subgroups | Reliability and uncertainty at the intended horizon; errors/coverage across relevant consented cohorts without collecting sensitive data just for segmentation |
| Shadow mode | No learner exposure or autonomous action; compare decisions, capture serving differences and monitor drift |
| Limited exposure | Approved human/ethical/product protocol, bounded reversible exposure, opt-out and fallback; define stop conditions before launch |
| Intervention outcome | Measure learning/task outcomes, burden and harms separately from model accuracy and click acceptance |
| Production | Operational, security, privacy, content and human gates satisfied; documented rollback, monitoring and accountability |

No stage is satisfied by this Phase 2 document. OULAD and UCI are **research baselines only**, with different populations/tasks and capture granularity; they cannot establish Mingo production effectiveness or labels. The product continues to function when ML/recommendation is disabled.

## Future speech/audio privacy — not implemented

Prefer on-device processing when reasonable for the task and hardware; verify its actual behavior and access requirements. Before any server upload, define an explicit recording/upload action, purpose, minimum necessary data, retention deadline, deletion behavior, encryption/access, consent/disclosure, and account lifecycle treatment. Playback/replay of supplied audio does not authorize microphone collection. A participant must be able to decline optional recording and still use an appropriate alternative. No raw voice recording, speaking score, transcript upload or biometric inference is implemented by this task. Review privacy and retention before a future pilot; [RE26](MINGO_RESEARCH_EVIDENCE_REGISTER.md) is a design framework, not jurisdiction-specific legal certification.

## Future production-readiness template — NOT READY

Use this compact template at the future deployment gate; fill evidence and owner before release. No production deployment is authorized here.

| Readiness area | Required review artifact | Owner / target / evidence |
|---|---|---|
| SLO, availability, latency | Defined user journeys, measurement windows, error/latency budgets and failure policy | PENDING |
| Monitoring and alerting | Actionable signals, dashboard/source, on-call routing and tested alert response | PENDING |
| Capacity and dependencies | Tested workload/limits, storage/worker capacity, dependency/version inventory | PENDING |
| Backup and restore | Scope/retention, RPO/RTO approved, actual restore drill and evidence | PENDING |
| Rollback | Reversible code/config/content release procedure and tested recovery boundary | PENDING |
| Incident response | Responsibilities, escalation, communications and recovery exercise | PENDING |
| Security and privacy | Authorization, threat model, secrets, retention/deletion and account lifecycle review | PENDING |

These are future operational acceptance areas, not new services or an assertion that Phase 1 foundation is production-ready.
