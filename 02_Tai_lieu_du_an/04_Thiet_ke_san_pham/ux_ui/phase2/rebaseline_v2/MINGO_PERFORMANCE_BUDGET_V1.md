# Mingo performance budget V1

2026-10-02 · Evidence level E4 · product requirement and engineering targets. These limits are candidate acceptance policy, not measured results or human approval. [PERFORMANCE_TEST_REPORT](PERFORMANCE_TEST_REPORT.md) holds observed numbers; [DEVICE_TEST_MATRIX](DEVICE_TEST_MATRIX.md) holds device coverage. Phase 3 remains HOLD.

## Frame policy

Use the display refresh rate reported by the device at measurement time. Do not force 120 fps. UI and raster are separate pipelined stages: compare each duration with the frame budget, rather than adding their durations and treating that sum as a frame deadline. `totalSpan` is a separate latency diagnostic. An idle screen does not need to repaint at the refresh rate. [Flutter FrameTiming](https://api.flutter.dev/flutter/dart-ui/FrameTiming-class.html) documents these measurements.

| Actual refresh | Deadline per stage | Coverage claim allowed |
|---|---:|---|
| 60 Hz | 16.67 ms | Only a measured 60 Hz device/run |
| 90 Hz | 11.11 ms | Only a measured 90 Hz device/run |
| 120 Hz | 8.33 ms | Only a measured 120 Hz device/run |

Candidate targets for the critical Home → Lesson → Answer → Feedback → Result journey: UI and raster p95 within the actual deadline; p99 within twice the deadline; no more than 1% of frames over either deadline in warmed repeated scrolling/navigation. Capture first-use frames separately and retain all raw samples; do not discard a shader/image cost to hide a problem. At least 300 captured frames per repeated scenario, five repeated startup samples and independent device review are required before calling a device budget satisfied. A brief tap sample remains diagnostic even when its few frames happen to be below budget. Budget overrun is a jank proxy; exact dropped compositor frames need a separate Android system trace.

## Startup, memory and assets

| Item | Candidate target | Measurement and boundary |
|---|---|---|
| Process cold start | p95 Android initial-display report ≤2 s on the selected LOW device | Force-stop then `am start -W`; no data/cache deletion. Not full first meaningful activity. |
| Warm background return | No process replacement, lost fixture state or visible stuck transition | Record PID before/after and `am start -W`; command WaitTime does not equal cold TotalTime. |
| Process memory | No monotonic growth after ten repeated journeys; investigate increase >32 MiB retained PSS | `dumpsys meminfo` plus repeated physical journeys; one snapshot cannot prove absence of leaks. |
| Decoded images | Target ≤16 MiB estimated RGBA in a core viewport | Actual display dimensions × DPR; cache/texture/native overhead measured separately. |
| Hero encoded asset | Target ≤512 KiB per packaged resolution | Optimize format/resolution with visual review; source master kept outside runtime declaration where feasible. |
| Mascot encoded asset | Target ≤256 KiB per small packaged pose | Same canonical animal; reuse a pre-rendered asset, no runtime 3D. |
| Packaged authored assets | Target ≤8 MiB total | Actual manifest footprint, not unreferenced master folder size. |
| Installed release footprint | Record actual APK/AAB bytes and compare candidate delta | Investigate >10% growth between equivalent ABI builds. Universal APK size is not download size; AAB is not Play delivery size. |
| Decode | Record bundle-load/first-codec-frame ms and decoded dimensions | Codec microbenchmark after a journey is not cold disk, actual ImageProvider timing or physical GPU upload. |
| Battery/thermal | No unnecessary continuous visual/audio/background activity | Physical energy/thermal session required; `dumpsys` snapshots alone provide context, not energy consumption. |

The initial-display target is a Mingo policy proposal rather than the Android vitals threshold. Android distinguishes cold/warm/hot and initial/full display, so do not merge these into one startup number. [Android launch-time guidance](https://developer.android.com/topic/performance/issues/launch-time).

## Rendering rules and quality adaptation

Prefer static composition, bounded image decode sizes, cached assets, reused renders, const widgets, and isolated rebuilds. Lazy-build a long list when the candidate actually needs it; a short finite three-item lesson list does not justify replacing the navigation/state model. No unnecessary BackdropFilter, saveLayer, full-screen live blur, large animated opacity tree or dynamic shadows. Any expensive effect needs a measured benefit/cost decision. [Flutter performance best practices](https://docs.flutter.dev/perf/best-practices).

LOW uses the same meaning, hierarchy, answer and accessibility affordances with simpler optional effects. MID/HIGH can use a brief optional transition only after its actual device budget is measured. Device tier is assigned from real hardware/context, never a fictional benchmark score or emulator label. System reduced motion takes precedence on every tier; no adaptation changes learning semantics or hides information.

## Reproduce and interpretation

Use [run_performance_benchmark.ps1](../../../../../04_Van_hanh/Scripts/run_performance_benchmark.ps1) with a selected Android device. Profile captures actual engine timing; release captures normal APK/startup/memory. The integration driver needs a VM service, so release does not fabricate a FrameTiming result. The wrapper restores `lib/main.dart` before measuring normal startup. Emulator profile measurements are engineering evidence only. [Flutter profiling](https://docs.flutter.dev/perf/ui-performance) recommends a physical device in profile mode; [integration profiling](https://docs.flutter.dev/cookbook/testing/integration/profiling) explains benchmark capture. Public documentation currently describes a newer Flutter version; the harness APIs were inspected in frozen Flutter 3.32.8 source.

Do not tune architecture/learning logic or add infrastructure to meet a cosmetic target. Optimize an identified bottleneck, rerun the same scenario/device/build mode, preserve both measurements, and obtain visual/accessibility review for any changed asset/effect.
