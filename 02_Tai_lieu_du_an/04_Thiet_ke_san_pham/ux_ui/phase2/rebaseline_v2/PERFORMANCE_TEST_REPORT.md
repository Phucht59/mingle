# Performance report —final candidate 2026-10-03

**RERUN NOW / measurement completed; performance budget NOT PASSED; PHYSICAL DEVICE PERFORMANCE PENDING.** Default Android engine, no renderer override, current source hashes match both runs. GoogleSwiftShader software OpenGLES on sdk_gphone64_x86_64/API35;1080×2400/DPR2.625; active60.000004Hz, no90/120supported mode. This virtual device is not LOW/MID/HIGH hardware.

## Actual profile frame windows

| Scenario | Frames | UI p95ms | Raster p95ms | Over-budget proxy | Sample qualification |
|---|---:|---:|---:|---:|---|
| first_home_widget_mount_not_android_cold_start | 3 | 89.85 | 325.93 | 100.00% | INSUFFICIENT_SAMPLE_FOR_DEVICE_GATE |
| home_scroll | 608 | 18.12 | 70.50 | 96.88% | ENGINEERING_SAMPLE_ONLY |
| home_to_lesson | 8 | 15.94 | 29.98 | 12.50% | INSUFFICIENT_SAMPLE_FOR_DEVICE_GATE |
| answer_interaction | 9 | 4.03 | 105.29 | 22.22% | INSUFFICIENT_SAMPLE_FOR_DEVICE_GATE |
| immediate_feedback | 4 | 6.16 | 26.48 | 50.00% | INSUFFICIENT_SAMPLE_FOR_DEVICE_GATE |
| lesson_to_result | 73 | 16.18 | 28.73 | 13.70% | INSUFFICIENT_SAMPLE_FOR_DEVICE_GATE |
| result_to_course | 8 | 22.63 | 23.22 | 12.50% | INSUFFICIENT_SAMPLE_FOR_DEVICE_GATE |
| course_scroll | 704 | 6.38 | 45.43 | 90.20% | ENGINEERING_SAMPLE_ONLY |
| home_scroll_text_200_percent | 742 | 6.08 | 33.94 | 89.89% | ENGINEERING_SAMPLE_ONLY |
| offline_fixture_render_not_network_sync | 3 | 8.63 | 17.54 | 33.33% | INSUFFICIENT_SAMPLE_FOR_DEVICE_GATE |
| warm_home_widget_mount_not_android_warm_start | 3 | 5.50 | 17.70 | 33.33% | INSUFFICIENT_SAMPLE_FOR_DEVICE_GATE |

60Hz budget16.67ms. Warmed scroll raster exceeds that budget and overrun exceeds1%; **no sustained60fps PASS**.90Hz11.11ms and120Hz8.33ms are policy only, UNMEASURED. UI/raster deadlines are evaluated separately; totalSpan remains in raw data. Proxy violations are not exact compositor dropped frames. First-mount and small tap windows have fewer300frames and cannot certify a device budget. These data describe this emulator/host/renderer and do not predict phone performance.

## Actual normal release activity / memory / footprint

Five process-cold launches, no data/filesystem-cache clearing: Android TotalTime median2617.0ms, p952677.0ms. Five valid same-PID background returns: command WaitTime median144.0ms,p95288.0ms. This is activity-start reporting, not time to meaningful learning. Release PSS snapshot73883KiB (72.15MiB); one snapshot cannot prove no memory growth. No physical battery/thermal consumption test; dumpsys snapshots are context only.

Normal main-entry release APK26,034,345bytes, SHA256`ddaa2b02bf112082bc474fbfb37da05b3e5445cd616e66a9817588a9fdf65130`. AAB44,977,818bytes, SHA256`e8a2a759bf153d6c58979de819a323fe0e6ba604ccc302b81e2a5c6d668eecf3`. Local generated debug signing only, not production signing/deployment. AABbytes are not Play delivery size; universal APK is not ABI-specific download size. The profile integration APK is a benchmark harness and is excluded from deliverables. Earlier121MBdebug APK is EXISTING EVIDENCE, not an equivalent performance baseline.

Codec probes after the journey, not cold filesystem or production ImageProvider/GPU timing: hero1080×720 RGBAestimate3,110,400bytes,73.101ms; mascot473×709 RGBAestimate1,341,428bytes,64.736ms. These estimates do not include native/GPU/cache overhead. Raw encoded assets remain unchanged: hero2,269,212B andmascot2,302,299B exceed per-asset512/256KiB candidate targets; total authored5,461,500B is below8MiB. Missing pose variants and controlled encoding/visual approval remain open; do not claim all asset budgets met.

## Identified failure, correction and retest

Initial default Impeller normal startup reproduced an invalid-texture fatal; a diagnostic Skia run reported empty resize dimensions. The first bounded sizing implementation could request1px at a transient tiny layout, allowing its other dimension to round to0. Minimumdecode16 corrects that condition.50technical candidate tests include four tiny-layout probes;275shared tests compare all205existing approved pixels unchanged. The new default-engine profile/release host runs retained five cold processes and five warm PIDs. Before-failure logs and the initial failed host report are retained, including the diagnostic renderer override. Neither the override nor failed run is labelled current-default PASS. [Flutter Impeller guidance](https://docs.flutter.dev/perf/impeller) documents the diagnostic CLI opt-out; the deployed candidate manifest was not changed to disable Impeller.

Static composition, no continuous animated scene, opaque text surfaces and DPR-bounded decoding are implemented. Software raster timings remain over budget; no speculative framework/architecture change was made to hide them. Physical LOW/MID/HIGH,90/120Hz, ten-journey memory, thermal/energy, real text200%/audio/background behavior and independent benchmark review are **PENDING / NOT RUN**. Reproduce with run_performance_benchmark.ps1 and actual hardware before certifying budgets.

Raw [profile host](../../../../../03_Kiem_thu/QA_QC/phase2/evidence_gated_20261002/performance/20261003T035003Z-82d57cfa/host_report.json), [release host](../../../../../03_Kiem_thu/QA_QC/phase2/evidence_gated_20261002/performance/20261003T040418Z-7102af70/host_report.json); rawFrameTiming JSONs/command logs and [PERFORMANCE_SUMMARY.json](../../../../../03_Kiem_thu/QA_QC/phase2/evidence_gated_20261002/PERFORMANCE_SUMMARY.json). Phase3 HOLD.
