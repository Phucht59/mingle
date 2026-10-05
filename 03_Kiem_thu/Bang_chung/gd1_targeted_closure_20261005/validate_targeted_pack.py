from pathlib import Path
import json,re,hashlib,csv
R=Path('C:/Mingo'); E=R/'03_Kiem_thu/Bang_chung/gd1_targeted_closure_20261005'; O=R/'03_Kiem_thu/Bao_cao/GD1_Targeted_Closure_20261005'
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
checks=[]
def check(n,v):checks.append({'check':n,'pass':bool(v)})
req=['EXECUTIVE_TARGETED_CLOSURE.md','GATE_RECOMMENDATION.md','WORKBOOK_DISCOVERY.md','TRACEABILITY_AUDIT.md','ORPHAN_REGISTER.md','ACCOUNT_LIFECYCLE_CANDIDATE.md','CONSISTENCY_MATRIX.md','PO_DECISION_SYNC_CANDIDATE.md','CANDIDATE_DOC_PATCHES.md','CHECK_RESULTS.md','SOURCE_PRESERVATION.md','FINDING_REGISTER.md','FINDING_REGISTER.json']
check('Required report files present/nonempty',all((O/p).exists() and (O/p).stat().st_size>0 for p in req))
c=load(E/'semantic_pack_counts.json');f=load(E/'final_counts.json');d=load(E/'workbook_discovery.json');s=load(E/'source_preservation.json');find=load(O/'FINDING_REGISTER.json')['findings']
check('16 trace requirements; all actual priority UNKNOWN',len(load(E/'semantic_trace_current.json'))==16 and all(x['priority']=='UNKNOWN' for x in load(E/'semantic_trace_current.json')))
check('17 area matrix / 17 account capabilities / 8 source-derived candidate AC',c['consistency_areas']==17 and c['account_capabilities']==17 and c['candidate_acceptance']==8)
check('All plausible candidates retained with path/hash/size/time and real read-only sheet metadata',len(d['candidates'])==116 and d['unique_hash_count']==12 and all(x.get('path') and x.get('sha256') and x.get('size') and x.get('modified_utc') and (x['sheets'] if x['openable'] else x.get('error')) for x in d['candidates']))
check('Workbook NOT FOUND; five prior candidates UNKNOWN',d['result']=='NOT FOUND' and all('| '+x in (O/'TRACEABILITY_AUDIT.md').read_text(encoding='utf-8') for x in ['A N-06','B WBS','C requirement','D BR','E account']))
check('Exact original request captured byte for byte',sha(E/'PO_TARGETED_REQUEST.txt')==load(E/'audit_paths.json')['request_sha256'])
check('Original102 / contract115 / SQL22',f['original_hashes']==102 and f['v3_contract']['passed']==115 and f['v3_contract']['failed']==0 and f['v3_sql']['passed']==22 and f['v3_sql']['failed']==0)
check('Actual executed Flutter232/0/0 and backend9/0/7',f['flutter']=={'passed':232,'failed':0,'skipped':0} and f['backend']['passed']==9 and f['backend']['failed']==0 and f['backend']['skipped']==7)
check('No protected source/workbook/status change',not s['changed'] and not s['missing'] and not s['workbook_bytes_changed'] and not s['unexpected_status_added'] and not s['unexpected_status_removed'] and s['head_before']==s['head_after'])
check('Loaded backend source boundary current',load(E/'backend_loaded_source_boundary.json')['all_match'])
check('Prior12 IDs/statuses retained, three targeted findings OPEN, gateFAIL',len(find)==12 and f['gate']=='FAIL' and f['open_gate_findings']==['AUD-001','AUD-003','AUD-005'] and all(x['Status']==next(y['Status'] for y in load(E/'FINDINGS_BEFORE_FIXES.json')['findings'] if y['ID']==x['ID']) for x in find))
requiredfields=['ID','Severity','Status','Area','Artifact','Location','Observed','Expected','Evidence','Source of truth','Impact','Recommended action','Change Request required','Gate blocking','Before fix','After fix']
check('Finding schema exact',all(list(x)==requiredfields for x in find))
check('Candidate canonical source hashes retained',all(sha(Path(x['canonical']))==x['canonical_sha256'] for x in load(E/'candidate_doc_hashes.json')))
check('No fabricated workbook',not list(O.glob('*.xlsx')))
check('Balanced Mermaid/code fences',all(p.read_text(encoding='utf-8').count('```')%2==0 for p in O.rglob('*.md')))
broken=[];links=0
for p in O.rglob('*.md'):
 for target in re.findall(r'\]\(([^\n\)]+)\)',p.read_text(encoding='utf-8')):
  if target.startswith(('https://','http://')):continue
  links+=1
  target=target.strip('<>');m=re.match(r'^(.*):(\d+)$',target);line=None
  if m:target=m[1];line=int(m[2])
  q=Path(target);q=q if q.is_absolute() else p.parent/q
  if not q.exists():broken.append({'from':str(p),'target':target,'error':'missing'})
  elif line and line>len(q.read_text(encoding='utf-8-sig').splitlines()):broken.append({'from':str(p),'target':target,'error':'line outside source'})
check('All local report links and exact line locators exist',not broken)
fields={x['Type'] for x in load(E/'orphan_register.json')}
check('All six orphan categories represented',all(x in fields for x in ['BR without Req','Trigger without Req/UC','UC without Requirement','Wireframe/State without direct business requirement','Test without direct requirement','Requirement without complete acceptance/test chain']))
result={'status':'PASS' if all(x['pass'] for x in checks) else 'FAIL','boundary':'Audit pack consistency only; GĐ1 gate remains FAIL','checks':checks,'links_checked':links,'broken_links':broken}
(E/'audit_pack_validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
manifest=[]
for directory in [O,E]:
 for p in directory.rglob('*'):
  if p.is_file() and not p.is_relative_to(E/'v3_work') and p.name!='deliverable_manifest.json':manifest.append({'path':str(p),'size':p.stat().st_size,'sha256':sha(p)})
(E/'deliverable_manifest.json').write_text(json.dumps({'files':manifest,'excluded':'Isolated generated v3_work copy and node_modules; original source checksum inventory and fresh v3_2 results are separately recorded.'},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':result['status'],'checks':len(checks),'links':links,'failures':[x for x in checks if not x['pass']],'broken_links':broken,'manifest_files':len(manifest)},ensure_ascii=False))
raise SystemExit(0 if result['status']=='PASS' else 1)
