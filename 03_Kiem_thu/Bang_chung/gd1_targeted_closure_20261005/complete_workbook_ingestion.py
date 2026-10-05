"""Complete read-only ingestion for XLSX sheets lacking cached dimensions."""
from pathlib import Path
import json, re, warnings, shutil, collections
import openpyxl
E=Path('C:/Mingo/03_Kiem_thu/Bang_chung/gd1_targeted_closure_20261005')
path=E/'workbook_discovery.json'
shutil.copyfile(path,E/'workbook_discovery_attempt1.json')
d=json.loads(path.read_text(encoding='utf-8')); cache={}
for x in d['candidates']:
 digest=x['sha256']
 if digest not in cache:
  out={'openable':False,'sheets':[],'expected_sheet_overlap':0,'fingerprint_ids':{},'content_labels':[],'formula_count':0}
  try:
   with warnings.catch_warnings():
    warnings.simplefilter('ignore')
    w=openpyxl.load_workbook(x['path'],read_only=True,data_only=False)
    for s in w:
     dimension=s.calculate_dimension(force=True)
     out['sheets'].append({'name':s.title,'state':s.sheet_state,'range':dimension,'rows':s.max_row,'columns':s.max_column})
     for row in s.iter_rows():
      for c in row:
       v=c.value
       if isinstance(v,str):
        if len(out['content_labels'])<12 and c.row<=5 and not v.startswith('='): out['content_labels'].append(s.title+'!'+c.coordinate+': '+v[:160])
        if v.startswith('='):out['formula_count']+=1
        for id in re.findall(r'\b(?:PRD|BR|TRG|TRIGGER|UC|WF|N)-\d{1,3}\b',v):out['fingerprint_ids'].setdefault(id,[]).append(s.title+'!'+c.coordinate)
    out['expected_sheet_overlap']=len(set(w.sheetnames)&set(d['expected_sheets'])); out['openable']=True; w.close()
  except Exception as ex:out['error']=str(ex)
  cache[digest]=out
 x.pop('error',None); x.update(cache[digest]); match=digest==d['workbook_anchor'] or x['expected_sheet_overlap']>=5
 x['selection']='REVIEW BA CANDIDATE' if match else 'REJECTED AS BA WORKBOOK'
 x['reason']='Inspect BA-family version; identity/content match' if match else ('Excel lock file/non-XLSX content; not an openable workbook' if not x['openable'] else f"Content inspected: {len(x['sheets'])} sheets, {x['expected_sheet_overlap']}/16 expected-sheet overlap. Labels show project management/UX-QA dashboard, not 16-sheet GD1 BA. Different SHA alone is not a rejection.")
d['ba_candidates']=[x['path'] for x in d['candidates'] if x['selection'].startswith('REVIEW')]
d['result']='FOUND' if d['ba_candidates'] else 'NOT FOUND'
d['ingestion_note']='Attempt1 kept. XLSX without dimension metadata were re-read with calculate_dimension(force=True); no save or mutation.'
path.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'result':d['result'],'unique_sheets':{Path(next(x['path'] for x in d['candidates'] if x['sha256']==h)).name:[s['name'] for s in c['sheets']] for h,c in cache.items()}},ensure_ascii=False))
