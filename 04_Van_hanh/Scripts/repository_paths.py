"""Resolve captured pre-restructure paths without rewriting historical evidence."""
import hashlib
import json
from functools import lru_cache


@lru_cache(maxsize=None)
def metadata(root):
    audit = root / "02_Tai_lieu_du_an/07_Tien_do_du_an/Tai_cau_truc_20261001"
    baseline = audit / "RESTRUCTURE_BASELINE.json"
    ledger = audit / "PATH_ADAPTATIONS.json"
    if not baseline.is_file():
        return {}, {}
    mapping = json.loads(baseline.read_text(encoding="utf-8"))["mapping"]
    adaptations = json.loads(ledger.read_text(encoding="utf-8")) if ledger.is_file() else []
    return mapping, {item["old"]: item for item in adaptations}


def captured_path(root, name):
    mapping, _ = metadata(root)
    for old, new in sorted(mapping.items(), key=lambda pair: -len(pair[0])):
        if name == old or name.startswith(old + "/"):
            return new + name[len(old):]
    return name


def captured_digest(root, name):
    """Return captured bytes' digest only if current bytes match the recorded move.

    Unrecorded content changes fail the caller's original protected hash check.
    This accepts only explicitly recorded path/navigation adaptations.
    """
    path = root / captured_path(root, name)
    if not path.is_file():
        return None
    actual = hashlib.sha256(path.read_bytes()).hexdigest()
    _, adaptations = metadata(root)
    item = adaptations.get(name)
    if item and actual == item["after_sha256"]:
        return item["before_sha256"]
    return actual
