"""Verify immutable V3.2 originals, then execute their unchanged suites on a copy."""
import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "04_architecture/contracts/v3_2/source"
SUMS = ROOT / "08_handoff/provenance/v3_2/SHA256SUMS.txt"


def verify_source(source=SOURCE, sums=SUMS):
    expected = {}
    for line in sums.read_text(encoding="utf-8").splitlines():
        digest, name = line.split("  ", 1)
        path = source / name
        if not path.resolve().is_relative_to(source.resolve()):
            raise ValueError("Checksum path outside source")
        if name in expected or len(digest) != 64:
            raise ValueError("Invalid checksum inventory")
        expected[name] = digest
    actual = {p.relative_to(source).as_posix() for p in source.rglob("*") if p.is_file()}
    if not expected or actual != set(expected):
        raise ValueError("Original source inventory missing or changed")
    for name, digest in expected.items():
        if hashlib.sha256((source / name).read_bytes()).hexdigest() != digest:
            raise ValueError("Original source checksum mismatch: " + name)
    manifest = json.loads((source / "MANIFEST.json").read_text(encoding="utf-8"))
    return manifest, len(expected)


def validate_report(report, kind, expected_count):
    checks = report["checks"]
    passed = sum(c.startswith("PASS ") if kind == "contract" else c["status"] == "PASS" for c in checks)
    failed = len(checks) - passed
    if (report["passed"], report["failed"]) != (passed, failed):
        raise ValueError(kind + " report counters disagree with actual check results")
    if failed or passed != expected_count:
        raise ValueError(f"{kind} gate: {passed} passed, {failed} failed; expected {expected_count} checks")
    return {"passed": passed, "failed": failed, "total": len(checks)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--integrity-only", action="store_true")
    args = parser.parse_args()
    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    evidence = ROOT / "06_quality/evidence/v3_2" / run_id
    evidence.mkdir(parents=True)
    result = {
        "utc": datetime.now(timezone.utc).isoformat(),
        "commit": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
        "working_tree_dirty": bool(subprocess.check_output(["git", "status", "--porcelain"], cwd=ROOT)),
        "adapter_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "python": sys.version,
        "status": "FAILED",
        "commands": [],
    }
    env = os.environ.copy()
    env["PYTHONUTF8"] = "1"
    env.pop("PGLITE_MODULE", None)
    env.pop("PYTHONPATH", None)
    env.pop("PYTHONHOME", None)

    def run(name, command, directory):
        with (evidence / (name + ".log")).open("w", encoding="utf-8") as log:
            log.write("Command: " + subprocess.list2cmdline(command) + "\n")
            log.flush()
            proc = subprocess.run(command, cwd=directory, env=env, stdout=log, stderr=subprocess.STDOUT, check=False)
            log.write(f"\nExit code: {proc.returncode}\n")
        result["commands"].append({"name": name, "exit_code": proc.returncode})
        return proc.returncode

    try:
        manifest, count = verify_source()
        result["original_files_verified"] = count
        result["package_version"] = manifest["version"]
        result["manifest_sha256"] = hashlib.sha256((SOURCE / "MANIFEST.json").read_bytes()).hexdigest()
        if args.integrity_only:
            result["status"] = "INTEGRITY_PASS_SUITES_NOT_RUN"
        else:
            node, npm = shutil.which("node"), shutil.which("npm.cmd" if os.name == "nt" else "npm")
            if not node or not npm:
                raise RuntimeError("Node.js and npm are required for the original SQL suite")
            result["node"] = subprocess.check_output([node, "--version"], text=True).strip()
            work = ROOT / ".local/v3_2-runs" / run_id
            shutil.copytree(SOURCE, work)
            # Originals include historical reports. Require fresh reports from this run.
            for name in ("VALIDATION_REPORT.txt", "validation_results.json", "SQL_VALIDATION_REPORT.json"):
                (work / name).unlink()
            install = run("npm-ci", [npm, "ci", "--ignore-scripts", "--no-audit", "--no-fund"], work)
            contract = run("contract", [sys.executable, "-X", "utf8", "validators/run_checks.py"], work)
            sql = run("sql", [node, "tests/check_sql.mjs"], work) if install == 0 else None
            for name in ("VALIDATION_REPORT.txt", "validation_results.json", "SQL_VALIDATION_REPORT.json"):
                if (work / name).is_file():
                    shutil.copyfile(work / name, evidence / name)
            if install != 0 or contract != 0 or sql != 0:
                raise RuntimeError("Original verification command failed; inspect command logs")
            for kind, filename in (("contract", "validation_results.json"), ("sql", "SQL_VALIDATION_REPORT.json")):
                report = json.loads((evidence / filename).read_text(encoding="utf-8"))
                expected = manifest["validation_summary"][kind]["passed"]
                result[kind] = validate_report(report, kind, expected)
            verify_source()  # Original bytes must remain unchanged after execution.
            result["status"] = "PASS"
            result["sql_engine"] = "Original PGlite PostgreSQL WASM suite; not native concurrency"
    except (OSError, ValueError, TypeError, KeyError, AttributeError, RuntimeError, subprocess.SubprocessError) as error:
        result["error"] = str(error)
    (evidence / "run.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    return 0 if result["status"] in {"PASS", "INTEGRITY_PASS_SUITES_NOT_RUN"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
