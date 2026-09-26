# Local runtime and fresh-clone reproduction

Use Python 3.12, Flutter 3.32.8 / Dart 3.8.1, JDK 17, Android SDK API 35,
an Android device/emulator, and Chrome. PostgreSQL 18 was verified on Windows;
CI uses PostgreSQL 16.10. Install toolchains independently of the repository.
See [Windows Flutter](WINDOWS_FLUTTER.md) for the verified Windows path settings.

## Fresh setup

Clone `https://github.com/Phucht59/mingo.git` into an empty directory. Follow the
root README to create a new `.venv`, install the lock, provision `mingo_app`,
`mingo`, and `mingo_test`, and create an ignored `05_code/.env`. Never copy a
previous `.venv`, `.dart_tool`, `build`, pytest cache, object store, or database.
For isolated reproduction, use a freshly initialized PostgreSQL server on an
unused port with the same canonical role/database names. Put that port and new
generated credentials in the new `.env`; do not reuse the main server's data.

Run the root README's backend verifier with `-RunPostgres`, bootstrap the Flutter
hosts, then run the Flutter verifier. The scripts write actual evidence under
`06_quality/evidence`. Run the original V3.2 suites with the isolated environment
described in `V3_2_VERIFICATION.md`; their exact sources are now preserved in the repo.

## API and worker on Windows

In each terminal, start at the repository root and load the ignored environment:

```powershell
foreach ($line in Get-Content -LiteralPath 05_code/.env) {
  if ($line -match '^([^#=]+)=(.*)$') {
    [Environment]::SetEnvironmentVariable($Matches[1], $Matches[2], 'Process')
  }
}
.\.venv\Scripts\python.exe -m all_foundation.cli migrate
```

Start the API in the first terminal:

```powershell
.\.venv\Scripts\python.exe -m uvicorn all_foundation.api:create_app --factory --host 127.0.0.1 --port 8000
```

Start the durable worker in a second terminal after loading the same environment:

```powershell
.\.venv\Scripts\python.exe -m all_foundation.worker
```

In a third terminal with the same environment:

```powershell
Invoke-WebRequest http://127.0.0.1:8000/health/live
Invoke-WebRequest http://127.0.0.1:8000/health/ready
.\.venv\Scripts\python.exe -m all_foundation.cli enqueue-probe --key manual-boot
.\.venv\Scripts\python.exe -m all_foundation.worker --healthcheck
```

Both HTTP checks must return 200. The worker logs `job.completed` for the probe.
Stop the long-lived processes with Ctrl+C. On Linux/macOS, export the `.env`
values (`set -a; source 05_code/.env; set +a`) and substitute `.venv/bin/python`.

## Learner and staff actual boot

After bootstrap and verification, start an Android emulator or connect a device:

```powershell
flutter devices
Set-Location 05_code/apps/learner
flutter run -d <android-device-id>
```

Confirm the learner shows `Your learning space` with no startup crash. In a
separate terminal from the root:

```powershell
Set-Location 05_code/apps/staff
flutter run -d chrome
```

Confirm `Learning workspace` renders. These are Phase 1 shells; there are no
additional feature routes to validate. A successful build alone is insufficient:
record the actual target, process startup, visible UI and any debugger limitation.

For a built APK, `adb install -r <apk>` and `adb shell am start -W -n
com.example.adaptive_learner/.MainActivity` provide an independent runtime check.
A built Web app can be served with Python's `http.server` and opened in Chrome.
Keep temporary browser profiles, APKs, generated hosts and caches out of Git.
