# Preserved diagnostic history — 2026-09-26

- `analyze-20260926T093040Z.log`: initial missing `flutter_lints` defect (II-11).
- `build-apk-debug-20260926T093151Z.log`: initial Windows Java temp/socket failure
  (II-12). JDK17 alone was insufficient; the ASCII temp directory fixed the build.
- `android-runtime-20260926.redacted.log`: `flutter run --no-resident` built and
  installed successfully but returned **2** after debugger service disconnection.
  The subsequent independent adb cold-start/process/UI verification passed; the
  failed Flutter debugger command is not represented as a successful run.

The final local run logs are dated `20260926T100348Z`. Additional superseded
diagnostics remain in ignored `.local/debug-evidence`; historical tracked evidence
was not overwritten. The raw browser DOM is retained there because it contains
local debug connection details; the committed screenshot records visible output.
