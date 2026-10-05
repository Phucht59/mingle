# Super Prompt — Continue This Project in Another Chat

You are continuing the project **Adaptive Language Learning & Early Intervention Platform**, evolved from Trần Hoàng Phúc's KLTN.

Treat the following as project memory and operating rules.

## Baseline

- Architecture/contract baseline is **V3.2**.
- V3.2 is the implementation source of truth.
- Recorded validation: 115 contract checks + 22 SQL checks passed.
- Baseline was assessed 9/10 and is sufficient to implement.
- V3.2 is specification + verification code, not a complete application.
- Do not reopen general architecture review unless implementation uncovers a specific blocking defect.
- Any foundational change must be documented as an Implementation Issue / Change Request. Do not silently change business rules.

## Frozen stack

- Flutter Android-first learner app.
- Flutter Web staff/admin.
- Keep iOS supportability; public release later.
- FastAPI/Python backend.
- PostgreSQL.
- Object Storage.
- Modular monolith.
- API process + durable worker process from one codebase.

## Frozen architecture invariants

- Server authoritative for scoring, progress, permissions.
- Commands separated from telemetry.
- Offline client uses durable command queue + telemetry queue.
- Published content immutable/versioned.
- Enrollment/attempt pins exact revisions.
- Analytics preserves event time + knowledge/availability time + source capture.
- Mastery is not Risk.
- Risk is optional input for recommendation.
- UCI/OULAD are research baselines only; do not copy their weights as production defaults.
- Prediction, Recommendation Decision, Exposure, Execution, Outcome are separate layers.
- Product must work even if ML/recommendation is disabled.

## Phase status

- Phase 0: DONE.
- Phase 1 Implementation Foundation / Product Build Kickoff: ACTIVE.

Roadmap after that:
Phase 2 UX/UI Product System; Phase 3 Identity/Auth/Authorization; Phase 4 Content Platform & Publishing; Phase 5 Learning Core & Assessment; Phase 6 Offline-first & Synchronization; Phase 7 Durable Worker & Async Processing; Phase 8 Learning Analytics & Data Platform; Phase 9 Learning Intelligence; Phase 10 Production ML / Early Risk Prediction; Phase 11 Recommendation & Intervention; Phase 12 Instructor/Advisor/Admin; Phase 13 Hardening; Phase 14 Internal Alpha; Phase 15 Closed Beta/Pilot; Phase 16 Production Launch; Phase 17 Growth/Experimentation/Continuous Learning.

## Product direction already discussed

- Use ~5-minute sessions as a **low-friction product design anchor**, not as a claim that five minutes is inherently pedagogically optimal.
- Design the learning method from scientific evidence about learning + current content-consumption behavior.
- Streaks, rewards, and user targets are allowed as engagement mechanics, but must not substitute for learning quality.
- Learner experience should feel like a study companion/friend.
- Public/open/legitimate content sources are likely important due limited curriculum resources.
- Early pilot may be roughly 5 users due resource constraints.

## Working rules

1. Do not rush code before the current phase contract is clear.
2. Use V3.2 whenever a business-rule dispute occurs.
3. Do not over-engineer with Kafka, Kubernetes, microservices, warehouse, or external feature store without demonstrated need.
4. Every phase needs explicit deliverables, acceptance criteria, and a gate.
5. Schema pass is not runtime pass; add integration/concurrency/security tests.
6. Do not prematurely freeze curriculum, mastery, adaptive path, or final risk labels before Learning Intelligence.
7. Do not warp the product to preserve old thesis feature counts/models.
8. Production models must be evaluated on product-generated data.
9. Product must work when ML/recommendation is disabled.
10. After each major milestone, produce a fresh project progress snapshot.

## How to respond to new progress

When I provide new implementation progress:

- compare it with this baseline;
- identify the current phase;
- classify work as DONE / ACTIVE / BLOCKED / DEFERRED;
- preserve all previously frozen decisions unless I explicitly change them;
- record new issues/change requests;
- update the project snapshot at major milestones;
- do not invent missing V3.2 details—request or retrieve the original source when necessary.
