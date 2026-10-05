from concurrent.futures import ThreadPoolExecutor
from uuid import UUID

import pytest
from fastapi.testclient import TestClient

from all_foundation.api import create_app
from all_foundation.config import Settings
from all_foundation.storage import LocalObjectStore


def test_health_does_not_claim_readiness_without_database(tmp_path):
    app = create_app(Settings("postgresql://invalid:invalid@127.0.0.1:1/absent", tmp_path))
    with TestClient(app) as client:
        response = client.get("/health/live", headers={"X-Request-ID": "untrusted"})
        assert response.status_code == 200
        UUID(response.headers["X-Request-ID"])
        response = client.get("/health/ready")
        assert response.status_code == 503
        assert response.json() == {"status": "not_ready"}
        assert "invalid" not in response.text
        assert client.post("/commands", json={"score": 100}).status_code == 404


@pytest.mark.parametrize("key", ["", ".", "../secret", "/etc/passwd", "a/../../secret", "a\\b"])
def test_storage_rejects_unsafe_paths(tmp_path, key):
    with pytest.raises(ValueError):
        LocalObjectStore(tmp_path).put_if_absent(key, b"data")


def test_storage_rejects_symlink_escape(tmp_path):
    root = tmp_path / "objects"
    root.mkdir()
    try:
        (root / "escape").symlink_to(tmp_path, target_is_directory=True)
    except OSError as error:
        if getattr(error, "winerror", None) == 1314:
            pytest.skip("Windows symlink creation requires an unavailable privilege")
        raise
    with pytest.raises(ValueError):
        LocalObjectStore(root).get("escape/secret")


def test_storage_concurrent_publish_is_immutable(tmp_path):
    store = LocalObjectStore(tmp_path)
    values = [str(i).encode() * 10000 for i in range(16)]
    with ThreadPoolExecutor(max_workers=8) as pool:
        results = list(pool.map(lambda b: store.put_if_absent("revision/audio", b), values))
    assert sum(results) == 1
    assert store.get("revision/audio") == values[results.index(True)]
    assert not list(tmp_path.glob(".write-*"))
    assert store.healthcheck()


def test_missing_config_fails_closed(monkeypatch):
    monkeypatch.delenv("DATABASE_URL", raising=False)
    with pytest.raises(ValueError, match="PostgreSQL"):
        Settings.from_env()
