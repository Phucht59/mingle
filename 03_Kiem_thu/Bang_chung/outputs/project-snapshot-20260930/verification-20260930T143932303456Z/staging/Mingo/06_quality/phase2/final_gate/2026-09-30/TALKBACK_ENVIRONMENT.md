# Interactive assistive technology environment — 2026-09-30

**Interactive TalkBack = BLOCKED BY ENVIRONMENT. Not run; not PASS and not a product FAIL.**

Latest environment update: new **Mingo API 35** (`Mingo_API_35`) boots through Android Studio after a later SDK/AVD repair. Reopening Studio in this session restored the emulator in 7273 ms; ADB reported `device` and `sys.boot_completed=1`. TalkBack 15.0.0.639625893 and Google TTS are installed, but actual speech/focus has not been tested. The earlier paragraphs below record older attempts and are superseded for emulator availability. The AT session itself remains NOT RUN. Emulator work is supporting test tooling; Phase 2 deliverables remain UX/UI specifications and a mock reference prototype.

Android Studio is installed at `C:/Program Files/Android/Android Studio/bin/studio64.exe`. Its SDK path was updated from the non-ASCII user path to the existing ASCII junction `C:/Android/Sdk` after saving a backup. A dedicated `mingo_ascii_api35` AVD is registered in Device Manager as `Mingo API 35 (Recovered)`; no AVD data was wiped.

ADB initially showed multiple offline emulator instances. The AVD is now configured for host graphics and the persistent user variable `ANDROID_EMULATOR_FEATURES=-Vulkan` is set. Android Studio was restarted and its log confirmed Vulkan disabled, but Device Manager Play still exited with `0xC0000005`. A direct launch with Studio's equivalent command-line options did boot to `sys.boot_completed=1`; a visible emulator launched directly is now available as ADB target `emulator-5554 device`. It can be used to run the app from Studio, but this does not repair or validate the Device Manager start action. Details are in `ANDROID_STUDIO_EMULATOR_REPAIR.md`.

No enabled tool supplies an interactive Android TalkBack speech recording/listening session. TalkBack has not been enabled and its speech/focus behavior has not been observed. ADB/device boot and screenshots cannot establish real AT PASS.

No accessibility setting was silently enabled/disabled, no real speech result recorded, no Chromium AX tree substituted. Headless Chrome reflow measurements are separate evidence.

Use `TALKBACK_MANUAL_RUNBOOK.md` and `TALKBACK_EVIDENCE_TEMPLATE.md`. Once a tester has a responsive Android device/emulator with audible TalkBack, record real speech, focus and status behavior before claiming PASS. A staff desktop screen-reader session must also be recorded.

Queued question for the AT step (not a gate approval): “Bạn có thể chạy TalkBack trên máy Android thật/emulator có speech không? Nếu có, tôi sẽ hướng dẫn từng bước và chờ kết quả trước khi tiếp tục gate.”
