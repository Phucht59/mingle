# Windows Flutter 3.32.8 runtime notes

## Required toolchain

- Flutter 3.32.8 / Dart 3.8.1
- Android SDK platform 35 and build tools 35
- JDK 17 for Flutter/Gradle
- Chrome for staff Web runtime
- Android emulator or device for learner runtime

Run `bootstrap_clients.ps1` before `verify_flutter.ps1`. Generated Android/Web host files
are ignored by repository policy; authored manifests, locks, analyzer policy, `lib/`, and
tests are tracked.

## Windows profiles containing Unicode characters

OpenJDK on the verified host could not create the Unix-domain socket used by Gradle when
`java.io.tmpdir` resolved below the `Phúc` user profile. `verify_flutter.ps1` sets `TEMP`,
`TMP`, and `java.io.tmpdir` to the ASCII repository path `.local/java-tmp` for the command.
This directory is ignored.

For manual `flutter run` or Gradle commands in a new PowerShell terminal, set all
three values together before launching the command (the verifier's process settings
do not configure other terminals):

```powershell
New-Item -ItemType Directory -Force C:\Mingo\.local\java-tmp | Out-Null
$env:TEMP = 'C:\Mingo\.local\java-tmp'
$env:TMP = $env:TEMP
$env:JAVA_TOOL_OPTIONS = "-Djava.io.tmpdir=$env:TEMP"
```

Use the corresponding ASCII checkout path when your repository is elsewhere.

The same host required an ASCII AVD home for reliable emulator boot:

```powershell
$env:ANDROID_HOME = "C:\Android\Sdk"
$env:ANDROID_SDK_ROOT = "C:\Android\Sdk"
$env:ANDROID_AVD_HOME = "C:\Android\avd"
```

`C:\Android\Sdk` may be a junction to the installed SDK. Create the AVD under
`C:\Android\avd`, confirm `emulator -accel-check`, then require
`adb shell getprop sys.boot_completed` to return `1` before installing the learner APK.

These are host-path fixes only. They do not modify application behavior or V3.2 rules.
