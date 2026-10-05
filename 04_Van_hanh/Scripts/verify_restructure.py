"""Verify file preservation and protected boundaries after repository relocation."""
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parents[2]
audit = root / '02_Tai_lieu_du_an/07_Tien_do_du_an/Tai_cau_truc_20261001'
baseline = json.loads((audit / 'RESTRUCTURE_BASELINE.json').read_text(encoding='utf-8'))
adaptations = {item['old']: item for item in json.loads((audit / 'PATH_ADAPTATIONS.json').read_text(encoding='utf-8'))}
errors = []
v32_count = 0
runtime_count = 0
immutable_count = 0
for item in baseline['inventory']:
    path = root / item['new']
    if not path.is_file():
        errors.append('missing: ' + item['new'])
        continue
    actual = hashlib.sha256(path.read_bytes()).hexdigest()
    expected = adaptations.get(item['old'], {}).get('after_sha256', item['sha256'])
    if actual != expected:
        errors.append('hash mismatch: ' + item['new'])
    old = item['old']
    if old in baseline['v3_2_sha256']:
        v32_count += 1
        if actual != baseline['v3_2_sha256'][old]:
            errors.append('V3.2 changed: ' + item['new'])
    protected = old.startswith(('05_code/backend/', '05_code/apps/'))
    if protected:
        runtime_count += 1
        if actual != item['sha256']:
            errors.append('runtime source changed: ' + item['new'])
    immutable = old.startswith(('99_archive/', '08_handoff/provenance/', 'outputs/', '06_quality/evidence/', '06_quality/phase2/evidence/', '06_quality/phase2/audits/')) or item['new'].startswith('99_Luu_tru/') or old.endswith('/MANIFEST_SHA256.txt') or '/final_gate/2026-09-30/inputs/' in old
    if immutable:
        immutable_count += 1
        if actual != item['sha256']:
            errors.append('historical/evidence bytes changed: ' + item['new'])
for folder in ['01_governance', '02_product', '03_research', '04_architecture', '05_code', '06_quality', '07_operations', '08_handoff', '99_archive', 'outputs']:
    if (root / folder).exists():
        errors.append('legacy root folder remains: ' + folder)
phase = (root / '02_Tai_lieu_du_an/07_Tien_do_du_an/PHASE_STATUS.yaml').read_text(encoding='utf-8')
if phase != baseline['phase_status']:
    errors.append('recorded phase status changed')
manifest = audit / 'RESTRUCTURE_MANIFEST_SHA256.txt'
manifest_count = 0
if manifest.is_file():
    manifest_paths = set()
    for line in manifest.read_text(encoding='utf-8').splitlines():
        if not line or line.startswith('#'):
            continue
        digest, name = line.split('  ', 1)
        path = root / name
        if not path.resolve().is_relative_to(root.resolve()) or name in manifest_paths:
            errors.append('invalid/duplicate manifest entry: ' + name)
            continue
        manifest_paths.add(name)
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != digest:
            errors.append('organization manifest mismatch: ' + name)
    manifest_count = len(manifest_paths)
    if {item['new'] for item in baseline['inventory']} - manifest_paths:
        errors.append('organization manifest omits pre-migration artifacts')
else:
    errors.append('organization manifest missing')
result = dict(status='PASS' if not errors else 'FAIL', artifact_files=len(baseline['inventory']), adapted_files=len(adaptations), organization_manifest_files=manifest_count, v3_2_source_and_provenance_files=v32_count, runtime_files_byte_identical=runtime_count, historical_evidence_files_byte_identical=immutable_count, errors=errors)
print(json.dumps(result, indent=2))
raise SystemExit(bool(errors))
