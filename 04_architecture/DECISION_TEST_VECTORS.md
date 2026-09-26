# Q9 and Audio Authority — Review Vectors

The vectors make the corrected product policy reviewable. They are semantic tests,
separate from the original V3.2 suite. `V3_2_COMPATIBILITY_MATRIX.md` now maps their
authority boundary to exact sources. Objective/band/assessment-condition metadata
remains a versioned implementation task for later learning/product phases.

| Case | Evidence available at decision | Expected decision and state |
|---|---|---|
| V1 | One unaided correct first response in current objective/band | No next-band CHALLENGE; current-band Transfer may be offered. |
| V2 | Two unaided correct first responses, two distinct item revisions, same objective/band; second is independent Check | At most one next-band CHALLENGE; no mastery, level or prerequisite promotion. |
| V3 | Same item wrong then correct on retry, plus one other correct | No step-up: retry is neither first-response success nor independent item evidence. |
| V4 | Two different correct items but one opened a hint before response | No step-up: assisted success excluded. |
| V5 | Two unaided correct items, one in another objective or task band | No step-up for current objective/band: predicate must use a coherent evidence set. |
| V6 | Two unaided correct first responses but neither is independent Check | No step-up; Check requirement unmet. |
| V7 | Listening Check answer right; offered two-play UI policy and client-reported count recorded | Server scores answer; it may support low-stakes provisional challenge with another valid success, but not certified listening level or verified number of physical listens. |
| V8 | Listening Check answer right, replay telemetry missing/offline delayed | Server may score answer; condition quality remains unknown, so it cannot satisfy Q9 Check predicate or support standardized listening interpretation until reconciled. |
| V9 | One correctly answered Check after model/recommender disabled | No hard dependency on ML; fallback selects eligible current-band/Review content, not an unjustified next-band challenge. |

In the later learning/offline phases, convert V1–V9 into domain/integration tests and
add duplicate/replay conflict vectors using the mapped canonical event/score contracts.
Their future implementation is not represented as one of the original 115 checks.
