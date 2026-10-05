# Chạy và kiểm tra nền tảng Phase 1

Các lệnh dưới đây chạy từ root repository. Đây là hướng dẫn môi trường và kiểm tra; trạng thái phase nằm trong tài liệu tiến độ và gate.

## Canonical database topology

One PostgreSQL server supports one Mingo system:

| Purpose | Name |
|---|---|
| Application role | `mingo_app` |
| Local application database | `mingo` |
| Disposable automated-test database | `mingo_test` |

Development phases never create separate application databases. Runtime reads
`DATABASE_URL`; destructive tests read `TEST_DATABASE_URL` and refuse a database whose
name does not end in `_test`.

Copy `01_San_pham/.env.example` to ignored `01_San_pham/.env`, generate a strong local password,
and replace `CHANGE_ME`. Never commit the resulting file. A PostgreSQL administrator can
provision the local roles once with:

```sql
CREATE ROLE mingo_app WITH LOGIN PASSWORD '<local-random-password>';
CREATE DATABASE mingo OWNER mingo_app;
CREATE DATABASE mingo_test OWNER mingo_app;
```

Docker users can set `MINGO_APP_PASSWORD` in `01_San_pham/.env` and run:

```sh
cd 01_San_pham
docker compose up --build -d
```

Compose creates `mingo` and initializes `mingo_test` on a fresh PostgreSQL volume.

## Backend setup and verification

The canonical Python is 3.12. On Windows PowerShell:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r 01_San_pham/backend/requirements.lock
python -m pip install --no-deps .\01_San_pham\backend
.\04_Van_hanh\Scripts\verify_backend.ps1 `
  -Python .\.venv\Scripts\python.exe -RunPostgres
```

The PostgreSQL run migrates `mingo`, uses only `mingo_test` for destructive integration
tests, processes a durable worker probe, requires API readiness HTTP 200, and records
timestamped evidence under `03_Kiem_thu/Bang_chung/{backend,postgres,api,worker}`.

For persistent API/worker processes and client launch commands, follow
[`LOCAL_RUNTIME.md`](LOCAL_RUNTIME.md).

Linux/macOS CI uses:

```sh
RUN_POSTGRES=1 bash 04_Van_hanh/Scripts/verify_backend.sh
```

## Flutter setup and verification

Use Flutter 3.32.8 with Dart 3.8.1. Bootstrap deliberately untracked Android/Web host
files while preserving authored `lib/`, `test/`, `integration_test/`, manifests, locks,
and analyzer policy:

```powershell
.\04_Van_hanh\Scripts\bootstrap_clients.ps1 `
  -Flutter C:\path\to\flutter\bin\flutter.bat
.\04_Van_hanh\Scripts\verify_flutter.ps1 `
  -Flutter C:\path\to\flutter\bin\flutter.bat
```

The verifier runs pub resolution, analysis, tests, learner debug APK build, and staff Web
build. Actual Android and browser boot evidence belongs under
`03_Kiem_thu/Bang_chung/flutter/{learner,staff}`.

