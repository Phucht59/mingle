# Canonical companion / asset manifest

CURRENT 2026-10-02. One canonical capybara and one exploration world; two existing masters are reused. No new pose or emotion image has been generated in this cycle. Ten logical uses are registered by `CompanionUse` in design.dart; eight unavailable distinct poses fall back to the neutral master. This is a **partial pose library**, not ten finished illustrations. Human character/pose approval PENDING. No realtime 3D.

| Asset ID | Pose / expression | Usage | Resolution / format | File bytes | Fallback | Light / dark |
|---|---|---|---|---:|---|---|
| capy-neutral-master | Existing calm companion; avoid psychological inference | Quiet support, profile, summary, topic thumbnail | 1024×1536 PNG | 2302299 | text/icon remains usable if media unavailable | Same decorative asset; text uses opaque theme surfaces |
| capy-exploration-master | Existing reading/exploration composition | Welcome/Home/Course static scenery | 1536×1024 PNG | 2269212 | neutral master or no decoration | Same asset; no critical text overlay |

| Logical state ID | Intended context | Current rendered asset / limitation |
|---|---|---|
| neutral | quiet presence | capy-neutral-master |
| reading | reading/review | neutral fallback; scenery also includes reading context |
| listening | listen step | neutral fallback; distinct pose pending |
| thinking | retrieve | neutral fallback; no inferred emotion |
| support | hint/help | neutral fallback |
| encouraging | supportive feedback | neutral fallback; no pressure/reward claim |
| completion | summary | neutral fallback in CompletionMoment |
| offline | local/offline explanation | neutral fallback; runtime queues not implemented |
| empty | empty state | neutral fallback; explicit text explains state |
| errorSupport | recoverable issue | neutral fallback; not a diagnosis |

DPR-bounded decoding: mascot cacheHeight is display height×DPR clamped to16…1536; scenery cacheWidth covers the viewport/crop at DPR, clamped to16…1536. Raw originals are unchanged. Static layout avoids continuous motion, blur/backdrop filters and runtime3D. Unique poses/alternate optimized encodings need controlled provenance and human approval; no unsupported automatic device-tier switching is introduced. Performance reports distinguish decode/cache estimates from observed process memory. Source/license/hashes: [ASSET_PROVENANCE.json](ASSET_PROVENANCE.json). Future pose changes must preserve character silhouette, proportions, quiet expression and universe continuity.

A minimum16 prevents a transient1px request producing a zero-size second dimension. Default Impeller startup initially reproduced a texture failure; the corrected source retains all205 priorapproved image hashes, verified by actual comparison. New source approval and native rerun are recorded separately in current evidence.
