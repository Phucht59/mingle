"""Verify audit source preservation, navigation and reported counts after doc-only fixes."""
from pathlib import Path
import hashlib,importlib.util,json,re,xml.etree.ElementTree as ET
R=Path('C:/Mingo');E=R/'03_Kiem_thu/Bang_chung/gd1_consistency_20261005';O=R/'03_Kiem_thu/Bao_cao/GD1_Consistency_Audit_20261005'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
before=json.loads((E/'active_source_inventory_before.json').read_text(encoding='utf-8'))
allowed={
 '02_Tai_lieu_du_an/04_Thiet_ke_san_pham/PRODUCT_CHARTER.md',
 '02_Tai_lieu_du_an/04_Thiet_ke_san_pham/MVP_PRD.md',
 '02_Tai_lieu_du_an/04_Thiet_ke_san_pham/learning_design/LEARNER_EVIDENCE_MODEL.md',
 '02_Tai_lieu_du_an/06_Quyet_dinh_da_chot/DECISION_REGISTER.md',
 '02_Tai_lieu_du_an/06_Quyet_dinh_da_chot/CHANGE_REQUESTS.md',
 '02_Tai_lieu_du_an/07_Tien_do_du_an/PROJECT_STATE.md',
}
ledger=[{'path':x['path'],'before_sha256':x['sha256'],'after_sha256':sha(R/x['path']) if (R/x['path']).is_file() else None} for x in before]
changed=[x for x in ledger if x['before_sha256']!=x['after_sha256']]
unexpected=[x['path'] for x in changed if x['path'] not in allowed]
missing_allowed=allowed-{x['path'] for x in changed}
(E/'source_change_ledger.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2),encoding='utf-8')
p=R/'04_Van_hanh/Scripts/check_original_contracts.py'
spec=importlib.util.spec_from_file_location('gd1_final_original_integrity',p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
manifest,count=m.verify_source()
link_files=[R/p for p in allowed]+list(O.glob('*.md'))+[
 R/'02_Tai_lieu_du_an/04_Thiet_ke_san_pham/GD1_INTERNAL_BA_CLOSURE_NOTES_20261005.md',
 R/'02_Tai_lieu_du_an/07_Tien_do_du_an/MINGO_PROJECT_PROGRESS_SNAPSHOT_2026-10-05.md',
]
errors=[];link_count=0
for p in link_files:
 for raw in re.findall(r'\[[^\]\n]+\]\(([^)]+)\)',p.read_text(encoding='utf-8')):
  target=raw.strip('<>').split('#')[0]
  if not target or re.match(r'^[a-zA-Z]+:',target):continue
  target=re.sub(r':\d+$','',target);link_count+=1
  if not (p.parent/target).resolve().exists():errors.append({'file':p.relative_to(R).as_posix(),'target':target})
run=R/'03_Kiem_thu/Bang_chung/v3_2/20261004T181105665514Z'
r=json.loads((run/'run.json').read_text(encoding='utf-8'))
c=json.loads((run/'validation_results.json').read_text(encoding='utf-8'));s=json.loads((run/'SQL_VALIDATION_REPORT.json').read_text(encoding='utf-8'))
cp=sum(x.startswith('PASS ') for x in c['checks']);sp=sum(x['status']=='PASS' for x in s['checks'])
events=[]
for line in (E/'flutter_selected.jsonl').read_text(encoding='utf-8-sig').splitlines():
 try:events.append(json.loads(line))
 except json.JSONDecodeError:pass
done=[x for x in events if x.get('type')=='testDone' and not x.get('hidden')]
flutter={'passed':sum(x.get('result')=='success' and not x.get('skipped') for x in done),'failed':sum(x.get('result') in ['failure','error'] for x in done),'skipped':sum(bool(x.get('skipped')) for x in done),'complete':any(x.get('type')=='done' and x.get('success') is True for x in events)}
b=ET.parse(E/'backend.xml').getroot().find('testsuite')
backend={k:int(b.attrib[k]) for k in ['tests','failures','errors','skipped']};backend['passed']=backend['tests']-backend['failures']-backend['errors']-backend['skipped']
f=json.loads((O/'FINDING_REGISTER.json').read_text(encoding='utf-8'))['findings']
critical=[x['ID'] for x in f if x['Gate blocking']=='YES']
report=(O/'EXECUTIVE_AUDIT.md').read_text(encoding='utf-8')
trace=(O/'AUDIT_TABLES.md').read_text(encoding='utf-8')
checks={
 'expected_only_document_edits':not unexpected and not missing_allowed,
 'original102_hashes_preserved':count==102,
 'actual_management_workbook_unchanged':all(x['before_sha256']==x['after_sha256'] for x in ledger if x['path'].endswith('.xlsx')),
 'runtime_source_tests_config_unchanged':all(x['before_sha256']==x['after_sha256'] for x in ledger if x['path'].startswith(('01_San_pham/','.github/','04_Van_hanh/'))),
 'links_resolve':not errors,
 'original_report_counts':r['status']=='PASS' and cp==115 and sp==22 and len(c['checks'])==115 and len(s['checks'])==22,
 'flutter_counts':flutter=={'passed':232,'failed':0,'skipped':0,'complete':True},
 'backend_counts':backend=={'tests':16,'failures':0,'errors':0,'skipped':7,'passed':9},
 'report_15_required_sections':all(re.search(r'^## '+str(i)+r'\.',report,re.M) for i in range(1,16)),
 'all16_PRDs_and17_matrix_areas':len(re.findall(r'^\| PRD-\d{2};',trace,re.M))==16 and all(a in trace for a in ['Architecture','Authority','Content versioning','Learning evidence','Assessment','Offline','Telemetry','Analytics','Recommendation','ML optionality','Privacy','Actor','Account','Staff/content','NFR','Scope','Traceability']),
 'all12_findings_and3_critical':len(f)==12 and critical==['AUD-001','AUD-003','AUD-005'],
 'status_counts':sum(x['Status']=='OPEN' for x in f)==6 and sum(x['Status']=='FIXED' for x in f)==4 and sum(x['Status']=='PASS' for x in f)==2,
 'customer_debt_and_internal_fail':bool(re.search(r'\*\*FAIL',report)) and 'VALIDATION DEBT' in report,
 'installed_backend_matches_current_source':json.loads((E/'backend_loaded_source_boundary.json').read_text(encoding='utf-8'))['all_same'],
 'current_evidence_verifier_after_pass':json.loads((E/'current_candidate_verification_after.json').read_text(encoding='utf-8'))['status']=='PASS',
}
result={'status':'PASS' if all(checks.values()) else 'FAIL','checks':checks,'changed':[x['path'] for x in changed],'unexpected_changes':unexpected,'link_count':link_count,'broken_links':errors,'contract_count':cp,'sql_count':sp,'backend':backend,'flutter':flutter,'critical_open':critical}
(E/'postfix_validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
outputs=[{'path':p.relative_to(R).as_posix(),'sha256':sha(p)} for p in O.iterdir() if p.is_file()]
outputs.append({'path':'02_Tai_lieu_du_an/07_Tien_do_du_an/MINGO_PROJECT_PROGRESS_SNAPSHOT_2026-10-05.md','sha256':sha(R/'02_Tai_lieu_du_an/07_Tien_do_du_an/MINGO_PROJECT_PROGRESS_SNAPSHOT_2026-10-05.md')})
(E/'deliverable_manifest.json').write_text(json.dumps(outputs,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(result,ensure_ascii=False))
raise SystemExit(0 if result['status']=='PASS' else 1)
