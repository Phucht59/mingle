# Android Studio emulator repair — 2026-09-30

## Latest verified environment — supersedes the older failure below

A later targeted repair placed the SDK in the physical ASCII directory `C:\Android\Sdk`, retained the previous SDK and junction, created the new **Mingo API 35** (`Mingo_API_35`) AVD with host GPU and persistent Vulkan-disabled configuration, and recorded Device Manager boot/Quick Boot success. See `03_Kiem_thu/Bang_chung/outputs/android-play-fix-20260930/status.json` and `device-manager-play-success.log` (Quick Boot 5986 ms).

This final-gate session reopened Android Studio; its log recorded new AVD restore/boot at 20:46:35 with boot time 7273 ms. ADB independently reported `emulator-5554 device` and `sys.boot_completed=1`. TalkBack 15.0.0.639625893 and Google TTS are installed; TalkBack is not enabled and no actual speech session has been run. Earlier guidance for the obsolete recovered AVD should not be used as the current start procedure.

This is supporting test-environment work requested by the user. It is not a Phase 2 production software deliverable or evidence that a Mingo application has been implemented. The sections below preserve the original diagnostic history.

## Diagnosis

The original suspicion that the non-ASCII SDK path caused the AVD process crash was incorrect. Android Studio's SDK setting was changed to the existing ASCII junction `C:\Android\Sdk` (backup: `C:\Mingo\03_Kiem_thu/Bang_chung/outputs\android-repair-20260930\android.sdk.path.before.xml`), but this was not the crash's root cause. The old SDK path and `C:\Android\Sdk` resolve to the same installed SDK.

Observed in Android Studio Device Manager: starting `Mingo API 35 (Recovered)` (`mingo_ascii_api35`) ended with “The emulator process for AVD mingo_ascii_api35 has terminated.” The Studio log showed:

- Software OpenGL library load failed (`Failed to load opengl32sw`), then fallback to system OpenGL.
- OpenGL selected NVIDIA GeForce GTX 1650 (driver 457.34), while Vulkan enumeration also detected the AMD Radeon(TM) integrated GPU.
- The emulator exited with code `-1073741819` (`0xC0000005`, access violation); ADB briefly reported `emulator-5554 offline` and then no device.

This initially pointed to the emulator's Vulkan/hybrid-GPU path. A later Studio retry inherited the Vulkan-disable setting (the Studio log explicitly says the feature is disabled) but still exited with the same access violation. Therefore the GPU path may contribute, but it is **not a confirmed complete root cause** for the Studio-managed launch. WHPX acceleration is available. The AVD data was not wiped.

## Repair and verification

- Set the recovered AVD graphics mode to `host`; backups of the prior config are in `C:\Mingo\03_Kiem_thu/Bang_chung/outputs\android-repair-20260930\`.
- Reproduced successful boot from CLI with `-gpu host -feature -Vulkan -cores 2 -memory 2048 -port 5554`: ADB reported `emulator-5554 device`, `sys.boot_completed=1`, and the Android 15 home screen rendered.
- Verified a persistent workaround through the Windows user environment variable `ANDROID_EMULATOR_FEATURES=-Vulkan`. A separate CLI boot inherited the variable; the emulator log explicitly said Vulkan was disabled and selected NVIDIA host GLES. It reached `sys.boot_completed=1` in 51.928 seconds, ADB reported `device`, and the Android home screen rendered.
- The environment workaround is experimentally verified for CLI launches. Studio was fully reopened and Play was tried; Studio still exited with `0xC0000005` even though its log confirmed Vulkan disabled. **Android Studio Device Manager Play remains failing.**
- Reproduced the Studio command-line options directly, including `-no-snapstorage`, `-qt-hide-window`, `-grpc-use-token`, and `-idle-grpc-timeout 300`, with the same AVD and Vulkan-disabled environment. That CLI-launched process reached ADB `device` and `sys.boot_completed=1`. So far, the failure is isolated to how the Studio-managed attempt behaves; no definitive lower-level cause is proven.
- The currently booted emulator was launched directly via CLI in a visible window. ADB reports `emulator-5554 device` and Android reports `sys.boot_completed=1`. Android Studio can use this running ADB target without pressing the AVD's Play button again. It is not itself a TalkBack session.

## Start it from Android Studio

1. The current visible emulator is already running. Do not click ▶ for the same AVD while it is running.
2. In Android Studio, wait for ADB to list `emulator-5554`; select that device in the run-target dropdown and run the app configuration. This checks app deployment to the running emulator, separate from Device Manager's failing start action.
3. To retry Device Manager later, first shut down the current emulator, then try **Cold Boot Now** and ▶ once. Preserve the latest `idea.log` timestamp and emulator crash dump if it fails again.
4. Run only one emulator at a time on this 16 GB host.

The verified direct fallback is:

```powershell
$env:ANDROID_HOME='C:\Android\Sdk'
$env:ANDROID_SDK_ROOT='C:\Android\Sdk'
$env:ANDROID_AVD_HOME='C:\Android\avd'
$env:ANDROID_EMULATOR_FEATURES='-Vulkan'
& 'C:\Android\Sdk\emulator\emulator.exe' -avd mingo_ascii_api35 -no-snapshot -gpu host -cores 2 -memory 2048 -port 5554
```

Do not start a second instance while one is running. Android boot/ADB is not TalkBack evidence. For the accessibility gate, use `TALKBACK_MANUAL_RUNBOOK.md` and record actual audible speech and focus behavior. TalkBack remains **BLOCKED BY ENVIRONMENT / NOT RUN**, not PASS.
