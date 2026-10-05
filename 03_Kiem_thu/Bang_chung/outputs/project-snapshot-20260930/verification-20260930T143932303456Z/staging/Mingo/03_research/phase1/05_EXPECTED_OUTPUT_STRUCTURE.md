# Expected Output Structure / Acceptance Gate

The research agent's final output should use this structure:

## 1. Executive conclusion
- What methodology emerges from the evidence?
- Which earlier assumptions survive?
- Which assumptions need qualification?

## 2. Evidence model
- source hierarchy
- evidence limitations
- generalizability caveats

## 3. Decisions Q1–Q18
For every question:
- Recommended MVP policy
- Why
- Evidence
- Evidence strength
- Implementation rule
- Telemetry/evidence to store
- What NOT to infer
- Later-phase option

## 4. Synthesized Learner Evidence Model
- raw observations
- derived short-term signals
- curriculum state
- user intent/preferences
- engagement state
- deferred intelligence state

## 5. Adaptive Learning Feed / Scheduler policy
- eligibility
- prerequisite constraints
- prioritization
- review/new balance
- difficulty
- remediation
- user focus
- completion
- explanation/audit reason
- non-ML fallback

## 6. Placement policy
- A0–B2
- Vocabulary + Grammar + Listening
- short/adaptive onboarding
- uncertainty
- progressive recalibration

## 7. Motivation / engagement policy
- streak
- target
- reward
- anti-gaming
- strict separation from learning/mastery

## 8. User-facing learner profile
- what is shown
- what is hidden
- confidence/uncertainty
- recommendation explanations

## 9. Minimal telemetry
- field
- reason needed
- source
- whether raw/derived
- retention/privacy note

## 10. Five-user pilot plan
- what can be learned
- what cannot be claimed
- qualitative evidence
- technical checks
- acceptance criteria

## 11. Decision register
Table:
| Q | Decision | Classification | Evidence Strength | Phase Impact |

Classifications:
- FREEZE NOW
- MVP HYPOTHESIS
- DEFER
- CHANGE REQUEST

## 12. Issues / Change Requests
Only if real conflicts exist.

## 13. Updated Phase 1 status
Use:
- DONE
- ACTIVE
- BLOCKED
- DEFERRED

Do not mark Phase 1 fully done unless all Phase 1 implementation-foundation deliverables and gates are actually complete.

## 14. Product Charter / MVP PRD changes
List exact requirements to copy into the official artifacts.

## 15. Sources
Prefer:
- meta-analyses/systematic reviews
- peer-reviewed SLA/education research
- reputable measurement/adaptive-learning sources
- current product/consumer evidence for UX behavior only

### Acceptance gate
PASS when:
- every question has a recommendation, not just options;
- evidence vs inference is explicit;
- scientific and consumer evidence are not conflated;
- policies are implementable;
- telemetry is minimized;
- the five-user pilot is treated realistically;
- V3.2 remains intact unless a formal change request is justified.
