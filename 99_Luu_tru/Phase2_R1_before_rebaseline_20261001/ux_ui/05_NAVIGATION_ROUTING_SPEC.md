# Navigation and Routing Specification

## Learner

Primary routes: `/home`, `/learn`, `/course`, `/profile`. Onboarding `/welcome`, `/onboarding/goal`, `/onboarding/placement`, `/placement/*`. Learning child flow `/learn/cycle/*`. System recovery `/sync`, `/sync/error`, `/reauth`.

Rules:
- A selected answer is local UI state until submitted; route changes must not implicitly submit.
- Exiting a cycle prompts when meaningful local state could be lost; completed canonical responses are not undone.
- Resume uses saved cycle context and pinned revisions; never resends already terminal commands merely due to navigation.
- Deep-link into objective/review re-evaluates eligibility. Locked preview remains preview-only.
- Main navigation may be hidden in focused learning/placement flows, but a safe exit path remains.

## Staff

Primary routes are `/staff/dashboard`, `/staff/learners`, `/staff/content`, `/staff/interventions`, `/staff/analytics`, `/staff/admin` with child resources documented in the screen inventory.

Rules:
- Unknown/unauthorized routes show access-required/not-found without exposing foreign resource existence.
- Role-based menu visibility is presentation only; Phase 3 server authorization is authoritative.
- Unsaved draft navigation prompts before discard.
- Published revision has no edit-in-place route.

## Back/deep-link behavior

Back returns to the nearest safe context and must never bypass prerequisite, permission, revision or canonical state. A browser refresh/deep link must reconstruct context from route + server state in implementation phases; the Phase 2 prototype uses mock state only.
