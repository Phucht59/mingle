from __future__ import annotations
from pathlib import Path
import hashlib
import sys

root = Path(__file__).resolve().parents[2]
manifest = root / "08_handoff" / "phase2" / "MANIFEST_SHA256.txt"
if not manifest.is_file():
    print("FAIL: missing manifest", file=sys.stderr)
    sys.exit(1)

expected: dict[str, str] = {}
for raw in manifest.read_text(encoding="utf-8").splitlines():
    line = raw.strip()
    if not line or line.startswith("#"):
        continue
    try:
        digest, rel = line.split("  ", 1)
    except ValueError:
        print(f"FAIL: malformed manifest line: {raw}", file=sys.stderr)
        sys.exit(1)
    expected[rel] = digest

errors: list[str] = []
for rel, digest in expected.items():
    p = root / rel
    if not p.is_file():
        errors.append(f"missing: {rel}")
        continue
    got = hashlib.sha256(p.read_bytes()).hexdigest()
    if got != digest:
        errors.append(f"hash mismatch: {rel}")

# All package files must be in the manifest except the manifest itself.
actual = {
    str(p.relative_to(root)).replace("\\", "/")
    for p in root.rglob("*")
    if p.is_file() and p != manifest
}
extra = sorted(actual - set(expected))
missing_from_tree = sorted(set(expected) - actual)
if extra:
    errors.append("unmanifested files: " + ", ".join(extra[:20]))
if missing_from_tree:
    errors.append("manifest entries absent from tree: " + ", ".join(missing_from_tree[:20]))

if errors:
    print("FAIL")
    for e in errors:
        print("-", e)
    sys.exit(1)

print(f"PASS: {len(expected)} files match manifest; no unmanifested package files")
