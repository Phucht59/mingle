# CURRENT WORK QUEUE — CONTINUE IMMEDIATELY

## Current phase
**Phase 1 — ACTIVE**

## Goal
Finish Phase 1 to a real gate, not just a research/spec discussion.

## Priority 0 — ingest and reconcile
- Read the full scientific resolution.
- Treat it as the current working Phase 1 methodology baseline.
- Do not rerun the 18-question research by default.
- If exact V3.2 is supplied, build a compatibility matrix:
  research requirement → V3.2 contract/rule → compatible / issue / CR needed.

## Priority 1 — official product artifacts
Create or update:

1. `PRODUCT_CHARTER.md`
   Must include:
   - target problem/user;
   - internal level progression;
   - MVP scope;
   - product promise;
   - finite Adaptive Learning Feed philosophy;
   - evidence vs engagement separation;
   - pilot boundaries;
   - commercialization direction;
   - what is explicitly deferred.

2. `MVP_PRD.md`
   Convert the research result into testable product requirements:
   - first attempt / retry;
   - hints;
   - skip;
   - listening replay;
   - vocabulary/grammar behavior;
   - difficulty progression;
   - user focus;
   - placement;
   - learner profile;
   - goals;
   - target/streak/reward;
   - course-map control;
   - explanations;
   - offline/late-event/idempotency boundaries inherited from V3.2.

3. `LEARNER_EVIDENCE_MODEL.md`
   Separate:
   - raw observations;
   - derived short-term signals;
   - curriculum state;
   - user intent;
   - engagement;
   - deferred intelligence.

4. `ADAPTIVE_FEED_MVP_SPEC.md`
   Define:
   - candidate eligibility;
   - prerequisite filter;
   - deterministic priority;
   - selection reasons;
   - difficulty/remediation;
   - user-focus override;
   - cycle closure;
   - fallback when ML/recommendation unavailable;
   - auditability;
   - configurable hypothesis parameters.

## Priority 2 — implementation foundation artifacts
Create/update:
- `IMPLEMENTATION_ROADMAP.md`
- `BACKLOG.md`
- `REPO_STRUCTURE.md`
- `ENVIRONMENTS.md`
- `CONFIG_AND_SECRETS.md`
- `DATABASE_BOOTSTRAP_AND_MIGRATIONS.md`
- `CI_CD.md`
- `TEST_STRATEGY.md`
- `CODING_STANDARDS.md`
- `DEFINITION_OF_DONE.md`
- `IMPLEMENTATION_ISSUES.md`
- `CHANGE_REQUESTS.md`

## Priority 3 — bootstrap evidence
If exact V3.2 and repo are available:
- inspect actual repository;
- run 115 contract checks and 22 SQL checks or the exact available verification suite;
- verify local backend/database bootstrap;
- establish minimal CI;
- create a Phase 1 evidence report.

If exact V3.2/repo is NOT available:
- do not invent implementation details;
- complete all unblocked documentation/foundation work;
- mark the missing artifact as a localized blocker.

## Priority 4 — Phase 1 gate
Create `PHASE_1_GATE.md`.

The gate must state:
- every required deliverable;
- evidence;
- PASS / FAIL / BLOCKED;
- unresolved issues;
- any Change Request;
- next phase eligibility.

Do not mark Phase 1 DONE if:
- official artifacts are missing;
- required exact V3.2 compatibility is unverified;
- bootstrap/test evidence required by the gate is missing.

## After Phase 1
Only after PASS:
continue to Phase 2 — UX/UI Product System.

Do not jump directly to ML or recommendation implementation.
