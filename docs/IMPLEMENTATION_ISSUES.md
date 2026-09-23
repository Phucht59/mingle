# Implementation Issues — current

| ID | Issue | Status / resolution |
|---|---|---|
| II-01 | Exact V3.2 package, original DDL/OpenAPI and 115+22 verification source absent | OPEN / BLOCKING exact mapping and gate. Previous repo absence is resolved by owner-authorized greenfield implementation; do not request a nonexistent repo |
| II-02 | MVP learning hypotheses could be mistaken for frozen scoring/architecture | OPEN / NON-BLOCKING; version defaults and keep scoring/domain implementation deferred until contracts map |
| II-03 | Offline Check/placement audio replay authority | OPEN / depends on II-01. Playback telemetry is not canonical score evidence and cannot prove listens |
| II-04 | PostgreSQL/container runtime unavailable here | OPEN / runtime blocker. Source and 6 integration/concurrency tests exist; run against real DB on supported host; no pass claimed |
| II-05 | Flutter execution rejected by automatic approval review | OPEN / runtime blocker. SDK contacted cloud metadata endpoint; no bypass or repeated execution. Authored shells/tests require safe supported Flutter runtime |
| II-06 | No external git remote/hosted CI evidence | OPEN / verification blocker. Workflow supplied, not executed. Full-stack clean reproduction still required |

No demonstrated V3.2 conflict; Change Request NONE. Infrastructure source remains provisional pending source mapping.
