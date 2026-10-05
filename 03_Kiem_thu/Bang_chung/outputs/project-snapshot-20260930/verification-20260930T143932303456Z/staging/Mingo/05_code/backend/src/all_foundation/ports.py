from typing import Protocol


class CanonicalCommandPort(Protocol):
    """Reserved boundary. Exact envelope and authorization depend on V3.2."""

    def execute(self, command: object) -> object: ...


class TelemetryPort(Protocol):
    """Separate ingestion interface; cannot authorize score or progress."""

    def record(self, observation: object) -> None: ...
