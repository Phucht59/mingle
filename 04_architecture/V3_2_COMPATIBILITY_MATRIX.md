> Canonical-layout update — 2026-09-24: active source is organized under `05_code/`; Phase 1 remains ACTIVE / GATE NOT PASSED. Current status: `01_governance/PROJECT_STATE.md`; observed runtime evidence: `06_quality/evidence/VERIFICATION_REPORT.md`. Exact original V3.2 verification sources remain absent.

# V3.2 Compatibility Matrix — evidence state

This matrix cannot certify compatibility until original V3.2 source arrives. A handoff summary is not an exact contract ID. Do not fill the 'exact rule' column from memory.

| Requirement group | Known summary invariant | Exact source ID | Current assessment | Required verification |
|---|---|---|---|---|
| First attempt, retry, hint, skip (PRD-02..04) | Server authoritative scoring; pinned revision | PENDING | UNVERIFIED, no conflict proven | Map command/schema/scoring to original rule; concurrent replay test |
| Replay and Check (PRD-05,09) | Server authority; command vs telemetry | PENDING | UNVERIFIED; II-03 tracks client-reported playback and comparability, not a proven V3.2 conflict | Verify score/telemetry boundary, missing/late playback and quality flags against exact contract |
| Curriculum/content (PRD-06..08,13..14) | Published immutable/versioned; pin revisions | PENDING | PARTIAL conceptual alignment, contract unverified | Content/prerequisite/attempt schema and checks |
| Evidence profile and timing (PRD-07,10,15) | Event time + knowledge/availability time; mastery≠risk | PENDING | PARTIAL conceptual alignment | Timestamp, source capture, projection and point-in-time tests |
| Streak/reward (PRD-11..12) | Server progress authoritative; offline queues | PENDING | UNVERIFIED | Idempotent business operation and timezone semantics |
| Scheduler and fallback (PRD-08,13,16) | Risk optional; product works without ML/recommendation | PENDING | PARTIAL conceptual alignment | API/worker reason and fallback mapping |
| Staff/access/security | Flutter Web, permission server authority | PENDING | UNVERIFIED | Actual authorization contracts and negative tests |

After source intake: capture file path/hash and rule ID per row; mark `COMPATIBLE / IMPLEMENTATION GAP / CONFLICT`; link tests and reproduction. A genuine frozen-rule conflict creates an issue and possibly a CR, never an untracked edit. Missing source remains II-01.
