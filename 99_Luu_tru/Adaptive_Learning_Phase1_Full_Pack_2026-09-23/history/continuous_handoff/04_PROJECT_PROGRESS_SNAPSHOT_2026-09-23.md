# PROJECT PROGRESS SNAPSHOT
## Adaptive Language Learning & Early Intervention Platform
### Snapshot: 23 September 2026

## 1. Current truth

### Phase 0 — Architecture & Contract Baseline
**DONE**

Architecture baseline:
- V3.2 is the source of truth for implementation.
- Baseline assessment: ~9/10.
- 115 contract checks passed.
- 22 SQL checks passed.
- V3.2 is a specification + verification baseline, not a completed app.
- Do not reopen architecture generally.
- Reopen only for a concrete blocking defect found during implementation.
- Foundational changes require an Implementation Issue / Change Request.

### Phase 1 — Implementation Foundation / Product Build Kickoff
**ACTIVE**

The scientific resolution of the 18 Learner Evidence / Adaptive Feed decisions is now complete and should be used as the current working methodology baseline.

Phase 1 is **not DONE** because official Phase 1 product/foundation artifacts and implementation gate evidence remain incomplete.

---

## 2. Latest owner instruction

The owner explicitly instructed that the completed research result should be read, integrated into the handoff, and that a fresh account should receive enough context to **continue the project immediately rather than restarting discovery**.

Operational consequence:
- do not rerun the 18-question research by default;
- do not ask the owner those 18 questions again;
- incorporate research conclusions into the Product Charter, MVP PRD, Learner Evidence Model and Adaptive Feed specification;
- continue remaining Phase 1 foundation work.

---

## 3. Frozen architecture / stack baseline

### Client
- Flutter learner client.
- Android-first.
- Flutter Web staff/admin.
- iOS compatibility retained; public release later.

### Backend / data
- FastAPI / Python.
- PostgreSQL.
- Object Storage.
- Modular monolith.
- API process + durable worker process from the same codebase.

### Core invariants
- Server authoritative for scoring, progress, permissions and canonical state.
- Command separated from telemetry.
- Offline durable command queue + telemetry queue.
- Published content immutable/versioned.
- Enrollment/attempt/scoring pin exact revisions where required.
- Analytics uses event time + knowledge/availability time + source capture.
- Mastery != Risk.
- Risk is optional input to recommendation.
- Prediction / Recommendation Decision / Exposure / Execution / Outcome are separate layers.
- Product works if ML/recommendation is disabled.
- No premature Kafka/Kubernetes/microservices/warehouse/external feature store.

---

## 4. Product direction currently established

### Target
Learners who:
- are beginners or lost their English foundation;
- study but feel ineffective;
- forget vocabulary;
- do not know their current level;
- do not know what to study/review next.

### Internal progression
A0 (internal / Pre-A1-like) → A1 → A2 → B1 → B2.

External goals such as TOEIC may map to learner goals, but do not replace internal progression.

### MVP learning scope
- Vocabulary.
- Grammar.
- Listening.

Deferred:
- Speaking.
- unrestricted AI conversation.
- broad social features.

### Pilot
~5 users due limited resources.

Pilot is for:
- usability;
- technical correctness;
- scheduler obvious failures;
- content mismatch;
- telemetry quality;
- trust/perceived personalization;
- offline/sync reliability.

It is NOT enough to claim:
- population learning efficacy;
- causal gain;
- validated mastery thresholds;
- production ML weights.

### Commercial direction
- free-first during development/pilot;
- preserve future Free/Premium path.

### Product name
NOT frozen.
“Mingo” appearing in research is a temporary working label only.

---

## 5. Adaptive Learning Feed baseline

Default learning cycle:
- approximately 5 minutes;
- finite;
- objective-bounded;
- explicit endpoint;
- user explicitly chooses to continue;
- NOT infinite scroll.

Five functional roles:
1. Review
2. Learn
3. Retrieve
4. Transfer
5. Check

Important:
5 minutes is primarily a product/consumption hypothesis and low-friction unit, not a scientific claim that exactly 5 minutes is pedagogically optimal.

Consumer-experience mechanics may optimize:
- low-friction start;
- short interactions;
- varied modality;
- immediate feedback;
- relevance;
- personalization;
- smooth continuation.

Pedagogy remains controlled by:
- curriculum;
- prerequisites;
- retrieval;
- spacing;
- feedback;
- cognitive-load management;
- contextualization;
- transfer;
- delayed reassessment;
- progressive difficulty.

---

## 6. Scientific Phase 1 resolution — current working baseline

The full result is in:
`03_PHASE1_SCIENTIFIC_RESEARCH_RESOLUTION.md`

Research acceptance:
- 18/18 questions resolved with a recommended default.
- Evidence strength separated from product hypothesis.
- Learner Evidence Model proposed.
- Scheduler policy proposed.
- Placement policy proposed.
- Motivation/reward policy proposed.
- User-facing learner profile proposed.
- Minimal telemetry proposed.
- 5-user pilot validation plan proposed.
- Research gate: PASS WITH LIMITS.

Working interpretation:
- `FREEZE NOW` = incorporate the principle/guardrail into Phase 1 official artifacts.
- `MVP HYPOTHESIS` = implement only as versioned/configurable default where appropriate; validate in pilot.
- `DEFER` = do not freeze before later learning-intelligence work.
- `CHANGE REQUEST` = only when a real V3.2 conflict is proven.

---

## 7. Research decisions summarized

### FREEZE NOW principles
- observable error evidence; no single-click psychological cause;
- response time not used as mastery/ability in MVP;
- assisted success distinct from unassisted success;
- explicit skip is not mastery;
- vocabulary uses meaning/audio/context + multiple retrieval forms;
- learner profile qualitative/evidence-backed; no fake mastery %.

### MVP HYPOTHESES
- one immediate retry in practice;
- unlimited practice listening replay / fixed Check replay policy;
- hybrid grammar sequence;
- within-objective difficulty progression;
- bounded review/prerequisite insertion vs user-selected focus;
- short provisional placement across Vocabulary/Grammar/Listening;
- optional learning goal;
- one ~5-minute default daily cycle;
- retrieval-based streak separate from daily target;
- progress/milestone rewards rather than XP farming;
- browse/review/preview course map under prerequisite constraints;
- concise verifiable recommendation explanations.

### DEFER
- causal error classifier;
- response latency → ability;
- psychometric replay parameters;
- final mastery thresholds;
- validated statistical CAT / CEFR certification;
- reward optimization;
- final XAI/model explanations;
- final knowledge tracing / adaptive-path optimizer / production risk/recommendation weights.

---

## 8. Learner Evidence Model direction

Keep distinct:

A. Raw observable evidence
- item/objective/content revision;
- modality;
- task mode;
- first response/correctness;
- retry;
- hint;
- replay;
- skip;
- active duration with measurement quality;
- event/known/received time;
- provenance.

B. Short-term derived signals
- due review;
- recent/repeated error;
- assisted success;
- insufficient evidence;
- recent unassisted success.

C. Curriculum state
- objective;
- skill dimension;
- prerequisite;
- eligibility/preview/review state.

D. User intent/preferences
- focus;
- stated goal;
- daily target;
- accessibility/override.

E. Engagement
- cycle completion;
- streak;
- reward.

F. Deferred intelligence
- mastery formula;
- knowledge tracing;
- production risk labels;
- recommendation weights;
- final adaptive paths;
- CEFR cut scores.

Preference must remain distinct from competence.
Engagement must remain distinct from mastery.

---

## 9. Known implementation issue

### II-01 — Exact V3.2 source verification
Status: **BLOCKING only for contract-level implementation**

The current handoff contains V3.2 context, but not the exact original V3.2 package.

Before writing implementation that depends on:
- exact schema;
- command/telemetry contract;
- SQL;
- OpenAPI;
- scoring;
- worker behavior;
- field names;
- exact business invariants;

the new account must inspect the exact V3.2 source files.

Do NOT create a Change Request merely because the package is absent.
First obtain/inspect it and prove a real conflict.

---

## 10. Phase 1 work remaining

### Product/foundation artifacts
- Product Charter — integrate latest research and freeze.
- MVP PRD — integrate testable research policies.
- Learner Evidence Model specification.
- Adaptive Learning Feed / Scheduler MVP specification.
- Placement/engagement/profile requirements.
- Implementation roadmap.
- Prioritized backlog.
- Repo/module structure.
- Environment strategy.
- configuration/secrets conventions.
- DB/migration bootstrap strategy.
- CI/CD baseline.
- test strategy.
- coding standards.
- Definition of Done.
- Implementation Issue / Change Request workflow.
- Phase 1 acceptance checklist.
- final Phase 1 progress snapshot.

### Implementation evidence
Where possible after exact V3.2/repo is available:
- bootstrap repository/runtime;
- run contract/SQL checks;
- establish CI baseline;
- prove minimal project boot/test path.

---

## 11. Status register

### DONE
- Phase 0 baseline.
- product direction discovery sufficient for Phase 1.
- Adaptive Learning Feed philosophy.
- scientific research Q1–Q18.
- research synthesis and decision classification.

### ACTIVE
- Phase 1 official artifact integration.
- engineering foundation planning/setup.
- Phase 1 gate preparation.

### BLOCKED
- exact contract-level implementation only, until exact V3.2 source package is available.

### DEFERRED
- Phase 2+ work until Phase 1 gate.
- final mastery/knowledge tracing/risk/recommendation weights.
- speaking/conversation.
- production efficacy claims.

---

## 12. Immediate next action

The next account should NOT ask what to do.

It should immediately:

1. read the full research resolution;
2. produce/update the official Phase 1:
   - Product Charter;
   - MVP PRD;
   - Learner Evidence Model;
   - Adaptive Learning Feed / Scheduler spec;
3. reconcile each research rule against exact V3.2 if the exact package is supplied;
4. continue remaining engineering-foundation artifacts;
5. assemble the Phase 1 acceptance gate;
6. only move beyond Phase 1 when that gate actually passes.

