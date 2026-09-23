"""Boot a real Uvicorn process, check HTTP, stop gracefully. No database required."""
import json
import os
from pathlib import Path
import subprocess
import sys
import time
import urllib.error
import urllib.request

root = Path(__file__).resolve().parents[1]
env = dict(os.environ, DATABASE_URL='postgresql://unused:unused@127.0.0.1:1/absent',
           OBJECT_STORAGE_ROOT=str(root / '.local/objects'))
with (root / 'evidence/api-process.log').open('w') as log:
    process = subprocess.Popen([sys.executable, '-m', 'uvicorn',
        'all_foundation.api:create_app', '--factory', '--port', '8018', '--no-access-log'],
        env=env, stdout=log, stderr=log)
    try:
        result = {}
        for attempt in range(50):
            try:
                urllib.request.urlopen('http://127.0.0.1:8018/health/live', timeout=1)
                break
            except urllib.error.URLError:
                if process.poll() is not None:
                    raise RuntimeError('API exited during startup')
                time.sleep(.1)
        for endpoint in ('live', 'ready'):
            try:
                response = urllib.request.urlopen('http://127.0.0.1:8018/health/' + endpoint, timeout=5)
            except urllib.error.HTTPError as error:
                response = error
            result[endpoint] = {'status': response.status, 'body': json.loads(response.read()),
                                'request_id': response.headers['X-Request-ID']}
        assert result['live']['status'] == 200
        assert result['ready']['status'] == 503
        (root / 'evidence/api-http-smoke.json').write_text(json.dumps(result, indent=2))
        print(json.dumps(result))
    finally:
        process.terminate()
        process.wait(timeout=10)
