# PHASE 1 DECISION REGISTER
## Snapshot: 23 September 2026

This is a working decision register derived from the current project context and the completed scientific resolution.

## Status semantics

- **FROZEN** — preserve unless a formal approved Change Request supersedes it.
- **FREEZE NOW** — research-supported guardrail to incorporate into official Phase 1 artifacts.
- **MVP HYPOTHESIS** — implement as configurable/versioned default where appropriate; validate; do not market as proven.
- **DEFERRED** — intentionally not finalized yet.
- **NOT FROZEN** — explicitly unresolved/working label.

| ID | Decision | Status | Notes |
|---|---|---|---|
| ARCH-001 | V3.2 is implementation source of truth | FROZEN | Exact source files override memory summaries. |
| ARCH-002 | Flutter Android-first learner app | FROZEN | Flutter Web staff/admin; iOS compatibility retained. |
| ARCH-003 | FastAPI + PostgreSQL + Object Storage + modular monolith | FROZEN | API + durable worker same codebase. |
| ARCH-004 | Server authoritative canonical scoring/progress/permissions | FROZEN | Client is not source of truth. |
| ARCH-005 | Command separated from telemetry | FROZEN | Offline queues remain distinct. |
| ARCH-006 | Published content immutable/versioned; attempts pin revisions | FROZEN | Historical evidence must remain interpretable. |
| ARCH-007 | Mastery != Risk; Risk optional for recommendation | FROZEN | Do not collapse concepts. |
| ARCH-008 | Product works without ML/recommendation | FROZEN | Deterministic fallback required. |
| PROD-001 | Vocabulary + Grammar + Listening are MVP scope | FROZEN/Phase baseline | Speaking/conversation deferred. |
| PROD-002 | A0 internal → A1 → A2 → B1 → B2 | Current baseline | TOEIC is external goal/mapping, not curriculum backbone. |
| PROD-003 | Pilot ~5 users | Current baseline | Usability/technical validation, not efficacy proof. |
| PROD-004 | Free-first development/pilot; preserve future Free/Premium | Current baseline | Pricing not frozen. |
| PROD-005 | Product name “Mingo” | NOT FROZEN | Treat as working label only. |
| LEARN-001 | Finite ~5-minute Adaptive Learning Feed | Current baseline | 5 minutes = product hypothesis, not proven optimal duration. |
| LEARN-002 | Review/Learn/Retrieve/Transfer/Check roles | Current baseline | Functional roles, not required UI labels. |
| LEARN-003 | No infinite learning scroll | FROZEN | Explicit cycle endpoint and explicit continue. |
| LEARN-004 | Curriculum/prerequisites constrain adaptive choice | FROZEN | Engagement optimization cannot bypass learning validity. |
| RES-Q1 | Observable error evidence; no one-click causal diagnosis | FREEZE NOW | Repeated item/objective evidence before qualitative learner insight. |
| RES-Q2 | Response latency stored for QA, not mastery | FREEZE NOW | No speed = ability inference. |
| RES-Q3 | Hints typed/versioned; assisted != unassisted | FREEZE NOW | Check independent before submit. |
| RES-Q4 | Preserve first attempt; one practice retry default | MVP HYPOTHESIS | Retry count configurable. |
| RES-Q5 | Skip explicit; no mastery; repeated skip can trigger support | FREEZE NOW | Threshold for support is hypothesis. |
| RES-Q6 | Practice replay flexible; Check replay bounded | MVP HYPOTHESIS | Exact play count is hypothesis. |
| RES-Q7 | Vocabulary uses meaning/audio/context/multi-form retrieval | FREEZE NOW | Translation card may exist but is not whole model. |
| RES-Q8 | Hybrid grammar scaffold/attempt sequence | MVP HYPOTHESIS | Varies by prior evidence. |
| RES-Q9 | Difficulty can rise within objective | MVP HYPOTHESIS | Final thresholds deferred. |
| RES-Q10 | Learner focus respected within bounded review/prerequisite need | MVP HYPOTHESIS | No opaque algorithm veto. |
| RES-Q11 | Short provisional placement across three domains | MVP HYPOTHESIS | Not CEFR certification. |
| RES-Q12 | Qualitative evidence-backed learner profile; no fake mastery % | FREEZE NOW | Show uncertainty / insufficient evidence. |
| RES-Q13 | Optional goal informs eligible-content weighting | MVP HYPOTHESIS | Goal != competence. |
| RES-Q14 | Default one ~5-minute daily cycle; customizable targets | MVP HYPOTHESIS | Time is not learning evidence. |
| RES-Q15 | Retrieval-based streak separate from target | MVP HYPOTHESIS | Streak != proficiency. |
| RES-Q16 | Progress/milestone reward; no XP farming/leaderboard in MVP | MVP HYPOTHESIS | Rewards never unlock mastery/prerequisites. |
| RES-Q17 | Browse/review/preview course map with prerequisite constraints | MVP HYPOTHESIS | Preview != mastery. |
| RES-Q18 | Short verifiable recommendation reason | MVP HYPOTHESIS | Explanation must match actual decision reason. |
| INTEL-001 | Final mastery formula | DEFERRED | Phase 9+. |
| INTEL-002 | Knowledge tracing model | DEFERRED | Phase 9+. |
| INTEL-003 | Production risk model/threshold | DEFERRED | Product data required. |
| INTEL-004 | Production recommendation weights/path optimizer | DEFERRED | Product data required. |
| INTEL-005 | Statistical CAT / validated CEFR cut scores | DEFERRED | Needs calibrated item bank/validation. |

## Change control rule

A decision marked FROZEN may only change through:
- a concrete implementation or evidence-based conflict;
- an explicit Change Request;
- impact analysis;
- owner approval where required.

Do not silently reinterpret a frozen rule.
