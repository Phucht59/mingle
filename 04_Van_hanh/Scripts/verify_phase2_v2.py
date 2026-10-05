"""Verify V2 presentation scope without weakening sealed historical audits."""
from pathlib import Path
import hashlib,json,csv,re,sys

ROOT=Path(__file__).resolve().parents[2]
UX=ROOT/'02_Tai_lieu_du_an/04_Thiet_ke_san_pham/ux_ui/phase2/rebaseline_v2'
EVIDENCE=ROOT/'03_Kiem_thu/QA_QC/phase2/rebaseline_v2_20261001'
BASELINE=ROOT/'02_Tai_lieu_du_an/07_Tien_do_du_an/Rebaseline_Phase2_V2_20261001/PRE_REWORK_BASELINE.json'
def main():
    baseline=json.loads(BASELINE.read_text(encoding='utf-8'));errors=[]
    mismatches=[]
    for name,digest in baseline['protected_sha256'].items():
        p=ROOT/name
        if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=digest:mismatches.append(name)
    errors += ['protected bytes changed: '+n for n in mismatches]
    organization=json.loads((ROOT/'02_Tai_lieu_du_an/07_Tien_do_du_an/Tai_cau_truc_20261001/RESTRUCTURE_BASELINE.json').read_text(encoding='utf-8'))
    missing=[item['new'] for item in organization['inventory'] if not (ROOT/item['new']).is_file()]
    errors += ['pre-migration artifact missing: '+n for n in missing]
    historical=[];historical_mismatches=[]
    for item in organization['inventory']:
        old=item['old']
        immutable=old.startswith(('99_archive/','08_handoff/provenance/','outputs/','06_quality/evidence/','06_quality/phase2/evidence/','06_quality/phase2/audits/')) or item['new'].startswith('99_Luu_tru/') or old.endswith('/MANIFEST_SHA256.txt') or '/final_gate/2026-09-30/inputs/' in old
        if immutable:
            historical.append(item['new']);p=ROOT/item['new']
            if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=item['sha256']:historical_mismatches.append(item['new'])
    errors += ['historical bytes changed: '+n for n in historical_mismatches]
    catalog=json.loads((UX/'SCREEN_CATALOG.json').read_text(encoding='utf-8'))
    ids={s['id'] for s in catalog}
    if len(ids)!=len(catalog):errors.append('duplicate screen id')
    expected={(s['id'],state) for s in catalog for state in s['states']}
    def states_of(s):
        value=s['states']
        return [p.strip() for p in value.split(',')] if isinstance(value,str) else value
    old={(s['id'],state) for s in baseline['source_screens'] for state in states_of(s)}
    if old-expected:errors.append('missing original state coverage: '+str(old-expected))
    trace=list(csv.DictReader((UX/'SCREEN_STATE_TRACEABILITY.csv').open(encoding='utf-8-sig')))
    if {(r['screen_id'],r['state']) for r in trace}!=expected:errors.append('state traceability mismatch')
    current_trace={(r['screen_id'],r['state']):r for r in trace}
    for r in baseline['source_state_traceability']:
        current=current_trace.get((r['screen_id'],r['state']),{})
        if current.get('inherited_rule')!=r['rule'] or current.get('inherited_qa_case_ids')!=r['qa_cases']:errors.append('original rule/QA mapping changed: '+r['screen_id']+'/'+r['state'])
    captures=[]
    extra=list(csv.DictReader((UX/'ADDITIONAL_PRESENTATION_TRACEABILITY.csv').open(encoding='utf-8-sig')))
    for r in trace+extra:
        p=ROOT/r['screenshot']
        if not p.is_file():errors.append('missing screenshot: '+r['screenshot'])
        else:captures.append(dict(path=r['screenshot'],sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
    required=['README.md','MINGO_DESIGN_SYSTEM_V2.md','MASCOT_STYLE_GUIDE.md','MOTION_SPEC.md','PRODUCT_LANGUAGE_GLOSSARY.md','CONTENT_QUALITY_RUBRIC.md','PHASE2_RESEARCH_RATIONALE.md','PHASE2_SCREEN_INVENTORY.md','PHASE2_USABILITY_TEST_PROTOCOL.md','PHASE2_DIARY_PILOT_PLAN.md','ACCESSIBILITY_TEST_PLAN.md','ACCESSIBILITY_MANUAL_CHECKLIST.md','HUMAN_APPROVAL_REQUIRED.md','DEVELOPER_HANDOFF_V2.md','D021_D022_RECONCILIATION.md','ASSET_PROVENANCE.json','PRD_TRACEABILITY_V2.csv','REGRESSION_REPORT.md','V3_2_INTEGRITY_REPORT.md','PHASE1_REVALIDATION_REPORT.md','PHASE2_FINAL_GATE_REPORT.md','SCREENSHOT_PACK.md','DELIVERABLE_INDEX.md','THIRD_PARTY_NOTICES.md']
    errors+=['missing artifact: '+n for n in required if not (UX/n).is_file()]
    provenance=json.loads((UX/'ASSET_PROVENANCE.json').read_text(encoding='utf-8'))
    for a in provenance['assets']:
        if hashlib.sha256((ROOT/a['path']).read_bytes()).hexdigest()!=a['sha256']:errors.append('asset hash changed '+a['path'])
    count=0;failures=[];done=False
    log=EVIDENCE/'flutter_sealed_final.jsonl'
    test_names={};passed_names=set()
    if log.is_file():
        for line in log.read_text(encoding='utf-8').splitlines():
            try:r=json.loads(line)
            except json.JSONDecodeError:continue
            # --machine emits daemon metadata arrays before test-runner events.
            if not isinstance(r,dict):continue
            if r.get('type')=='testStart':test_names[r['test']['id']]=r['test']['name']
            if r.get('type')=='testDone' and not r.get('hidden'):
                count+=1
                if r['result']!='success' or r.get('skipped'):failures.append(r)
                else:passed_names.add(test_names.get(r['testID'],''))
            if r.get('type')=='done':done=r.get('success') is True
    if not done or failures:errors.append('final Flutter regression missing/incomplete/failing')
    for r in trace+extra:
        if r['test'] not in passed_names:errors.append('capture test did not pass: '+r['test'])
    runtime=json.loads((EVIDENCE/'web_runtime_sealed_final/run.json').read_text(encoding='utf-8'))
    if len(runtime['results'])!=7 or any(r['status']!='PASS' for r in runtime['results']):errors.append('compiled Web runtime navigation did not pass')
    contracts=json.loads((EVIDENCE/'v3_2_after.log').read_text(encoding='utf-8'))
    if contracts['contract']!={'passed':115,'failed':0,'total':115} or contracts['sql']!={'passed':22,'failed':0,'total':22}:errors.append('original V3.2 suite did not pass')
    android=(EVIDENCE/'android_review_final.log').read_text(encoding='utf-8')
    if '+2: All tests passed!' not in android:errors.append('actual Android boot/audio integration did not pass')
    phase=(ROOT/'02_Tai_lieu_du_an/07_Tien_do_du_an/PHASE_STATUS.yaml').read_text(encoding='utf-8')
    if 'status: HOLD' not in phase or 'eligible: false' not in phase or 'gate: NOT_PASSED' not in phase or f'local_flutter_tests_passed: {count}' not in phase:errors.append('current phase/governance evidence mismatch')
    (EVIDENCE/'screenshot_manifest.json').write_text(json.dumps(captures,indent=2),encoding='utf-8')
    result=dict(status='PASS' if not errors else 'FAIL',protected_files=len(baseline['protected_sha256']),protected_mismatches=mismatches,
      historical_files=len(historical),historical_mismatches=historical_mismatches,
      pre_migration_files=len(organization['inventory']),missing_pre_migration_files=missing,
      v3_2_source_files=sum('/v3_2/source/' in n for n in baseline['protected_sha256']),screens=len(catalog),states=len(expected),preserved_original_states=len(old),screenshots=len(captures),flutter_tests=count,compiled_web_cases=len(runtime['results']),errors=errors)
    (EVIDENCE/'v2_verification.json').write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result,indent=2))
    return int(bool(errors))
if __name__=='__main__':sys.exit(main())
