"""Create and verify a source/evidence snapshot without asserting phase closure."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import re
import shutil
import subprocess
import sys
import zipfile


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def write_json(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--r1-zip", type=Path, required=True)
    parser.add_argument("--destination", type=Path, required=True)
    parser.add_argument("--node", type=Path, required=True)
    args = parser.parse_args()
    repo = args.repo.resolve()
    source_zip = args.r1_zip.resolve()
    destination = args.destination.resolve()
    commit = "a112f762ab08f6fa688cc4857b21d95d1055ab5c"
    original_sha = "a1221923834cfeb84fd245e93694df2b78b85daf8f23eb6908b04cabe802be10"
    css_rel = "02_product/ux_ui/phase2/prototype/styles.css"
    css_sha = "df4df9ddf878db4aaf68d91aff13b609f6d2091125d87136d98eb013a3331ffb"
    manifest_rel = "08_handoff/phase2/MANIFEST_SHA256.txt"
    final_gate_rel = "06_quality/phase2/final_gate/2026-09-30"
    handoff_rel = "08_handoff/project_snapshot_20260930"
    name = "Mingo_Project_Phase1-3_Snapshot_20260930.zip"
    archive = destination / name
    external_manifest = archive.with_suffix(".manifest.json")
    checksum = destination / (name + ".sha256")
    if any(p.exists() for p in (archive, external_manifest, checksum)):
        raise SystemExit("STOP: delivery target already exists; do not overwrite")
    if subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=repo, text=True).strip() != commit:
        raise SystemExit("STOP: Git candidate identity mismatch")
    changed = subprocess.check_output(["git", "diff", "--name-only", "HEAD"], cwd=repo, text=True).splitlines()
    if changed != [css_rel]:
        raise SystemExit("STOP: unexpected tracked source change")
    source_bytes = source_zip.read_bytes()
    if digest(source_bytes) != original_sha:
        raise SystemExit("STOP: R1 ZIP hash mismatch")
    source_manifest_path = source_zip.with_suffix(".manifest.json")
    source_manifest = json.loads(source_manifest_path.read_text(encoding="utf-8-sig"))
    declared = {x["path"]: x for x in source_manifest["files"]}
    if source_manifest["sha256"] != original_sha or source_manifest["git_commit"] != commit:
        raise SystemExit("STOP: R1 external manifest identity mismatch")
    tracked = set(subprocess.check_output(["git", "ls-files", "-z"], cwd=repo).decode("utf-8").rstrip("\0").split("\0"))
    original_files = {}
    with zipfile.ZipFile(io.BytesIO(source_bytes)) as z:
        if z.testzip() is not None:
            raise SystemExit("STOP: R1 CRC mismatch")
        for info in z.infolist():
            if info.is_dir():
                continue
            if not info.filename.startswith("Mingo/"):
                raise SystemExit("STOP: unexpected R1 root")
            rel = info.filename[len("Mingo/"):]
            path = PurePosixPath(rel)
            if path.is_absolute() or ".." in path.parts or ":" in rel or "\\" in rel or rel in original_files:
                raise SystemExit("STOP: unsafe or duplicate R1 member")
            original_files[rel] = z.read(info)
    if set(original_files) != set(declared) or set(original_files) != tracked or len(original_files) != 780:
        raise SystemExit("STOP: R1 file set mismatch")
    for rel, data in original_files.items():
        entry = declared[rel]
        if digest(data) != entry["sha256"] or len(data) != entry["bytes"]:
            raise SystemExit("STOP: R1 manifest mismatch: " + rel)
    css = (repo / css_rel).read_bytes()
    if digest(css) != css_sha:
        raise SystemExit("STOP: CSS differs from regression-tested candidate")
    for rel, data in original_files.items():
        if rel == css_rel:
            continue
        working = (repo / rel).read_bytes()
        if working != data and working.replace(b"\r\n", b"\n") != data.replace(b"\r\n", b"\n"):
            raise SystemExit("STOP: workspace source differs from sealed candidate: " + rel)

    destination.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    run = destination / ("verification-" + stamp)
    stage = run / "staging" / "Mingo"
    stage.mkdir(parents=True)
    for rel, data in original_files.items():
        target = stage / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
    (stage / css_rel).write_bytes(css)
    shutil.copytree(repo / final_gate_rel, stage / final_gate_rel,
                    ignore=shutil.ignore_patterns("~$*", "__pycache__", "*.pyc"))

    workbook_rel = "outputs/phase2-completion-20260930"
    workbook_names = [
        "Mingo_Phase2_QA_Control_Dashboard_Corrected_2026-09-30.xlsx",
        "Mingo_Phase2_QA_Control_Dashboard_Corrected_2026-09-30.xlsx.sha256",
        "workbook-correction-verification.json", "dashboard-edits.json",
        "artifact-inspection.ndjson", "formula-error-scan.ndjson",
        "edit-dashboard.mjs", "inspect-dashboard.mjs", "preserve-workbook.py", "render-dashboard-view.mjs",
    ]
    for filename in workbook_names:
        target = stage / workbook_rel / filename
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(repo / workbook_rel / filename, target)
    support_names = [
        "outputs/final-gate-20260930/workbook_rows.json",
        "outputs/android-play-fix-20260930/status.json",
        "outputs/android-play-fix-20260930/device-manager-play-success.log",
    ]
    for rel in support_names:
        target = stage / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(repo / rel, target)

    handoff = stage / handoff_rel
    provenance = handoff / "provenance"
    provenance.mkdir(parents=True)
    (provenance / "R1_ORIGINAL_MANIFEST_SHA256.txt").write_bytes(original_files[manifest_rel])
    (provenance / "R1_ORIGINAL_PROTOTYPE_STYLES.css").write_bytes(original_files[css_rel])
    for path in [source_zip, source_manifest_path, source_zip.with_name(source_zip.name + ".sha256"), source_zip.with_name(source_zip.stem + "_HANDOFF.md")]:
        shutil.copyfile(path, provenance / path.name)
    shutil.copyfile(Path(__file__), handoff / "build_snapshot.py")

    statuses = {
        "phase_0": {"status": "DONE"},
        "phase_1": {"status": "DONE", "gate": "PASSED"},
        "phase_2": {"status": "ACTIVE", "technical_retest": "PASS", "gate": "HOLD / NOT PASSED"},
        "phase_3": {"status": "DEFERRED", "eligible": False, "implementation_started": False},
        "interactive_talkback": "BLOCKED BY ENVIRONMENT / NOT RUN",
        "tech_lead_acceptance": "PENDING",
        "product_owner_uat": "PENDING",
        "P2-D021": "FIX NOW authorized; CSS fix implemented; Windows regression PASS; Linux/independent closure PENDING",
        "P2-D022": "Dashboard derivative correction implemented; data/preservation PASS; final visual/independent confirmation PENDING",
    }
    package_status = {
        "as_of": "2026-09-30", "kind": "SOURCE_AND_EVIDENCE_SNAPSHOT_NOT_PHASE_CLOSURE",
        "git_base_commit": commit, "original_r1_zip_sha256": original_sha,
        "original_tracked_files": 780, "tracked_source_overlay": {css_rel: css_sha},
        "protected_originals": "Byte-identical to sealed R1 package; all except toolbar CSS and regenerated package manifest preserved",
        "independent_r1": {"canonical_pass": 94, "canonical_total": 94, "p0_pass": 44, "p0_total": 44, "D001_D020": "CLOSED"},
        "targeted_css_regression": {"browser": "74/74 PASS", "supplemental": "30/30 PASS", "platform": "Windows Chrome", "linux": "NOT RUN"},
        "phases_and_gate_items": statuses,
        "excluded": [".git", "virtual environments", "SDK/runtime installations", "caches and generated build/platform hosts", "Office owner lock files (~$*)", "node_modules", "duplicate temporary candidate extractions", "unrelated untracked Manage Project.xlsx"],
        "earlier_governance": "Original R1-era governance preserved as history; read 00_PACKAGE_STATUS.md and final_gate/2026-09-30 for newer factual evidence. No gate approval or signature added.",
    }
    write_json(handoff / "PACKAGE_STATE.json", package_status)
    (stage / "00_PACKAGE_STATUS.md").write_text("""# Mingo — gói nguồn và evidence ngày 2026-09-30

Đây là bản snapshot bàn giao theo yêu cầu đóng gói dự án. Không phải biên bản chốt Phase 2/3.

| Phase | Trạng thái đã có evidence |
|---|---|
| Phase 0 | DONE |
| Phase 1 | DONE / GATE PASSED |
| Phase 2 | ACTIVE / TECHNICAL RETEST PASS / GATE HOLD |
| Phase 3 — Identity/Auth/Authorization | DEFERRED; chưa triển khai; chưa đủ điều kiện bắt đầu |

Phase 2 là UX/UI, đặc tả, prototype mô phỏng, traceability và developer handoff. Production app/web/backend được triển khai ở các phase sau. Các shell Flutter và nền tảng backend Phase 1 có trong `05_code/`.

Independent R1: canonical 94/94 PASS, P0 44/44 PASS, D001–D020 CLOSED. D021 đã được chủ dự án chọn FIX NOW: chỉ sửa CSS toolbar QA; Windows browser 74/74, supplemental 30/30 và 320px/200% PASS. Linux/independent closure còn chờ. D022 có workbook derivative sửa 19 ô Dashboard; data/preservation PASS; final visual/independent confirmation còn chờ.

| Gate item | Trạng thái |
|---|---|
| Objective verification | Core PASS; report follow-up PENDING |
| Interactive TalkBack | BLOCKED BY ENVIRONMENT / NOT RUN |
| Tech Lead decision | PENDING |
| Product Owner UAT | PENDING |
| P2-D021 | FIX IMPLEMENTED; independent retest PENDING |
| P2-D022 | FIX IMPLEMENTED; confirmation PENDING |
| Phase 2 gate | HOLD / NOT PASSED |
| Phase 3 | DEFERRED |

## Đọc và kiểm tra gói

1. Đọc `06_quality/phase2/final_gate/2026-09-30/FINAL_GATE_STATUS.md`, `PHASE2_SCOPE_RECONCILIATION.md` và `FINAL_GATE_OBJECTIVE_VERIFICATION.md`.
2. Original independent report/JSON/workbook nằm trong `06_quality/phase2/final_gate/2026-09-30/inputs/`; corrected derivative nằm trong `outputs/phase2-completion-20260930/`.
3. TalkBack runbook, evidence template, Tech Lead packet và Owner UAT packet ở cùng thư mục final gate. Những trường quyết định/chữ ký còn trống.
4. Phase 1 closure: `08_handoff/PHASE1_CLOSURE_20260926.md`; nguồn ứng dụng: `05_code/README.md`.
5. Từ thư mục `Mingo`, chạy `python 07_operations/scripts/verify_phase2_package_manifest.py` để kiểm tra hash toàn bộ file. Kiểm tra này không ghi file.
6. Xem prototype: `python -m http.server 8765 --bind 127.0.0.1 --directory 02_product/ux_ui/phase2/prototype`, rồi mở `http://127.0.0.1:8765`. Đây là prototype UX mô phỏng.
7. Xem `START_HERE.md` và `07_operations/` để dựng môi trường Phase 1; dependency/runtime cài riêng. Chạy verifier có ghi evidence trên một bản sao để giữ bản bàn giao nguyên trạng.

`01_governance/` và hồ sơ cũ được giữ nguyên như lịch sử R1; một số dòng vẫn mô tả independent retest đang chờ. Evidence mới ngày 2026-09-29/30 ở final gate và `08_handoff/project_snapshot_20260930/PACKAGE_STATE.json` xác nhận technical retest đã PASS, nhưng không phê duyệt gate thay chủ dự án.

Toàn bộ 780 file tracked của R1 được xuất từ ZIP đã xác minh; chỉ overlay CSS đã kiểm thử và tái tạo package manifest. V3.2 originals, Phase 1 code/evidence và các workbook signoff gốc giữ nguyên byte từ R1. ZIP R1 gốc, companion manifest/checksum/handoff và manifest/CSS gốc được giữ trong `08_handoff/project_snapshot_20260930/provenance/`.

Không đóng gói `.git`, môi trường ảo, SDK cài trên máy, cache/build/node_modules, các bản giải nén tạm trùng lặp hoặc workbook local `Manage Project.xlsx` không thuộc candidate. Không ghi ACCEPTED, không ký tên, không đổi Phase 2/3 thành DONE.
""", encoding="utf-8")

    checks = run / "checks" / "Mingo"
    shutil.copytree(stage, checks)
    commands = [
        ("rework_static", [sys.executable, "-X", "utf8", "07_operations/scripts/verify_phase2_rework.py"]),
        ("artifact_review", [sys.executable, "-X", "utf8", "07_operations/scripts/verify_phase2_review.py"]),
        ("javascript_syntax", [str(args.node), "--check", "02_product/ux_ui/phase2/prototype/app.js"]),
    ]
    executed = []
    for label, command in commands:
        result = subprocess.run(command, cwd=checks, capture_output=True, text=True, encoding="utf-8")
        entry = {"name": label, "exit_code": result.returncode, "stdout": result.stdout, "stderr": result.stderr,
                 "scope": "Clean snapshot copy; writes remain in verification copy; no independent approval"}
        executed.append(entry)
        print(label, "PASS" if result.returncode == 0 else "FAIL", flush=True)
        if result.returncode != 0:
            write_json(run / "FAILED_CHECKS.json", executed)
            raise SystemExit("STOP: verification failed; see FAILED_CHECKS.json")

    source_changes = [rel for rel, data in original_files.items() if (stage / rel).read_bytes() != data]
    if source_changes != [css_rel]:
        raise SystemExit("STOP: unexpected mutation before package manifest regeneration")
    protection = {"sealed_r1_files": 780, "baseline_bytes_preserved_before_manifest": 779,
                  "only_changed_original_file": css_rel,
                  "v3_2_source_files": sum(rel.startswith("04_architecture/contracts/v3_2/source/") for rel in original_files),
                  "phase_1_code_files": sum(rel.startswith("05_code/") for rel in original_files),
                  "v3_2_and_phase_1_bytes_preserved": True}
    write_json(handoff / "SNAPSHOT_VERIFICATION.json", {"intake": "PASS", "preservation": protection, "executed": executed,
               "independent_acceptance": "NOT ASSERTED", "new_full_runtime_regression": "NOT REPEATED; regression-tested CSS SHA identical"})
    (handoff / "checks").mkdir(exist_ok=True)
    shutil.copyfile(checks / "06_quality/phase2/evidence/rework_r1_static_checks.json", handoff / "checks/rework_r1_static_checks.json")
    shutil.copyfile(checks / "06_quality/phase2/evidence/codex/review/run.json", handoff / "checks/review_run.json")

    patterns = re.compile(r"gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|postgresql://[^\s:]+:[^<\s@]+@")
    text_extensions = {".md", ".json", ".csv", ".js", ".cjs", ".mjs", ".css", ".html", ".log", ".txt", ".yaml", ".yml", ".py", ".sh", ".ps1", ".ini", ".xml", ".toml", ".sql", ".dart", ".example", ".ndjson"}
    scan_counts = {"text_files": 0, "nested_containers": 0, "nested_text_parts": 0}
    matches = []
    classified = []
    # Exact path + match digest exceptions, reviewed in the immutable R1 bytes.
    # They are template/test/regex expressions, not captured local credentials.
    reviewed_nonsecrets = {
        ("05_code/.env.example", "424aa566044b6d15abf45ed6dc886c30f5c1b19ad256858b03015567de8dc4f7"): "CHANGE_ME template at loopback; example file",
        (".github/workflows/foundation.yaml", "3d94b230676e5841618a1c1b2100636b67d4ab2f9bddfa3e853fdb9cc6aaafa7"): "Explicit disposable CI Postgres service password; localhost job service",
        ("05_code/backend/tests/test_unit.py", "2cd330cc0c76e3c18ea6b36367026b3d0808e6344d3465ba696068b02445be05"): "Negative readiness fixture at 127.0.0.1:1/absent",
        ("06_quality/evidence/clean_reproduction/run-4cdecb4/harness/reproduce.py", "e51c4891eb7126cd2b3964b29d0e2e920906ae608168e0251c6b854894e60027"): "Python f-string variable expression; runtime password is not embedded",
        ("07_operations/scripts/smoke_api.py", "7caa89a3cfb611aa38e7258e13eef92c3e9e32babc497e1ea8d69bbfcffb8f88"): "unused negative readiness fixture at 127.0.0.1:1",
        ("07_operations/scripts/verify_backend.ps1", "7caa89a3cfb611aa38e7258e13eef92c3e9e32babc497e1ea8d69bbfcffb8f88"): "unused negative readiness fixture at 127.0.0.1:1",
        ("07_operations/scripts/verify_backend.sh", "7caa89a3cfb611aa38e7258e13eef92c3e9e32babc497e1ea8d69bbfcffb8f88"): "unused negative readiness fixture at 127.0.0.1:1",
        ("07_operations/scripts/verify_phase2_artifacts.py", "7bcf82dc163b9562ac4a44c13402f943a3ed82c75a107468d89904d5157225dd"): "Literal regex pattern definition, not a connection string",
        ("07_operations/scripts/verify_phase2_rework.py", "7bcf82dc163b9562ac4a44c13402f943a3ed82c75a107468d89904d5157225dd"): "Literal regex pattern definition, not a connection string",
    }

    def scan_data(rel: str, data: bytes, extension: str, depth: int = 0) -> None:
        if extension in text_extensions:
            scan_counts["nested_text_parts" if depth else "text_files"] += 1
            logical_rel = rel
            r1_nested_prefix = handoff_rel + "/provenance/" + source_zip.name + "!Mingo/"
            if logical_rel.startswith(r1_nested_prefix):
                logical_rel = logical_rel[len(r1_nested_prefix):]
            for found in patterns.finditer(data.decode("utf-8", errors="replace")):
                key = (logical_rel, digest(found.group().encode("utf-8")))
                reason = reviewed_nonsecrets.get(key)
                if reason and logical_rel in original_files and data == original_files[logical_rel]:
                    classified.append({"path": rel, "match_sha256": key[1], "classification": reason,
                                       "sealed_r1_file_sha256": digest(data)})
                else:
                    matches.append(rel)
        if extension in {".zip", ".xlsx", ".docx", ".pptx"} and depth < 8:
            scan_counts["nested_containers"] += 1
            with zipfile.ZipFile(io.BytesIO(data)) as z:
                for member in z.infolist():
                    if not member.is_dir():
                        scan_data(rel + "!" + member.filename, z.read(member), PurePosixPath(member.filename).suffix.lower(), depth + 1)

    for path in stage.rglob("*"):
        if path.is_file():
            scan_data(path.relative_to(stage).as_posix(), path.read_bytes(), path.suffix.lower())
    if matches:
        write_json(run / "SECRET_SCAN_FINDINGS.json", {"matched_paths": matches})
        raise SystemExit("STOP: potential credential finding; paths recorded without values")
    write_json(handoff / "SECRET_HYGIENE.json", {"result": "PASS", "pattern_scope": "Existing credential/token/private-key patterns with individually reviewed exact R1 template/test/regex findings; not exhaustive detection", "counts": scan_counts, "unclassified_matched_paths": matches, "classified_nonsecret_matches": classified})
    print("credential_pattern_scan PASS", scan_counts, flush=True)

    manifest = stage / manifest_rel
    files = sorted(p for p in stage.rglob("*") if p.is_file() and p != manifest)
    manifest.write_text("# SHA-256 of 2026-09-30 source/evidence snapshot; excludes this manifest.\n" + "".join(digest(p.read_bytes()) + "  " + p.relative_to(stage).as_posix() + "\n" for p in files), encoding="utf-8")
    result = subprocess.run([sys.executable, "-X", "utf8", "07_operations/scripts/verify_phase2_package_manifest.py"], cwd=stage, capture_output=True, text=True, encoding="utf-8")
    if result.returncode != 0:
        raise SystemExit("STOP: fresh package manifest verifier failed: " + result.stdout + result.stderr)
    print(result.stdout.strip(), flush=True)

    all_files = sorted(p for p in stage.rglob("*") if p.is_file())
    entries = [{"path": p.relative_to(stage).as_posix(), "bytes": p.stat().st_size, "sha256": digest(p.read_bytes())} for p in all_files]
    partial = run / (name + ".partial")
    with zipfile.ZipFile(partial, "x", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as z:
        for p in all_files:
            z.write(p, "Mingo/" + p.relative_to(stage).as_posix())
    with zipfile.ZipFile(partial) as z:
        if z.testzip() is not None or len(z.infolist()) != len(entries):
            raise SystemExit("STOP: output ZIP CRC/file count mismatch")
        members = {member.filename: member for member in z.infolist()}
        if set(members) != {"Mingo/" + entry["path"] for entry in entries}:
            raise SystemExit("STOP: output ZIP member set mismatch")
        for entry in entries:
            data = z.read("Mingo/" + entry["path"])
            if len(data) != entry["bytes"] or digest(data) != entry["sha256"]:
                raise SystemExit("STOP: output ZIP member hash mismatch: " + entry["path"])
        extraction = run / "roundtrip"
        z.extractall(extraction)
    clean = extraction / "Mingo"
    check = subprocess.run([sys.executable, "-X", "utf8", "07_operations/scripts/verify_phase2_package_manifest.py"], cwd=clean, capture_output=True, text=True, encoding="utf-8")
    if check.returncode != 0:
        raise SystemExit("STOP: roundtrip manifest verification failed")
    print("roundtrip:", check.stdout.strip(), flush=True)
    archive_sha = digest(partial.read_bytes())
    metadata = {"package": name, "kind": package_status["kind"], "created_utc": datetime.now(timezone.utc).isoformat(),
                "git_base_commit": commit, "sha256": archive_sha, "bytes": partial.stat().st_size,
                "files_count": len(entries), "integrity": "PASS", "crc": "PASS", "exact_file_set_and_member_hashes": "PASS",
                "clean_extraction_manifest_verifier": {"exit_code": check.returncode, "stdout": check.stdout.strip()},
                "source_package_sha256": original_sha, "protected_bytes": protection,
                "phase_status": statuses, "credential_pattern_scan": {"result": "PASS", "counts": scan_counts},
                "files": entries}
    partial.rename(archive)
    write_json(external_manifest, metadata)
    checksum.write_text(archive_sha + "  " + name + "\n", encoding="utf-8")
    delivery_note = destination / "Mingo_Project_Snapshot_20260930_HANDOFF.md"
    with delivery_note.open("x", encoding="utf-8") as f:
        f.write("# Mingo snapshot handoff — 2026-09-30\n\n" +
                "Package: " + name + "\n\nSHA-256: " + archive_sha + "\n\n" +
                "Integrity/clean extraction: PASS. " + str(len(entries)) + " files.\n\n" +
                "Phase 1 DONE / GATE PASSED. Phase 2 ACTIVE / TECHNICAL RETEST PASS / GATE HOLD. Phase 3 DEFERRED, not implemented.\n\n" +
                "Start with Mingo/00_PACKAGE_STATUS.md. Required accessibility and designated acceptance remain pending; no closure/signature is asserted.\n")
    print(json.dumps({"zip": str(archive), "manifest": str(external_manifest), "sha256_file": str(checksum),
                      "sha256": archive_sha, "bytes": archive.stat().st_size, "files": len(entries), "gate": "HOLD"}, ensure_ascii=False, indent=2), flush=True)


if __name__ == "__main__":
    main()
