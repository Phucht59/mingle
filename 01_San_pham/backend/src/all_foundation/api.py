import logging
from contextlib import asynccontextmanager
from uuid import uuid4

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from all_foundation.config import Settings
from all_foundation.db import schema_ready
from all_foundation.logging import configure_logging
from all_foundation.storage import LocalObjectStore

log = logging.getLogger("api")


def create_app(settings: Settings | None = None):
    config = settings or Settings.from_env()

    @asynccontextmanager
    async def lifespan(app):
        configure_logging()
        log.info("api.started")
        yield
        log.info("api.stopped")

    app = FastAPI(title="Adaptive Learning Foundation", version="0.1.0", lifespan=lifespan)

    @app.middleware("http")
    async def request_context(request, call_next):
        request_id = str(uuid4())
        try:
            response = await call_next(request)
        except Exception:
            log.error("request.failed", extra={"request_id": request_id})
            response = JSONResponse({"error": "internal_error"}, status_code=500)
        response.headers["X-Request-ID"] = request_id
        log.info("request.completed", extra={"request_id": request_id})
        return response

    @app.get("/health/live")
    def live():
        return {"status": "alive"}

    @app.get("/health/ready")
    def ready():
        try:
            ok = schema_ready(config.database_url)
            ok = ok and LocalObjectStore(config.storage_root).healthcheck()
        except Exception:
            ok = False
        return JSONResponse(
            {"status": "ready" if ok else "not_ready"}, status_code=200 if ok else 503
        )

    # No unauthenticated domain/admin/worker submission routes.
    return app
