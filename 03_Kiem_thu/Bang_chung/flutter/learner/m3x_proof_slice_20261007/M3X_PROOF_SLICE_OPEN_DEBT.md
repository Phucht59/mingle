# M3.X proof slice — open debt

No listed item is closed by schema, widget or screenshot success alone. Owners below are roles, not assertions that a person accepted an assignment.

| ID | Debt / impact | Required next evidence | Role / scope |
|---|---|---|---|
| M3X-D01 | Mac/Xcode/signing access and exact iOS beta unknown; iOS compilation unavailable on Windows | Record Mac/macOS/Xcode, phone OS/build, Flutter 3.32.8, signing configuration; successful simulator and device build of the supplied source hashes | iOS engineer + device owner; propagation blocker |
| M3X-D02 | Native tab/modal/Close, sheet and gesture behavior untested | Videos of focused route, same origin after Close, Resume and native gestures; no lost state | iOS QA; propagation blocker |
| M3X-D03 | VoiceOver semantics/focus untested; button-selected representation provisional | Spoken role/selection, adjacent explanation, one verdict, stable focus and reachable next action with recording/settings | Accessibility reviewer; propagation blocker |
| M3X-D04 | Actual Dynamic Type, contrast/transparency and all touch regions untested | Largest accessibility categories, dark/increased contrast, Reduce Motion/Transparency, all essential controls ≥44 points | Accessibility + iOS QA; propagation blocker |
| M3X-D05 | Native app termination/durable restoration not proven | Release-mode app force termination and icon relaunch; before/after learning snapshot, exact bytes/revisions/responses; pending without ACK, then valid ACK | Runtime QA; propagation blocker |
| M3X-D06 | Physical performance/haptics untested | Profile trace and observations on iPhone Air; measured frames/input latency if quantified; optional selection haptic review | iOS engineer/design reviewer; no FPS/haptic freeze yet |
| M3X-D07 | Pinned Flutter compatibility with exact iOS 27 beta/Xcode unknown | Build logs; if incompatible, record a narrow implementation issue/change candidate and validate affected code after an approved compatibility change | iOS engineer; do not silently upgrade all dependencies |
| M3X-D08 | Controlled server is in-process proof infrastructure; no production scoring/permissions/grants/network adapter | Existing production service integration at the proper future phase; real receipt, grant expiry/revocation and account-isolation tests | Backend/mobile; outside narrow proof |
| M3X-D09 | Assistance metadata is durable local proof evidence; production transport/canonical linkage is not implemented | Integrate the established evidence contract without adding ad hoc fields to frozen submit commands | Product/backend/mobile; future integration, no false unaided evidence |
| M3X-D10 | Snapshot store is single-writer, unencrypted fixture storage with basic checksum and 20 MiB safety bound | Production storage security/migrations/recovery, interruption-at-each-write-boundary, low-space/power-loss and account switching evidence | Mobile/security; broader offline debt |
| M3X-D11 | Full command scheduler, canonical refetch/recovery policy and telemetry queue not implemented | Existing V3.2 production integration; keep telemetry separate, avoid silent repin/reset on conflict | Mobile/backend; outside slice |
| M3X-D12 | Result Pending sample persists its eventual ACK | Use a fresh disposable proof installation for a fresh pending fixture; preserve prior run container before resetting | Reviewer workflow limitation; no product policy change |
| M3X-D13 | External learner usability and staff usability not validated | Approved participant studies and human sign-off | Product/research; existing debt remains open |
| M3X-D14 | Production accessibility certification and Android TalkBack unverified | Separate platform/production accessibility audit | Accessibility/QA; existing debt remains open |
| M3X-D15 | Broad real-world offline testing incomplete | Real networks, storage pressure, app/OS lifecycle, replay, account revocation and concurrent server conditions | Runtime QA; existing debt remains open |
| M3X-D16 | Production ML/risk/recommendation not implemented | Separate future workstream and validation | Future scope; existing debt remains open |
| M3X-D17 | Exact Mingo Blue, artwork and haptic usage not frozen | Physical appearance/usability review and appropriate design acceptance | Design/product; candidate remains candidate |

M3 stays NOT YET PASSED. GĐ1 internal BA closure remains the owner-confirmed historical milestone; customer validation is separate. Phase 3 Auth remains HOLD. None of these debts authorizes another workstream automatically.
