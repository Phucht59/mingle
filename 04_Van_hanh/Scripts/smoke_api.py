"""Boot a real Uvicorn process, check HTTP, and stop it gracefully."""
import argparse
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

repo_root = Path(__file__).resolve().parents[2]
parser = argparse.ArgumentParser()
parser.add_argument(
    "--expect-ready",
    action="store_true",
    help="Use DATABASE_URL from the environment and require readiness HTTP 200.",
)
args = parser.parse_args()

evidence = repo_root / "03_Kiem_thu/Bang_chung/api"
evidence.mkdir(parents=True, exist_ok=True)
run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
commit = subprocess.run(
    ["git", "rev-parse", "HEAD"],
    cwd=repo_root,
    check=True,
    capture_output=True,
    text=True,
).stdout.strip()
process_log = evidence / f"api-process-{run_id}.log"
http_result = evidence / f"api-http-smoke-{run_id}.json"
env = dict(os.environ, OBJECT_STORAGE_ROOT=str(repo_root / ".local" / "objects"))
if args.expect_ready:
    if not env.get("DATABASE_URL"):
        raise SystemExit("DATABASE_URL is required with --expect-ready")
else:
    env["DATABASE_URL"] = "postgresql://unused:unused@127.0.0.1:1/absent"
with process_log.open("w") as log:
    process = subprocess.Popen(
        [
            sys.executable,
            "-m",
            "uvicorn",
            "all_foundation.api:create_app",
            "--factory",
            "--port",
            "8018",
            "--no-access-log",
        ],
        env=env,
        stdout=log,
        stderr=log,
    )
    try:
        result = {"commit": commit}
        for _attempt in range(50):
            try:
                urllib.request.urlopen("http://127.0.0.1:8018/health/live", timeout=1)
                break
            except urllib.error.URLError:
                if process.poll() is not None:
                    raise RuntimeError("API exited during startup")
                time.sleep(0.1)
        for endpoint in ("live", "ready"):
            try:
                response = urllib.request.urlopen(
                    "http://127.0.0.1:8018/health/" + endpoint, timeout=5
                )
            except urllib.error.HTTPError as error:
                response = error
            result[endpoint] = {
                "status": response.status,
                "body": json.loads(response.read()),
                "request_id": response.headers["X-Request-ID"],
            }
        assert result["live"]["status"] == 200
        assert result["ready"]["status"] == (200 if args.expect_ready else 503)
        http_result.write_text(json.dumps(result, indent=2), encoding="utf-8")
        print(json.dumps(result))
    finally:
        process.terminate()
        process.wait(timeout=10)
