import os
import tempfile
from pathlib import Path, PurePosixPath
from typing import Protocol


def _resolved_path(path: Path) -> Path:
    resolved = path.resolve()
    if os.name == "nt":
        value = str(resolved)
        if value.startswith("\\\\?\\UNC\\"):
            value = "\\\\" + value[8:]
        elif value.startswith("\\\\?\\"):
            value = value[4:]
        resolved = Path(value)
    return resolved


class ObjectStore(Protocol):
    def put_if_absent(self, key: str, data: bytes) -> bool: ...
    def get(self, key: str) -> bytes: ...


class LocalObjectStore:
    """Local development adapter; immutable keys and atomic publication."""

    def __init__(self, root: Path):
        self.root = _resolved_path(root)
        self.root.mkdir(parents=True, exist_ok=True)

    def _path(self, key: str):
        p = PurePosixPath(key)
        if not key or p.is_absolute() or ".." in p.parts or "\\" in key:
            raise ValueError("Invalid object key")
        target = self.root.joinpath(*p.parts)
        if not _resolved_path(target).is_relative_to(self.root) or target == self.root:
            raise ValueError("Object key escapes storage root")
        return target

    def put_if_absent(self, key: str, data: bytes):
        target = self._path(key)
        target.parent.mkdir(parents=True, exist_ok=True)
        fd, name = tempfile.mkstemp(prefix=".write-", dir=target.parent)
        try:
            with os.fdopen(fd, "wb") as stream:
                stream.write(data)
                stream.flush()
                os.fsync(stream.fileno())
            try:
                os.link(name, target)
            except FileExistsError:
                return False
            # POSIX can flush the directory entry after linking. Windows does not
            # expose O_DIRECTORY; the file itself was flushed before publication.
            if hasattr(os, "O_DIRECTORY"):
                directory_fd = os.open(target.parent, os.O_RDONLY | os.O_DIRECTORY)
                try:
                    os.fsync(directory_fd)
                finally:
                    os.close(directory_fd)
            return True
        finally:
            os.unlink(name)

    def get(self, key: str):
        return self._path(key).read_bytes()

    def healthcheck(self):
        fd, name = tempfile.mkstemp(prefix=".health-", dir=self.root)
        try:
            with os.fdopen(fd, "wb") as stream:
                stream.write(b"ok")
            return Path(name).read_bytes() == b"ok"
        finally:
            os.unlink(name)
