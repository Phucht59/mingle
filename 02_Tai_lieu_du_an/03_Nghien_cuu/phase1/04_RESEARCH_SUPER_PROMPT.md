# SUPER PROMPT — Phase 1 Scientific Resolution of Learner Evidence Model

You are acting as a combined:
- learning-science researcher,
- second-language acquisition researcher,
- educational measurement specialist,
- adaptive-learning systems designer,
- mobile consumer-product researcher,
- product manager for an evidence-driven EdTech product.

Your task is NOT to brainstorm casually and NOT to ask the user to make all 18 product decisions from personal preference.

Your task is to independently research, compare evidence, and recommend the strongest defensible MVP policy for each of the 18 pending decisions in `03_RESEARCH_QUESTIONS_18.md`.

## Files you must read first

1. `01_MASTER_MEMORY_TRANSFER.md`
2. `02_ADAPTIVE_PROJECT_CONTEXT.md`
3. `03_RESEARCH_QUESTIONS_18.md`
4. `05_EXPECTED_OUTPUT_STRUCTURE.md`

Use the master memory only as project/user context. For this task, prioritize the Adaptive Language Learning sections and the latest dated decisions.

## Project invariants

Treat these as frozen unless your research reveals a concrete blocking contradiction:

- V3.2 is the implementation source of truth.
- Phase 0 is DONE.
- Phase 1 is ACTIVE.
- Flutter Android-first learner app.
- Flutter Web staff/admin.
- FastAPI/Python.
- PostgreSQL.
- Modular monolith.
- API + durable worker in the same codebase.
- Server authoritative for canonical scoring/progress/permissions.
- Commands separate from telemetry.
- Offline durable queues.
- Content immutable/versioned.
- Exact revisions pinned to attempts/enrollments.
- Mastery != Risk.
- Risk is optional for recommendation.
- Recommendation must have deterministic fallback when ML is unavailable.
- Product must function without production ML.
- Do not add Kafka/Kubernetes/microservices/warehouse/external feature store without a real requirement.

If your recommendation would require changing a frozen V3.2 business rule, DO NOT silently redefine it.
Create an explicit:
`IMPLEMENTATION ISSUE / CHANGE REQUEST`
with:
- conflict,
- evidence,
- why current baseline blocks the recommended behavior,
- minimal proposed change,
- impact,
- whether it is blocking or deferrable.

## Core product hypothesis

The product is an adaptive English-learning companion.

It should learn from the learner's behavior and performance over time, understand their current state, and help choose what they should study or review next.

MVP learning areas:
- Vocabulary
- Grammar
- Listening

Not MVP:
- Speaking
- unrestricted AI conversation
- large social features

Proficiency:
A0 → A1 → A2 → B1 → B2

TOEIC and other goals may map onto the learner profile, but should not replace the internal proficiency/curriculum structure.

Pilot:
~5 users.

Therefore:
- optimize pilot for qualitative validation, behavioral correctness, telemetry quality and technical reliability;
- do NOT claim efficacy from 5 users.

Commercialization:
- pilot/development free-first;
- preserve future Free/Premium capability;
- do not optimize the learning methodology around monetization.

## Learning experience already accepted

Core interaction model:
`Adaptive Learning Feed`

Default session/cycle:
approximately 5 minutes.

Important:
5 minutes is a consumer-experience constraint/hypothesis, NOT a claim that exactly five minutes is pedagogically optimal.

The product must combine:

### Consumer experience layer
- low-friction entry
- short interactions
- immediate feedback
- modality variation
- high relevance
- personalization
- smooth continuation
- modern mobile content-consumption expectations

WITH

### Learning-science layer
- clear objectives
- retrieval practice
- spacing
- feedback
- prerequisite structure
- appropriate cognitive load
- contextualization
- transfer
- delayed reassessment
- progressive difficulty

Already accepted cycle functions:
1. Review
2. Learn
3. Retrieve
4. Transfer
5. Check

Already accepted:
- finite cycle
- explicit endpoint
- no infinite doomscroll
- explicit user choice to continue
- skip is logged evidence, not mastery
- attempt-first when appropriate, but not dogmatically
- curriculum controls what is valid to learn
- personalization cannot arbitrarily violate prerequisites
- initial scheduler should be explainable/rule-based before ML
- every selected item should ideally carry a selection reason

Candidate selection reasons already discussed:
- DUE_REVIEW
- RECENT_ERROR
- PREREQUISITE_GAP
- CURRENT_OBJECTIVE
- MODALITY_TRANSFER
- CHALLENGE

These are not immutable taxonomy names, but preserve the conceptual distinction unless evidence supports a better scheme.

## Research requirement

You MUST browse current external sources.

Do not answer the 18 questions only from model memory.

Use a research hierarchy.

Prefer:
1. systematic reviews / meta-analyses;
2. peer-reviewed primary studies;
3. reputable educational measurement / SLA references;
4. official product experiments only for product-behavior evidence;
5. current consumer/mobile research from reputable research firms;
6. practitioner articles only as secondary context.

For each important claim, distinguish:
- strong evidence,
- moderate evidence,
- limited/mixed evidence,
- product hypothesis.

Do NOT write "scientifically proven" unless evidence genuinely supports that level of certainty.

Separate:
- evidence about learning effectiveness,
- evidence about engagement/consumer behavior,
- evidence about UX,
- product inference.

A design that increases engagement is NOT automatically a better learning design.

A design that works in general education is NOT automatically validated for adult Vietnamese English learners.

Explicitly note transfer limitations.

## Areas you should research

At minimum search across:

### Learning science
- retrieval practice / testing effect
- spacing / distributed practice
- feedback timing
- worked examples / guidance fading
- desirable difficulties
- interleaving where relevant
- segmentation / cognitive load
- mastery learning
- delayed retention
- metacognition / confidence calibration

### Second-language acquisition
- L2 vocabulary learning
- contextualized vocabulary vs isolated translation
- receptive vs productive knowledge
- form-meaning mapping
- grammar instruction
- explicit vs implicit/form-focused instruction
- listening comprehension
- replay/repetition
- glosses/hints/scaffolding
- beginner learners

### Educational measurement
- response time as evidence
- speed-accuracy tradeoff
- attempt history
- partial evidence
- hint use
- confidence
- formative vs summative assessment
- placement testing
- adaptive testing
- measurement uncertainty
- avoiding false precision

### Adaptive systems
- learner models
- explainable recommendations
- human control / learner agency
- prerequisite constraints
- remediation scheduling
- rule-based adaptive sequencing
- knowledge tracing only as future context, NOT mandatory for MVP

### Motivation/product behavior
- streaks
- goals
- gamification
- intrinsic/extrinsic motivation
- self-determination theory
- progress feedback
- habit formation
- reward misuse
- user autonomy

### Consumer behavior
Use current evidence only to shape:
- interaction length,
- friction,
- content presentation,
- continuation mechanics,
- expectations of personalization.

Do NOT infer pedagogy directly from social-media engagement.

## The 18 questions

Resolve every question in `03_RESEARCH_QUESTIONS_18.md`.

Do not merely present options.

For EACH question, provide a default recommendation.

Use this structure:

### Q[number]. [name]

**Recommended MVP policy**
One concrete recommendation.

**Why**
Concise reasoning.

**Evidence**
What research supports it.
Cite sources.

**Evidence strength**
Strong / Moderate / Limited / Product hypothesis.

**Implementation rule**
Write the behavior as a product/system rule precise enough to become a PRD requirement.

**Evidence/telemetry to store**
Only fields that materially support learner modeling or product evaluation.
Do not collect data merely because it is available.

**What NOT to infer**
Explicitly list dangerous interpretations.
Example:
"response time must not be interpreted as intelligence."

**Later-phase option**
What could become more sophisticated after real product data exists.

## Important design principle: Observable evidence first

Prefer storing objective observations rather than inventing psychological explanations.

Example:

Prefer:
- first answer incorrect,
- 2 retries,
- hint used,
- 18.4s response time,
- correct after feedback,
- failed again 3 days later

over:
- "learner was distracted"
- "learner lacks motivation"
- "learner has low ability"

unless such a construct is directly measured and validated.

Do not infer unobservable learner states from one interaction.

## Learner Evidence Model deliverable

After resolving all 18 questions, synthesize a proposed MVP Learner Evidence Model.

Separate at least:

### A. Raw observable interaction evidence
Examples:
- correctness
- first-attempt correctness
- response latency
- retry count
- hint type/use
- replay count
- skip
- content revision
- item/objective
- modality
- event time
- server/knowledge availability timestamps where relevant

### B. Derived short-term signals
Examples only if justified:
- repeated error
- due review
- weak evidence
- recent success pattern

### C. Curriculum state
- objective
- prerequisite state
- allowed next objectives

### D. User preference / intent
- chosen focus
- stated goal
- daily target

Keep preference distinct from competence.

### E. Engagement state
- streak
- target completion
- reward progress

Keep engagement distinct from mastery/proficiency.

### F. Future intelligence state
Explicitly mark what should NOT yet be frozen:
- final mastery formula
- knowledge tracing model
- production risk model
- production recommendation weights
- final adaptive-path model

## Scheduler deliverable

Produce an MVP scheduler policy using the research conclusions.

It should answer:

1. What candidates are eligible?
2. What is filtered out by level/prerequisites?
3. How are due review, recent errors, current objective, transfer and challenge balanced?
4. How are user-selected focus/preferences respected?
5. When is difficulty raised?
6. When is remediation inserted?
7. How is session completion determined?
8. How is a ~5-minute cycle constructed without hard-cutting an incomplete learning loop?
9. What selection reason is logged for each item?
10. What deterministic fallback exists if intelligence/ML is unavailable?

Do NOT invent a complex mastery formula unless evidence and the current phase justify one.

## Placement deliverable

Propose an onboarding/placement policy for A0–B2 with Vocabulary + Grammar + Listening.

Constraints:
- mobile
- low friction
- do not require a 30–40 minute mandatory test
- allow uncertainty
- placement can continue to calibrate after onboarding
- do not produce fake precision

Specify:
- what is tested initially,
- approximate experience structure,
- whether it is adaptive,
- what can be skipped,
- how confidence/uncertainty is represented,
- how later evidence can update placement.

## Reward/streak deliverable

Design a minimal MVP engagement system grounded in motivation research.

Specify:
- streak condition,
- daily target behavior,
- rewards,
- what rewards do NOT affect,
- anti-gaming rules,
- what metrics remain separate from learning progress.

## User-facing learner model deliverable

Propose how to make "the system understands me" visible.

Avoid fake precision.

Examples may include:
- qualitative states,
- evidence-backed insights,
- recent patterns,
- explanation of recommended review,
- confidence/uncertainty.

Specify what the user sees and what remains internal.

## Data minimization / privacy

For every telemetry recommendation:
ask:
"Does the product need this signal to improve learning, reliability, or evaluation?"

If no:
do not store it by default.

Do not recommend intrusive sensor/behavioral collection.

## Pilot constraint

Because the pilot is ~5 users:
do not propose statistical claims that require large samples.

Define what can be evaluated with 5 users:
- comprehension/usability,
- friction,
- obvious scheduler errors,
- telemetry correctness,
- content difficulty mismatch,
- qualitative trust,
- perceived personalization,
- offline/sync reliability,
- session completion behavior.

Define what cannot be established:
- population efficacy,
- causal learning gains,
- stable ML weights,
- validated mastery thresholds,
- robust segmentation.

## Decision classification

At the end, classify each of the 18 decisions as one of:

- FREEZE NOW — enough evidence + compatible with Phase 1
- MVP HYPOTHESIS — implement a default but validate in pilot
- DEFER — should not be locked until later learning-intelligence/product data
- CHANGE REQUEST — conflicts with V3.2 / existing frozen rule

## Phase impact

After analysis, state whether the conclusions affect:

- Product Charter
- MVP PRD
- Learner Evidence Model
- Adaptive Feed specification
- telemetry contract
- content authoring requirements
- UX requirements
- Phase 1 acceptance criteria
- later Phase 9 Learning Intelligence

Do NOT declare Phase 1 complete just because this research is complete.

## Final result required

The final answer must contain:

1. Executive conclusion.
2. Evidence framework and caveats.
3. 18 question-by-question recommendations.
4. Final Learner Evidence Model.
5. Final MVP scheduler behavior.
6. Placement policy.
7. Streak/target/reward policy.
8. User-facing learner-profile policy.
9. Minimal telemetry schema recommendations.
10. Five-user pilot validation plan.
11. Decision register: FREEZE / HYPOTHESIS / DEFER / CHANGE REQUEST.
12. Any Implementation Issues / Change Requests.
13. Updated Phase 1 status: DONE / ACTIVE / BLOCKED / DEFERRED.
14. Explicit list of decisions that should be written into the Product Charter/MVP PRD.
15. Sources/bibliography with links and dates.

## Interaction rule

Do the research first.

Do NOT start by asking the user to choose among the 18 questions.

Only ask the user for a decision when:
- evidence genuinely cannot distinguish between alternatives,
- the choice is inherently business/brand preference,
- or V3.2 creates a product tradeoff requiring owner approval.

Even then:
- first give the evidence-based default,
- explain the tradeoff,
- then identify exactly what owner decision remains.

## Quality gate

FAIL the research if:
- it simply mirrors the user's preferences,
- it uses engagement evidence as proof of learning effectiveness,
- it presents one paper as universal proof,
- it hides uncertainty,
- it invents a mastery formula prematurely,
- it redesigns V3.2 silently,
- it recommends excessive telemetry,
- it treats a five-user pilot as efficacy validation,
- it gives 18 menus of choices instead of recommendations.

PASS only if the result is sufficiently concrete that the project owner can review recommendations and approve/reject them, rather than designing the methodology from scratch himself.
