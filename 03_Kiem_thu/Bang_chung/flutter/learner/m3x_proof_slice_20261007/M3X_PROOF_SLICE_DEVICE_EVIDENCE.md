# M3.X proof slice — device evidence

**DEVICE PASS: NOT ESTABLISHED.** No iOS simulator or physical iPhone test was executed in this Windows task. Owner reports an iPhone Air on iOS 27 beta; that report is retained as target availability, not observed device evidence.

| Field | Execution record |
|---|---|
| Target model | iPhone Air — owner reported |
| iOS version | iOS 27 beta — owner reported; exact beta number/build UNKNOWN |
| Mac / macOS / Xcode | Access and versions UNKNOWN; question pending |
| Flutter / Dart | Source prepared with Flutter 3.32.8 / Dart 3.8.1 |
| iOS build mode | NOT BUILT; no debug/profile/release binary |
| Signing / team / bundle | NOT CONFIGURED; generated placeholder `com.example.adaptiveLearner` |
| Generated minimum target | 12.0 in standard host template; not a verified compatibility claim |
| Text size | Device UNKNOWN / NOT EXECUTED |
| VoiceOver | NOT EXECUTED |
| Reduce Motion | Device NOT EXECUTED |
| Reduce Transparency | Device NOT EXECUTED |
| Increased contrast / dark | Device NOT EXECUTED |
| Native transitions/gestures | NOT EXECUTED |
| Haptics / performance | NOT EXECUTED; no FPS/input-latency claim |
| Actual iPhone app termination | NOT EXECUTED |

## Actual host evidence

Windows Flutter reports Windows, Chrome and Edge only (`devices.log`). `doctor.log` and `flutter_version.log` retain the environment. The standard iOS host was generated in an isolated source copy; `ios_host_preparation.log` records it. `IOS_BUILD_INPUT_SOURCE_MATCH.json` confirms all 36 copied authored/dependency asset files match their source hashes. Generated values and source equality do not prove compilation.

The attempted iOS build cannot run here: `ios_build_command_unavailable.log` records “Could not find a subcommand named "ios" for "flutter build".” Exit 64. The earlier flag-bearing attempt is also retained in `ios_build_host_limit.log`.

The host process probe did terminate the Dart process (recorded PID 20756, exit 15) and launch a new reader. The exact snapshot compares equal, including revision IDs, command bytes, first and assisted retry responses, pending states and Home offset 137. See `PROCESS_DEATH_HOST.json`. This is a separate host process/storage test, not background/foreground and not native iPhone process-death acceptance.

## Captures available

Fourteen unedited widget-render PNGs are in `screenshots/`: Home Resume, Practice default/selected, incorrect/correct feedback, Independent Check, Result, Result Pending Sync, Sync Recovery pending/ACKed, 3.2× large text at 320 points, long bilingual text at 2×/320 points, dark feedback and Welcome. `HOST_CAPTURE_CONTACT_SHEET.jpg` is an overview derived from those PNGs. No native status bar/device frame or physical-device provenance is implied.

Host fonts substitute Inter for Cupertino system font names in tests only; the actual application retains platform fonts. Some isolated harness captures retain the Flutter debug banner/default Cupertino primary color. Screenshots prove the rendered state at capture and do not certify exact device typography/colors.

Required physical interaction videos are **NOT EXECUTED / NOT CAPTURED**:

1. Select → submit → inline Feedback, including VoiceOver audio/focus.
2. Close → same Home origin → Resume.
3. Pending → connection restored → still pending → explicit ACK → synced.
4. Saved pending state → actual force termination → icon relaunch → Resume with exact original state.

Follow [M3X_IPHONE_RUNBOOK.md](M3X_IPHONE_RUNBOOK.md). Add a new timestamped device run with source manifest, exact device/build/settings and raw evidence; do not rewrite this unexecuted record into a pass.
