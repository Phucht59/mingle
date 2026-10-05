"""Verify the current candidate without rewriting sealed historical verifiers.

Machine scope: artifact integrity, inherited constraints, current executed tests,
trace coverage and authority boundaries. Never certifies human/product approval.
"""
from pathlib import Path
import csv,hashlib,json,re,datetime,sys
R=Path(__file__).resolve().parents[2]
U=R/'02_Tai_lieu_du_an/04_Thiet_ke_san_pham/ux_ui/phase2/rebaseline_v2'
E=R/'03_Kiem_thu/QA_QC/phase2/evidence_gated_20261002'
def j(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def table(name):return list(csv.DictReader((U/name).open(encoding='utf-8-sig')))
def run():
 errors=[]; checks={}
 def check(name,condition,detail=None):
  checks[name]={'status':'PASS' if condition else 'FAIL','detail':detail}
  if not condition:errors.append(name)
 foundation=j(E/'baseline/FINAL_FOUNDATION_COUNTS.json')
 check('foundation commands/log integrity',all(x['exit_code']==0 and digest(E/'baseline/phase1_final'/x['log'])==x['sha256'] for x in foundation['phase1_run']['commands']))
 check('original115+22',foundation['original_v3_final']['contract']['passed']==115 and foundation['original_v3_final']['sql']['passed']==22 and foundation['original_v3_final']['status']=='PASS')
 baseline=j(R/'02_Tai_lieu_du_an/07_Tien_do_du_an/Rebaseline_Phase2_V2_20261001/PRE_REWORK_BASELINE.json')
 changed=[name for name,h in baseline['protected_sha256'].items() if not (R/name).is_file() or digest(R/name)!=h]
 check('protected141 current bytes',not changed,changed)
 org=j(R/'02_Tai_lieu_du_an/07_Tien_do_du_an/Tai_cau_truc_20261001/RESTRUCTURE_BASELINE.json')
 missing=[x['new'] for x in org['inventory'] if not (R/x['new']).is_file()]
 check('all10096 original artifact paths present',not missing,missing)
 historical=[];hm=[]
 for x in org['inventory']:
  old=x['old']; new=x['new']
  if old.startswith(('99_archive/','08_handoff/provenance/','outputs/','06_quality/evidence/','06_quality/phase2/evidence/','06_quality/phase2/audits/')) or new.startswith('99_Luu_tru/') or old.endswith('/MANIFEST_SHA256.txt') or '/final_gate/2026-09-30/inputs/' in old:
   historical.append(new)
   if not (R/new).is_file() or digest(R/new)!=x['sha256']:hm.append(new)
 check('historical artifact bytes',not hm,{'count':len(historical),'mismatch':hm})
 approval=j(E/'TECHNICAL_VISUAL_CANDIDATE_APPROVAL_FINAL.json')
 cm=[n for n,h in approval['source_sha256'].items() if digest(R/n)!=h]
 check('approved render source unchanged',not cm,cm)
 catalog=j(U/'SCREEN_CATALOG.json'); expected={(s['id'],state) for s in catalog for state in s['states']}
 trace=table('SCREEN_STATE_TRACEABILITY.csv'); extra=table('ADDITIONAL_PRESENTATION_TRACEABILITY.csv')
 check('61screens175states',len(catalog)==61 and len(expected)==175 and {(x['screen_id'],x['state']) for x in trace}==expected)
 scopes=table('SCREEN_SCOPE_REGISTER.csv')
 check('61routes classified without additions',len(scopes)==61 and {x['screen_id'] for x in scopes}=={s['id'] for s in catalog} and all(x['category'] in {'CORE','SUPPORT','RECOVERY','RARE','FUTURE'} for x in scopes))
 check('175 inherited rules unchanged',j(E/'baseline/INHERITED_RULE_QA_TRACEABILITY.json')['status']=='PASS')
 captures=[R/x['screenshot'] for x in trace+extra]
 check('205captures traced and present',len(captures)==205 and len(set(captures))==205 and all(p.is_file() and p.read_bytes().startswith(b'\x89PNG') for p in captures))
 counts={}
 for name in ['candidate_tests_20261003','golden_generation_final','shared_final_20261003']:
  events=[json.loads(line) for line in (E/(name+'.jsonl')).read_text(encoding='utf-8-sig').splitlines() if line.startswith('{')]
  done=[x for x in events if x.get('type')=='testDone' and not x.get('hidden')]
  passed=[x for x in done if x.get('result')=='success' and not x.get('skipped')]
  counts[name]={'passed':len(passed),'failed':len(done)-len(passed)}
  expected_count={'candidate_tests_20261003':50,'golden_generation_final':274,'shared_final_20261003':275}[name]
  check(name+' actual execution',len(done)==expected_count and len(done)==len(passed) and any(x.get('type')=='done' and x.get('success') is True for x in events),counts[name])
 check('205 approved golden bytes unchanged',all(digest(E/'screenshots'/n)==h for n,h in approval['existing_capture_sha256'].items()))
 # Coverage is a declared matrix, qualified by the successful executions above.
 check('trace tests executed',all(any(x.get('type')=='testStart' and x.get('test',{}).get('name')==row['test'] for x in events) for row in trace+extra))
 gate=(U/'PHASE2_FINAL_GATE_REPORT.md').read_text(encoding='utf-8')
 check('AtoS final report',all(re.search(r'^## '+c+r'\.',gate,re.M) for c in 'ABCDEFGHIJKLMNOPQRS'))
 state=(R/'02_Tai_lieu_du_an/07_Tien_do_du_an/PHASE_STATUS.yaml').read_text(encoding='utf-8')
 check('Phase3 HOLD',bool(re.search(r'phase_3:.*?status: HOLD.*?eligible: false',state,re.S)))
 check('no assistant human signoff',all(x['human_review']=='PENDING' for x in trace+extra))
 # Check actual local Markdown targets in current entry/candidate docs. Relative
 # plain-text paths and historical/root-relative source examples are not links.
 link_errors=[]; link_count=0
 for p in list(U.glob('*.md'))+[R/x for x in ['README.md','START_HERE.md','PROJECT_MAP.md','REPO_RULES.md']]:
  for target in re.findall(r'\[[^\]\n]+\]\(([^)]+)\)',p.read_text(encoding='utf-8')):
   target=target.strip('<>'); target=target.split('#')[0]
   if not target or re.match(r'^[a-zA-Z]+:',target):continue
   target=re.sub(r':\d+$','',target); link_count+=1
   if not (p.parent/target).resolve().exists():link_errors.append(f'{p.relative_to(R)} -> {target}')
 check('current navigation Markdown links',not link_errors,{'checked':link_count,'errors':link_errors})
 report={'schema':'mingo.evidence_gated.verification.v1','provenance':'RERUN NOW','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
  'scope':'Machine artifact/contract/presentation checks; human and physical-device gates separately pending',
  'counts':counts,'checks':checks,'status':'PASS' if not errors else 'FAIL','errors':errors}
 (E/'CURRENT_CANDIDATE_VERIFICATION.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
 print(json.dumps({'status':report['status'],'checks':len(checks),'errors':errors,'counts':counts},ensure_ascii=False))
 return bool(errors)
if __name__=='__main__':sys.exit(run())
