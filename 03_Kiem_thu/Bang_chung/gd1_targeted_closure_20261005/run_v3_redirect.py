"""Execute existing adapter checks; redirect ONLY evidence/work-copy output paths."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, subprocess, sys
R=Path('C:/Mingo')
E=R/'03_Kiem_thu/Bang_chung/gd1_targeted_closure_20261005'
P=R/'04_Van_hanh/Scripts/check_original_contracts.py'
text=P.read_text(encoding='utf-8')
edits={
 'evidence = ROOT / "03_Kiem_thu/Bang_chung/v3_2" / run_id': 'evidence = Path('+repr(str(E/'v3_2'))+') / run_id',
 'work = ROOT / ".local/v3_2-runs" / run_id': 'work = Path('+repr(str(E/'v3_work'))+') / run_id',
}
for a,b in edits.items():
 assert text.count(a)==1, 'Output redirect must match exactly once'
 text=text.replace(a,b)
(E/'v3_output_redirect.json').write_text(json.dumps({'original':str(P),'original_sha256':hashlib.sha256(P.read_bytes()).hexdigest(),'changes':edits,'conditions_validators_original_hash_checks_unchanged':True},indent=2)+'\n',encoding='utf-8')
original_run=subprocess.run
records=[]
def instrumented_run(command,*a,**kw):
 start=datetime.now(timezone.utc).isoformat()
 result=original_run(command,*a,**kw)
 if not kw.get('stdout')==subprocess.PIPE:
  records.append({'command':subprocess.list2cmdline(command) if isinstance(command,list) else str(command),'cwd':str(kw.get('cwd',R)),'start_utc':start,'end_utc':datetime.now(timezone.utc).isoformat(),'exit_code':result.returncode})
 return result
subprocess.run=instrumented_run
try:
 exec(compile(text,str(P),'exec'),{'__file__':str(P),'__name__':'__main__'})
finally:
 (E/'v3_child_commands.json').write_text(json.dumps(records,indent=2)+'\n',encoding='utf-8')
