import os
from dataclasses import dataclass, field
from pathlib import Path


@dataclass(frozen=True)
class Settings:
    database_url: str = field(repr=False)
    storage_root: Path
    environment: str = "development"
    worker_id: str = "foundation-worker"
    lease_seconds: int = 30
    max_attempts: int = 3

    @classmethod
    def from_env(cls):
        url = os.environ.get("DATABASE_URL", "")
        if not url.startswith(("postgresql://", "postgres://")):
            raise ValueError("DATABASE_URL must be a PostgreSQL connection URI")
        return cls(
            database_url=url,
            storage_root=Path(os.environ.get("OBJECT_STORAGE_ROOT", "./.local/objects")),
            environment=os.environ.get("APP_ENV", "development"),
            worker_id=os.environ.get("WORKER_ID", "foundation-worker"),
        )
