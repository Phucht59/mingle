import argparse
import json
from uuid import uuid4

from all_foundation.config import Settings
from all_foundation.db import migrate
from all_foundation.storage import LocalObjectStore
from all_foundation.worker import enqueue


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["migrate", "enqueue-probe", "storage-smoke"])
    parser.add_argument("--key", default="boot-probe")
    args = parser.parse_args()
    config = Settings.from_env()
    if args.action == "migrate":
        print(json.dumps({"applied": migrate(config.database_url)}))
    elif args.action == "enqueue-probe":
        print(json.dumps({"job_id": str(enqueue(config.database_url, args.key))}))
    else:
        store = LocalObjectStore(config.storage_root)
        key = f"smoke/{uuid4()}"
        assert store.put_if_absent(key, b"foundation")
        assert store.get(key) == b"foundation"
        assert not store.put_if_absent(key, b"overwrite")
        print(json.dumps({"adapter": "local-object-store", "smoke": "passed"}))


if __name__ == "__main__":
    main()
