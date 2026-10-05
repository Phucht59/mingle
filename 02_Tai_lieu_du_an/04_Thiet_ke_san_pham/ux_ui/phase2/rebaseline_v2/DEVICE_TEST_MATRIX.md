# Device and refresh-rate test matrix

2026-10-02 · E4 engineering coverage. Hardware discovery below was independently rerun now; older debug integration logs remain historical evidence. No physical Android device was attached during this audit. **PHYSICAL DEVICE PERFORMANCE PENDING.**

| Target | Actual discovered hardware / condition | 60 Hz | 90 Hz | 120 Hz | Status |
|---|---|---|---|---|---|
| LOW physical | QA must select a supported budget Android representative of recruited users; record model/SoC/RAM/Android/refresh/thermal condition | UNMEASURED | UNMEASURED | UNMEASURED | Physical device pending; no model invented |
| MID physical | QA must select a common Android representative using actual recruitment/device evidence | UNMEASURED | UNMEASURED | UNMEASURED | Physical device pending |
| HIGH physical | QA must select a real high-refresh Android; record active rate rather than marketing maximum | UNMEASURED | UNMEASURED | UNMEASURED | Physical device pending |
| Mingo_API_35 emulator | x86_64/API35, 4 virtual CPUs, 2GiB configured RAM, 1080×2400, density420; active display approximately60Hz; GoogleSwiftShader software renderer | CAPABILITY OBSERVED; FRAMES NOT RUN | UNMEASURED | UNMEASURED | Task-owned emulator online; engineering only |

An AVD setting is not observed refresh and cannot prove sustained frame delivery. Record FlutterView.display.refreshRate and Android display service readout during a real run. Emulator architecture x86_64 supports profile/release in the installed Flutter3.32.8 AndroidDevice implementation; the x86 variant supports debug only. No change of SDK or hardware scoring algorithm is needed.

After the initial audit, a task-owned read-only AVD was launched headlessly with no audio and `swiftshader_indirect`; bounded launch returned exit0, emulator-5554 online, launcher PID13884. [Preparation evidence](../../../../../03_Kiem_thu/QA_QC/phase2/evidence_gated_20261002/performance/PREPARED_SCRIPT_STATUS.json) records this actual result. This changes device availability only: no frame/refresh/physical-performance claim follows from successful boot.

A subsequent [read-only metadata capture](../../../../../03_Kiem_thu/QA_QC/phase2/evidence_gated_20261002/performance/DEVICE_METADATA_INITIAL.json) observed qemu1, model sdk_gphone64_x86_64 and active renderFrameRate60.000004Hz with no90/120Hz supportedmode. Renderer is GoogleSwiftShader software OpenGLES3.0. These are actual capability/context values; frame delivery still needs the profile run, and they do not represent LOW/MID/HIGH physical hardware.

## Scenarios for every selected physical device

| Scenario | Automated method | Independent/manual requirement |
|---|---|---|
| Process cold launch | Five force-stop / `am start -W` samples of normal app; PID and build hash | Observe initial-display/content readiness; no app-data deletion |
| Warm launch / background resume | HOME key then launcher start; accept warm sample only if PID unchanged | Observe state continuity, no blank/stuck surface, lifecycle interruption |
| Home scroll | Actual flings in the rendered scrollable, raw UI/raster timings | Thumb scroll, display consistency and thermal context |
| Home → Lesson | Tap current primary action, actual route transition | Visible continuity and no lost context |
| Answer / feedback | Select answer and submit; record separate timing windows | Input latency and feedback announcement, no semantic change |
| Lesson → Result | Actual sample Review/Learn/Retrieve/Transfer/Check journey | Meaningful completion and honest observed evidence |
| Course scroll | Repeated rendered journey scroll | Path meaning, legibility, locked/completed labels |
| 200% text | Explicit scale2 preview plus scroll frame capture | Real Android font size and TalkBack core journey |
| Offline surface | Explicit offline fixture render | Actual durable queue/network/restart semantics are Phase6; no fabricated sync |
| Battery/thermal | Before/after battery and thermal service snapshots | Physical sustained session, charging/temperature/background apps controlled |

The current benchmark tests presentation with sample content. Profile harness action wall time includes tester scrolling/settling and does not measure cognitive response time. Manual TalkBack and physical listening cannot be inferred from these timings. Log build mode, candidate source/asset hashes, device alias, model/ABI/API, active refresh, RAM/PSS, renderer, brightness, charge/thermal context and excluded scenarios. Redact participant/account identifiers; collect no lesson-answer telemetry from real users.

## Commands for QA

```powershell
& .\04_Van_hanh\Scripts\run_performance_benchmark.ps1 -Device '<adb-device-id>' -DeviceTier LOW -BuildMode Profile
& .\04_Van_hanh\Scripts\run_performance_benchmark.ps1 -Device '<adb-device-id>' -DeviceTier LOW -BuildMode Release -BuildAab
```

Use a fresh timestamped evidence directory for each run; preserve failures and pre/post-optimization captures. Release local generated signing is a test build, not production distribution. Compare equivalent ABI/build/refresh/device conditions; do not compare a universal debug APK with a release arm64 APK as a runtime improvement.

## Final local execution2026-10-03

Current source ran on task-owned headless read-only sdk_gphone64_x86_64/API35/1080×2400/DPR2.625/GoogleSwiftShader, actual60.000004Hz. Default engine profile and normal profile/release five cold/five warm measurements completed; Androidboot/audioinit2PASS. This is engineering coverage only. Software raster misses candidate60Hz budget;90/120Hzunsupported here. PhysicalLOW/MID/HIGH,realTalkBack/gestures/hearing/energy/thermal/ten-journeyPSSremainPENDING. Exact numbers/provenance: [PERFORMANCE_TEST_REPORT.md](PERFORMANCE_TEST_REPORT.md).
