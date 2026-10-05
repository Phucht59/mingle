> Canonical-layout update — 2026-09-24: active source is organized under `01_San_pham/`; Phase 1 remains ACTIVE / GATE NOT PASSED. Current status: `02_Tai_lieu_du_an/07_Tien_do_du_an/PROJECT_STATE.md`; observed runtime evidence: `03_Kiem_thu/Bang_chung/VERIFICATION_REPORT.md`. Exact original V3.2 verification sources remain absent.

# Test Strategy — contract plus runtime proof

## Layers

1. **Original contract checks:** run V3.2 suite unchanged; any failing rule is investigated before application edits.
2. **Pure rule tests:** eligibility, reason priority, provisionally versioned scheduler/config and derived signals with fixed input/clock.
3. **Integration:** real PostgreSQL transaction path, worker durable task processing, object-store interface and FastAPI boundaries.
4. **Concurrency/offline:** duplicates, out-of-order arrivals, same learner on two devices, late event, retry after timeout, idempotent score/reward.
5. **Security:** unauthorized content/attempt access and staff permissions, no sensitive telemetry leak.
6. **End-to-end smoke:** Flutter learner and Web staff shells boot, backend and worker ready, minimal test operation.

## Highest-value test cases

| Scenario | Must hold |
|---|---|
| First wrong, hint, retry right | First evidence remains wrong; retry assisted; server score/feedback revision pinned. |
| Multiple same command IDs | One canonical effect, one progress/streak/reward award. |
| Telemetry absent or late | Missing observation is unknown; cannot silently count as zero replay or verified unaided Check. |
| Event T1 arrives T3 after decision T2 | T2 reason/evidence does not contain event unknown at T2; future decisions may use it. |
| Concurrent devices and timezone switch | Stable canonical ordering, deterministic local-day attribution and no duplicate award. |
| Content revision changes | Old attempt remains on exact old revision; invalid new content cannot score old attempt. |
| ML/recommender disabled | Curriculum and due-review fallback returns valid finite cycle or honest empty state. |
| Prerequisite blocked | Chosen focus cannot open invalid content; preview does not grant mastery. |
| Missing five-role content | No fake cycle completion; authoring gap logged. |
| One vs two distinct unaided correct first responses | One success stays in current task band; two in same objective/band including independent Check offer at most one next-band challenge without marking mastery or unlocking new objective. |
| Listening replay missing/late/client-reported | Answer can be server-scored, playback quality remains explicit/unknown; replay telemetry alone cannot certify assessment condition or alter canonical score. |
| Invalid license/source | Item cannot publish, even if publicly available. |

Test fixture data are synthetic; assertions target externally meaningful behavior, not just implementation branching. Pilot usability testing complements, rather than replaces, engineering tests. Phase 1 only needs harnesses and minimal smoke appropriate to the foundation; later features gain full tests when implemented.
