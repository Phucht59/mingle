from pathlib import Path
from datetime import datetime,timezone
import json,csv,re,hashlib,difflib,subprocess,collections,xml.etree.ElementTree as ET
R=Path('C:/Mingo'); E=R/'03_Kiem_thu/Bang_chung/gd1_targeted_closure_20261005'; O=R/'03_Kiem_thu/Bao_cao/GD1_Targeted_Closure_20261005'
P=R/'02_Tai_lieu_du_an/04_Thiet_ke_san_pham'; U=P/'ux_ui/phase2'; V=U/'rebaseline_v2'; C=R/'02_Tai_lieu_du_an/05_Kien_truc_he_thong/contracts/v3_2/source'; G=R/'02_Tai_lieu_du_an/06_Quyet_dinh_da_chot'; Q=R/'03_Kiem_thu/QA_QC/phase2'
def load(p): return json.loads(p.read_text(encoding='utf-8'))
def dump(p,v): p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p): return p.read_text(encoding='utf-8-sig')
def lines(p): return read(p).splitlines()
def loc(p,token):
 for i,l in enumerate(lines(p),1):
  if token in l: return f'{p}:{i}'
 return f'{p} [identifier not found: {token}]'
def link(p,token=None):
 s=loc(p,token) if token else str(p)
 return f'[{p.name}{" · "+token if token else ""}]({s.replace(chr(92),"/")})'
def cell(x): return str(x).replace('|',' / ').replace('\n','<br>')
def table(headers,rows): return '\n'.join(['| '+' | '.join(headers)+' |','| '+' | '.join(['---']*len(headers))+' |']+['| '+' | '.join(cell(x) for x in row)+' |' for row in rows])+'\n'
def report(name,text): (O/name).write_text(text.rstrip()+'\n',encoding='utf-8')
dis=load(E/'workbook_discovery.json'); assert dis['result']=='NOT FOUND'
prior=load(E/'FINDINGS_BEFORE_FIXES.json')
reqs=[]
for i,l in enumerate(lines(P/'MVP_PRD.md'),1):
 if re.match(r'\| PRD-\d\d \|',l):
  v=[x.strip() for x in l.strip('|').split('|')]
  reqs.append({'id':v[0],'statement':v[1],'acceptance':v[2],'decision_status':v[3],'priority':'UNKNOWN','priority_source':'Actual BA workbook NOT FOUND; repo PRD has no priority field','locator':f'{P}/MVP_PRD.md:{i}'})
dump(E/'requirement_inventory_before.json',reqs)
catalog=load(V/'SCREEN_CATALOG.json'); screens={s['id']:s for s in catalog}; qa={x['id']:x for x in load(Q/'qa_cases.json')}
with (V/'PRD_TRACEABILITY_V2.csv').open(encoding='utf-8-sig',newline='') as f: mappings=list(csv.DictReader(f))
with (V/'SCREEN_STATE_TRACEABILITY.csv').open(encoding='utf-8-sig',newline='') as f: states=list(csv.DictReader(f))
with (V/'SCREEN_SCOPE_REGISTER.csv').open(encoding='utf-8-sig',newline='') as f: scope={x['screen_id']:x for x in csv.DictReader(f)}
statekey=next(k for k in states[0] if k.lower() in {'state','state_name'})
idkey=next(k for k in states[0] if k.lower() in {'screen','screen_id'})
bad=[]
for m in mappings:
 for k,inv in [('screens',screens),('qa',qa)]:
  for x in m[k].split(','):
   if x not in inv: bad.append({'prd':m['prd'],'type':k,'id':x})
expected={(s['id'],st) for s in catalog for st in s['states']}; actual=[(s[idkey],s[statekey]) for s in states]
struct={'requirements':len(reqs),'mapped_requirements':len(mappings),'screens':len(catalog),'states':len(states),'qa_specs':len(qa),'duplicate_requirements':len(reqs)-len({x['id'] for x in reqs}),'duplicate_screens':len(catalog)-len(screens),'duplicate_states':len(actual)-len(set(actual)),'missing_states':sorted(expected-set(actual)),'extra_states':sorted(set(actual)-expected),'dangling_refs':bad,'priority_unknown':len(reqs),'boundary':'Current repo structure, not workbook semantics or executed QA case IDs'}
dump(E/'structural_audit_current.json',struct)
reqmap={x['id']:x for x in reqs}; mm={x['prd']:x for x in mappings}
journey={1:['J-L01','J-L13'],2:['J-L04'],3:['J-L05','J-L07'],4:['J-L06','J-L13'],5:['J-L07','J-L15'],6:['J-L14','J-L15'],7:[],8:['J-L03'],9:['J-L01','J-L02'],10:['J-L01','J-L02','J-L11'],11:[],12:[],13:['J-L08','J-L10'],14:['J-S01','J-S02'],15:['J-L09','J-L12'],16:['J-L10']}
triggers={1:'Start finite cycle; finish Check; opt-in continue',2:'Wrong first answer → feedback → optional retry',3:'Request practice hint / enter independent Check',4:'Explicit practice Skip; blank required response',5:'Request audio; essential media unavailable',6:'Start grammar/vocabulary/listening objective',7:'Provisional challenge predicate satisfied',8:'Select focus; due review / blocking prerequisite exists',9:'Choose or skip placement',10:'Select/skip/edit goal; open profile/evidence',11:'Qualifying retrieval with feedback; local day',12:'Meaningful milestone under provisional policy',13:'Browse course; locked preview; request next action',14:'Create draft; submit review; return/approve; publish; new revision',15:'Connectivity loss / restoration; queued action/retry; late arrival',16:'Disable/unavailable ML or recommendation; no eligible content'}
testtokens={1:('presentation_test.dart','grammar'),2:('fixture_test.dart','first wrong answer'),3:('fixture_test.dart','hint marks'),4:('fixture_test.dart','skip is not'),5:('fixture_test.dart','audio'),6:('presentation_test.dart','grammar'),7:('fixture_test.dart','challenge'),8:('fixture_test.dart','fallback'),9:('presentation_test.dart','placement'),10:('presentation_test.dart','profile'),11:('presentation_test.dart','profile'),12:('presentation_test.dart','summary'),13:('independent_test.dart','IV04'),14:('independent_test.dart','IV03'),15:('presentation_test.dart','sync'),16:('fixture_test.dart','fallback remains')}
T=R/'01_San_pham/cong_cu_phat_trien/mingo_ui/test'
# Only exact found executable names get a locator. No invented equivalence to legacy QA IDs.
trace=[]
for req in reqs:
 n=int(req['id'][-2:]); m=mm[req['id']]
 j=[]
 for jid in journey[n]:
  jp=U/('04_STAFF_JOURNEYS.md' if jid.startswith('J-S') else '03_LEARNER_JOURNEYS.md')
  j.append({'id':jid,'location':loc(jp,jid),'relation':'SEMANTICALLY SUPPORTED','quoted_text':lines(jp)[int(loc(jp,jid).rsplit(':',1)[1])+1]})
 fn,token=testtokens[n]; tp=T/fn; exe=loc(tp,token)
 if 'identifier not found' in exe: exe='UNKNOWN exact test mapping; selected executable file '+str(tp)
 brsrc=P/'MVP_PRD.md'
 br={'id':'UNKNOWN workbook BR ID','relation':'SEMANTICALLY SUPPORTED','location':req['locator'],'quoted_text':req['statement'],'note':'Rule stated in repo requirement; not a canonical workbook BR edge'}
 if n in [7,8,11,12]:
  flow={'id':'No standalone UC ID in repo','relation':'SEMANTICALLY SUPPORTED','location':loc(P/'learning_design/ADAPTIVE_FEED_MVP_SPEC.md','Selection procedure') if n in [7,8] else req['locator'],'note':'Policy/procedure and PRD acceptance support flow; workbook UC/Trigger IDs unknown'}
 else: flow={'id':','.join(journey[n]),'relation':'SEMANTICALLY SUPPORTED','evidence':j,'note':'Repo journeys explicitly describe operation; no asserted formal workbook relationship'}
 screen_evidence=[]
 for sid in m['screens'].split(','):
  s=screens[sid]; screen_evidence.append({'id':sid,'states':s['states'],'location':loc(V/'SCREEN_CATALOG.json','"id": "'+sid+'"'),'mapping':loc(V/'PRD_TRACEABILITY_V2.csv',req['id']+','),'relation':'EXPLICIT'})
 qa_evidence=[{'id':qid,'location':loc(Q/'qa_cases.json','"id": "'+qid+'"'),'mapping':loc(V/'PRD_TRACEABILITY_V2.csv',req['id']+','),'expected':qa[qid]['expected'],'relation':'EXPLICIT','evidence_type':'SPEC EXISTS; legacy status not current execution'} for qid in m['qa'].split(',')]
 trace.append({**req,'business_need':{'id':'UNKNOWN workbook Need ID','relation':'UNKNOWN','location':'07_RTM NOT FOUND'},'business_rule':br,'trigger':{'id':'UNKNOWN workbook Trigger ID','description':triggers[n],'relation':'SEMANTICALLY SUPPORTED' if j or n in [7,8,11,12] else 'UNKNOWN','location':j[0]['location'] if j else flow['location'] if 'location' in flow else req['locator']},'flow':flow,'screens':screen_evidence,'acceptance':{'location':req['locator'],'text':req['acceptance'],'relation':'EXPLICIT'},'qa_spec':qa_evidence,'executable':{'location':exe,'relation':'SEMANTICALLY SUPPORTED' if not exe.startswith('UNKNOWN') else 'UNKNOWN','evidence_type':'EXECUTABLE EXISTS; selected suites executed separately; no one-to-one legacy QA execution claim'},'result':'PARTIAL','gap':'Actual priority/Need/BR/Trigger/UC/WF workbook IDs and relations UNKNOWN. Runtime validation DEFERRED; applicable repo fixture/spec coverage does not close workbook chain.'})
dump(E/'semantic_trace_current.json',trace)
header='''# Targeted semantic traceability audit — 2026-10-05

AUD-003: **HIGH / OPEN**. Actual workbook NOT FOUND; all 16 actual priorities are **UNKNOWN**. Repo requirement statements and acceptance exist, but accountable P0/P1 inventory and formal Need/BR/Trigger/UC/WF links cannot be certified. No priority is inferred from QA, screen order or this audit.

P0-first audit cannot be performed on an absent actual artifact. Tables below use the PO transfer fingerprint only to arrange the review queue. The Priority column remains UNKNOWN, including every item listed in the diagnostic P0/P1 groups. The fingerprint is not a substitute requirement artifact. Row order does not approve priority.

Relation types: EXPLICIT / SEMANTICALLY SUPPORTED / MISSING / CONFLICT / DEFERRED / NOT APPLICABLE / UNKNOWN. Semantically supported links below cite source text in each detailed row and semantic_trace_current.json. No canonical workbook IDs are created.

'''
rowby={x['id']:x for x in trace}
for title,nums in [('PO fingerprint P0 review queue — actual priority UNKNOWN',[1,2,3,4,10,14,15,16]),('PO fingerprint P1 review queue — actual priority UNKNOWN',[5,6,7,8,9,11,12,13])]:
 header+='## '+title+'\n\n'
 rows=[]
 for n in nums:
  x=rowby[f'PRD-{n:02d}']; m=mm[x['id']]
  rows.append([x['id'],'UNKNOWN','Formal BR UNKNOWN; repo rule: '+link(P/'MVP_PRD.md',x['id']),'Formal Trigger UNKNOWN; '+triggers[n],','.join(journey[n]) or 'PRD/Feed procedure; formal UC UNKNOWN',m['screens'],m['qa']+'; PRD AC; selected suite separately executed','SPEC / EXPLICIT screen-QA map; semantic flow; executable fixture boundary','PARTIAL',x['gap']])
 header+=table(['Requirement','Priority','BR','Trigger','UC/Flow','Screen/State','Acceptance/Test','Evidence Type','Result','Gap'],rows)+'\n'
header+='## Exact row evidence and supported semantics\n\n'
for x in trace:
 n=int(x['id'][-2:]); header+='### '+x['id']+'\n\n'
 header+='Requirement: '+x['statement']+'\n\nDecision classification in repo: '+x['decision_status']+'. Higher PO decisions apply as recorded in PO_DECISION_SYNC_CANDIDATE.md. Source: '+link(P/'MVP_PRD.md',x['id'])+'.\n\n'
 header+='Need ID: UNKNOWN (missing 07_RTM). BR ID: UNKNOWN; **SEMANTICALLY SUPPORTED** rule text is the cited requirement, without claiming a formal BR relationship. Trigger ID: UNKNOWN; supported event: '+triggers[n]+'.\n\n'
 if 'evidence' in x['flow']:
  for y in x['flow']['evidence']: header+='Flow **SEMANTICALLY SUPPORTED**, '+y['id']+' at '+y['location']+': “'+y['quoted_text']+'”.\n\n'
 else: header+='Flow **SEMANTICALLY SUPPORTED** by '+x['flow']['location']+' and the acceptance statement; exact workbook UC ID UNKNOWN.\n\n'
 header+='Screen/state **EXPLICIT** edges: '+link(V/'PRD_TRACEABILITY_V2.csv',x['id']+',')+' → '+', '.join(z['id']+' {'+', '.join(z['states'])+'}' for z in x['screens'])+'. Exact catalog locators in semantic_trace_current.json.\n\n'
 header+='Acceptance **EXPLICIT**: “'+x['acceptance']['text']+'” at '+link(P/'MVP_PRD.md',x['id'])+'. QA spec **EXPLICIT**: '+', '.join(z['id']+' (“'+z['expected']+'”; '+z['location']+')' for z in x['qa_spec'])+'.\n\n'
 header+='Executable support: '+x['executable']['location']+'. Entire three selected files executed in this audit; this is not a claim that individual historical QA IDs ran. Contract/SQL checks apply to original V3.2 and copied PGlite boundary. Production/auth/offline/runtime/human/customer validation remains separate.\n\nResult **PARTIAL**: '+x['gap']+'\n\n'
header+='''## Known workbook observations — not confirmed

| Candidate | Status | Disposition |
| --- | --- | --- |
| A N-06 → WF-10 | UNKNOWN | Actual RTM/WF cells absent. L-011 offline, L-054 downloads, L-060/061 sync, L-050 profile are possible semantic surfaces, but L- IDs do not establish WF- IDs. No replacement is authoritative. |
| B WBS 1.11 DONE | UNKNOWN | No actual status observed. Conditional safe patch only: if DONE and DoD remains unmet, change to ACTIVE; never mark DONE until AUD-003 closes. |
| C requirement Evidence/Wireframe/Test fields | UNKNOWN | No actual cells inspected; safe repo links are recorded above for later reconciliation. |
| D BR Related Req fields | UNKNOWN | Actual BR inventory absent; do not create fictional BR-01..30 mappings. |
| E account BA incompleteness in workbook | UNKNOWN | Repo incompleteness and approved PO gate examined separately in ACCOUNT_LIFECYCLE_CANDIDATE.md. |

## Repair plan

Reconcile every actual requirement priority and Need/BR/Trigger/UC/WF reference against these cited repo edges after the workbook is available. Copy only explicitly supported edges; examine conflicting behavior before any mapping. Check duplicates and dangling IDs in all 16 actual sheets, including hidden sheets, formulas, decision classifications and test types. Do not force fingerprint counts. Keep safe clerical fixes in a separate candidate copy; original hash remains unchanged. No candidate workbook was fabricated.

```mermaid
flowchart LR
    NEED[Business Need: workbook UNKNOWN] --> REQ[Requirement: repo 16; priority UNKNOWN]
    REQ --> BR[Business Rule: repo text; formal ID UNKNOWN]
    BR --> TRG[Trigger: source-supported event; ID UNKNOWN]
    TRG --> UC[Use Case / Flow: repo journey or procedure]
    UC --> UI[Screen / State: explicit repo map]
    UI --> AC[Acceptance Criteria: PRD and QA spec]
    AC --> TEST[Test / Verification: fixture or original contract boundary]
```
'''
report('TRACEABILITY_AUDIT.md',header)

# All candidate paths and hashes, not only selected examples.
disrows=[]
for i,x in enumerate(dis['candidates'],1): disrows.append([i,x['path'],x['sha256'],x['size'],x['modified_utc'],'YES' if x['openable'] else 'NO','; '.join(s['name']+' ('+s['state']+', '+s['range']+')' for s in x['sheets']),x['identity'],x['reason']])
report('WORKBOOK_DISCOVERY.md','# AUD-001 workbook discovery — NOT FOUND\n\n**BLOCKER / OPEN**. Recursive search covered C:/Mingo, hidden and ignored files, archive, outputs and .local; only .git internals were excluded. '+str(dis['candidate_count'])+' Excel paths, '+str(dis['unique_hash_count'])+' unique contents. Every unique openable content was inspected read-only for sheets, used ranges and identifier fingerprints; copies retain individual path/hash/size/time below. No workbook opened then saved. No artifact was rejected solely for a differing hash.\n\nExpected zone: `'+dis['expected_zone']+'`. Filename patterns: '+', '.join(dis['patterns'])+'. Exact title and underscore variant were absent. Workbook identity anchor: `'+dis['workbook_anchor']+'`. Expected sheets: '+', '.join(dis['expected_sheets'])+'.\n\n'+table(['#','Absolute path','SHA-256','Bytes','Modified UTC','Openable','Sheet inventory / state / used range','Identity','Rejection reason'],disrows)+'\n## Snapshot reconciliation\n\n2026-10-04 snapshot NOT FOUND; no exact anchor match. Missing historical snapshot remains non-gating; AUD-002 disposition retained. Current 2026-10-05 snapshot is continuity from the previous audit, superseded on Account/Home by this PO packet.\n\n'+table(['Path','SHA-256','Size','Modified UTC','Identity','Authority'],[[x['path'],x['sha256'],x['size'],x['modified_utc'],x['identity'],x['authority']] for x in dis['snapshots']])+'\n## Closure limits\n\nNo actual BA workbook authority/version or actual sheet inventory can be recorded. Prior workbook observations A–E remain UNKNOWN. No clerical workbook fix is justified without the source; no TARGETED_CANDIDATE.xlsx was created. AUD-001 closes only after a real artifact is opened and its version, hash and content reviewed.\n')

# Orphan registers distinguish real missing formal artifacts from support coverage.
orphans=[]
def orphan(kind,id,relation,source,why,action): orphans.append({'Type':kind,'ID':id,'Relation':relation,'Source':source,'Reason':why,'Action':action})
for kind in ['BR without Req','Trigger without Req/UC','UC without Requirement']:
 orphan(kind,'Actual workbook namespace UNKNOWN','UNKNOWN','BA workbook NOT FOUND','Cannot assert zero or enumerate absent IDs','Inspect actual 04/05/06/07 sheets; resolve or justify every MVP orphan')
usedjourneys={j for v in journey.values() for j in v}
for jf in [U/'03_LEARNER_JOURNEYS.md',U/'04_STAFF_JOURNEYS.md']:
 for i,line in enumerate(lines(jf),1):
  m=re.match(r'## (J-[LS]\d\d)',line)
  if m and m[1] not in usedjourneys:
   jid=m[1]; reason={'J-S03':'Conditional assigned-advisor support; V3.2 docs07 object scope; evidence-safe PRD10; no new intervention authorization','J-S04':'Explicit future intervention; Q12 DEFERRED-FUTURE and audit lifecycle contracts','J-S05':'Explicit analytics shell; future domain, no production data','J-S06':'Administration shell; V3.2 server role/audit, implementation later'}.get(jid,'Repo supporting flow; no direct formal requirement map')
   orphan('UC without Requirement',jid,'DEFERRED' if jid in ['J-S04','J-S05','J-S06'] else 'SEMANTICALLY SUPPORTED',f'{jf}:{i}',reason,'Keep source-derived classification; reconcile actual UC IDs without expanding MVP')
usedscreens={s for m in mappings for s in m['screens'].split(',')}
support={'L-001':('Q3 / J-L01','Launch/recovery infrastructure'),'L-002':('Q3 / J-L01','Guest welcome'),'L-028':('PRD02 / J-L04','Feedback inherited learning step'),'L-033':('Q7 / J-L12','Resume inherited PRD01/15'),'L-053':('Q4 / PRD10','Voluntary profile preferences'),'L-054':('Q10 / V3.2 docs04','Download management; requires authenticated owner'),'L-062':('QA error/accessibility','Generic recovery shell; not new business feature'),'L-064':('V3.2 docs07 / offline UX','Reauth safety state; exact policy UNKNOWN'),'L-070':('Q3 / PRD10','Progress inherited qualitative evidence; durable state auth-gated'),'L-071':('PRD13 / Course catalogue','Search supporting browse; no separate product feature approval'),'L-072':('PRD10 / preferences','Settings support shell'),'L-073':('Existing scope register','Notification preferences fixture; actual delivery/policy deferred'),'S-001':('V3.2 docs07','Staff access shell; UI visibility is not authz'),'S-010':('Existing staff IA','Dashboard shell; no operational data proof'),'S-020':('J-S03 / V3.2 docs07','Assigned learner support shell'),'S-021':('J-S03 / PRD10','Learner overview support'),'S-022':('J-S03 / PRD10','Evidence support; no new risk permission'),'S-023':('J-S03','Activity support; no diagnosis'),'S-031':('Q11 / J-S01 / PRD14','Draft substep'),'S-032':('Q11 / J-S01 / PRD14','Preview substep'),'S-034':('Q11 / J-S01 / PRD14','Review queue substep')}
for sid in sorted(set(screens)-usedscreens):
 src,why=support.get(sid,('Q12 / J-S04..06','Explicit future placeholder; not current MVP implementation'))
 cat=scope[sid]['category']; relation='DEFERRED' if 'FUTURE' in cat else 'SEMANTICALLY SUPPORTED'
 orphan('Wireframe/State without direct business requirement',sid,relation,loc(V/'SCREEN_SCOPE_REGISTER.csv',sid+',')+'; '+src,why+'; inherited catalog is not customer evidence','Retain basis and category; actual WF/business trace UNKNOWN')
mappedqas={x for m in mappings for x in m['qa'].split(',')}
for qid,x in qa.items():
 if qid not in mappedqas:
  basis=x.get('req','').strip(); orphan('Test without direct requirement',qid,'EXPLICIT' if basis else 'UNKNOWN',loc(Q/'qa_cases.json','"id": "'+qid+'"'),'QA spec: '+x['title']+'; declared req='+ (basis or 'blank')+'; expected='+x['expected'],'If no explicit req: identify cited governance/accessibility/navigation/support/future basis before semantic closure; not automatically unauthorized. No new execution of this legacy ID claimed')
for x in reqs: orphan('Requirement without complete acceptance/test chain',x['id'],'UNKNOWN','Actual workbook UNKNOWN; '+x['locator'],'Repo acceptance + QA spec present, formal workbook Test/AC links and runtime proof not known','Map actual AC/Test IDs; distinguish spec, executable and executed')
for category,paths,why in [('Executable check without product requirement',['04_Van_hanh/tests/test_original_contract_adapter.py'],'Foundation adapter guards test audit integrity, not product feature'),('Executable check without product requirement',['01_San_pham/backend/tests'],'API/worker/database foundation; not learning/account implementation'),('Executable check without explicit legacy QA ID',[str(T/x) for x in ['fixture_test.dart','independent_test.dart','presentation_test.dart']],'Named invariants and catalog states inherit PRD/rule coverage; not one-to-one legacy QA result')]:
 for p in paths: orphan(category,p,'SEMANTICALLY SUPPORTED',p,why,'Execution result recorded at suite boundary; do not synthesize QA-ID pass mapping')
dump(E/'orphan_register.json',orphans)
with (O/'ORPHAN_REGISTER.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(orphans[0]));w.writeheader();w.writerows(orphans)
report('ORPHAN_REGISTER.md','# Orphan and inherited/support coverage register\n\nAll six required categories are included. Formal workbook inventories remain UNKNOWN. Current structural checks found '+str(len(bad))+' dangling repo screen/QA links, '+str(struct['duplicate_states'])+' duplicate state rows, '+str(len(expected-set(actual)))+' missing catalog states. This is structural validation. '+str(len(set(screens)-usedscreens))+' screens lack direct PRD CSV mapping; support inheritance and explicit future basis below do not make them automatically unauthorized.\n\n'+table(list(orphans[0]),[list(x.values()) for x in orphans]))

# Candidate PO synchronization. It supersedes prose only within this audit candidate.
request=E/'PO_TARGETED_REQUEST.txt'
def po(q): return link(request,'Q'+str(q)+' —')
decisions=[('Q1','APPROVED OPERATING HYPOTHESIS','Vietnamese 18–35 English beginner/rebuilder; not market validation'),('Q2','APPROVED MVP DIRECTION','English-first; avoid unnecessary hard-code; no new languages'),('Q3','APPROVED','Guest browse/preview; authenticate before Start Learning, Attempt, independent Check, durable Progress, offline learning download, learning sync. Email required supported method; Google target; Facebook DEFERRED-FUTURE; return valid intended context.'),('Q4','APPROVED PRINCIPLE','Goal optional/editable preference; no history/mastery rewrite or prerequisite bypass; categories hypothesis'),('Q5','APPROVED PRINCIPLE','Placement optional; skip nonpunitive; provisional; 6–9 not invariant'),('Q6','APPROVED BASELINE ORDER','Valid unfinished Resume → due Review → next eligible path → goal-matched eligible → deterministic fallback → honest empty. No numeric thresholds or eligibility bypass.'),('Q7','APPROVED PRINCIPLE','Autosave appropriate durable boundary; exit not necessarily abandon; conceptual Resume; no fake saved-progress-loss UX'),('Q8','APPROVED PRINCIPLE','Return without guilt/punishment; short review allowed; absence threshold not frozen'),('Q9','APPROVED LIMITED DIRECTION','Light streak/milestones; not mastery/proficiency; no XP economy/pressure leaderboard/shop as current core'),('Q10','APPROVED / V3.2 REQUIRED','Eligible download before offline; durable local save; later sync; downloaded/pending/syncing/synced/failed distinct; network ≠ synced'),('Q11','APPROVED','Author→Reviewer→Publisher/Admin; Draft→Submit Review→Review→Return/Approve→Publish→Published Revision→New Revision; immutable published'),('Q12','DEFERRED-FUTURE','Advanced Speaking AI/chatbot/social/community/leaderboard/gamification/production Risk Prediction/ML ranking/adaptive optimization/advanced Intervention; not permanently rejected, OUT OF CURRENT MVP IMPLEMENTATION'),('Q13','RESEARCH','Pricing/monetization not frozen'),('Q14','DEFERRED-FUTURE','Child/Guardian separate future UX; no same adult flow'),('Q15','VALIDATION DEBT','Actual discovery not done; no customer/market/PMF/learning/ML efficacy claim')]
report('PO_DECISION_SYNC_CANDIDATE.md','# PO decision synchronization candidate\n\nAuthority: V3.2 > explicit PO packet > actual workbook > repo > snapshots. No canonical file replaced. All approved decisions below are effective audit inputs; candidate prose is an index of their source, not a new approval.\n\n'+table(['Decision','Classification','Meaning','Exact source'],[[id,st,text,po(int(id[1:]))] for id,st,text in decisions])+'\nThe old Account Gate inclusion question and Home-order hypothesis are superseded by Q3/Q6. CR-GD1-001 is not needed for copying these approved decisions. Any unresolved necessary new policy must be assessed separately. All old FIXED/PASS findings retain their disposition; lower historical/current documents awaiting synchronization do not override this packet.\n')

# Account candidate uses source pointers as rules/flows, no fictional BR/UC namespace.
ac=[('AC-A01','Given guest browse of Welcome/demo Home/catalog/course/lesson preview, browsing remains allowed; no learning state/evidence created.',3),('AC-A02','Given guest invokes Start Learning/Attempt/independent Check/durable Progress/offline learning download/learning sync, authentication must precede the protected operation.',3),('AC-A03','Given successful authentication and technically/semantically valid intended context, resume that context; no prerequisite or ownership bypass.',3),('AC-A04','Email is a required supported authentication method; Google is target supported; Facebook is DEFERRED-FUTURE.',3),('AC-A05','Identity/role/object scope derive from verified auth; learner may access only own enrollment/attempt/receipt/grant.',0),('AC-A06','Offline grant/receipt require authenticated owner and contract context; network restored is not synced.',10),('AC-A07','Goal remains optional/editable preference and cannot rewrite history/mastery or bypass prerequisites.',4),('AC-A08','Deletion/export/publish share V3.2 subject-generation race/lock gate; export download blocked once deletion requested; restore closed until ledger reconciliation.',-1)]
account=[
 ('Guest browse','APPROVED','Q3; PRD13 browse is semantically supported','Q3 guest preview / no learning evidence','Guest opens Welcome/demo Home/catalog/course/lesson preview','Q3 browse flow; J-L08 preview subset','L-002/L-010 demo/L-040/L-042; guest variant not explicit in catalog','AC-A01; NOT EXECUTED auth/guest runtime','Q3','Guest variants/gate not in full existing BA chain; formal Req/BR/Trigger/UC/WF IDs UNKNOWN'),
 ('Registration','APPROVED account gate; detailed creation flow UNDECIDED','Q3 account requirement; no explicit registration Req ID','Verified identity before protected learning','Guest chooses account creation before protected action','Candidate intent: guest→auth→valid intended context; registration steps UNKNOWN','No registration screen in actual repo catalog','AC-A02/A03; create-account-specific AC missing','Q3 / V3.2 docs07','No approved creation/failure/minimum credential flow; cannot assert every P0 path defined'),
 ('Login','APPROVED','Q3; formal Req UNKNOWN','Auth before protected operation; verified owner','Guest/returning user requests protected action','Q3 auth gate and return; exact login UC UNKNOWN','L-064 reauth support only; no explicit login screen','AC-A02/A03/A05; NOT EXECUTED runtime','Q3 / V3.2 docs07','Success/failure/session implementation later; full BA failure journey missing'),
 ('Email auth','APPROVED','Q3 method; formal Req UNKNOWN','Email required supported method','Choose supported Email method','Q3 method scope; exact mechanism UNDECIDED','No Email-auth screen/state in catalog','AC-A04; NOT EXECUTED','Q3','Email does not imply password/OTP/magic-link, mandatory verification or policy; do not invent'),
 ('Google auth','APPROVED target supported method','Q3; formal Req UNKNOWN','Google target supported method','Choose Google auth','Q3 method scope; provider-link behavior UNDECIDED','No Google-auth screen/state in catalog','AC-A04; NOT EXECUTED','Q3','Provider linking/unlinking and failure path await approved policy; implementation GĐ4'),
 ('Facebook future','DEFERRED','Q3 / Q12','OUT OF CURRENT MVP IMPLEMENTATION; not permanently rejected','Future only','DEFERRED-FUTURE','NOT APPLICABLE current UI','AC-A04 scope only; no implementation test needed now','Q3','No current gap; no permanent rejection'),
 ('Logout','UNDECIDED minimum business flow; implementation DEFERRED','No explicit repo/workbook Req available','V3.2 requires verified identity; logout/pending-queue policy not specified','User chooses sign out','Exact UC UNKNOWN','No logout state in catalog','No approved logout AC; NOT EXECUTED','V3.2 docs07 gives authority only','Cannot infer local pending-work retention, revoke scope or cross-device logout; minimum scope remains unresolved'),
 ('Session restoration','REQUIRED BY V3.2 CONTRACT: verified identity; exact lifecycle UNDECIDED','Q3/Q7 returning intent; formal Req UNKNOWN','Restore must still respect verified owner; expiry unspecified','Returning user / app restart','J-L12 learning Resume is not an auth-session restoration UC','L-001 bootstrap/L-033 learning Resume/L-064 reauth; support only','AC-A05; NOT EXECUTED auth restore','V3.2 docs07 / Q3 / Q7','No canonical auth session-success/failure flow; no inferred expiry'),
 ('Authentication failure','REQUIRED BY V3.2 CONTRACT authority; flow UNDECIDED','Q3; no formal failure Req','No verified auth → no protected evidence/access; semantic consequence, not invented retry cap','Authentication fails or unavailable','Gate remains unsatisfied; failure/retry/cancel journey UNKNOWN','L-064 required/error; generic L-062 is not login failure proof','AC-A02/A05; no executed auth failure test','Q3 / V3.2 docs07','User failure/recovery handling not complete; no guessed error taxonomy or retry limits'),
 ('Recovery','UNDECIDED minimum capability; exact policy DEFERRED to GĐ4 decision','No explicit approved recovery Req','Credential proof/mechanism not specified','Cannot authenticate with selected method','Recovery UC UNKNOWN','No recovery screen/state','No recovery AC; NOT EXECUTED','No source determines policy; Q3 defines supported methods only','Need source/accountability before minimum recovery scope; exact windows deferred, not marked designed'),
 ('Reauthentication','EXPLICIT IN REPO; sensitive-action policy UNDECIDED','L-064 offline/sync support; V3.2 owner auth','Receipt/grant access requires current valid auth; sensitive reauth policy unknown','Reauth-required state','Offline UX reauth support, not blanket sensitive-action UC','L-064 required/error; L-060 reauth','AC-A05/A06; presentation suite only','V3.2 docs07 / catalog L-064 / offline UX','Do not invent mandatory sensitive-action challenge; classify applicability at GĐ4'),
 ('Device change','REQUIRED BY V3.2 CONTRACT owner/device grant boundaries; BA restore flow UNDECIDED','Q3/Q7 intent; exact Req UNKNOWN','Server owns history; local grant bound to device installation/package','Different device / restore server-backed learner state','No explicit account device-restore UC','L-033 learning Resume not proof of cross-device restore','AC-A05/A06; NOT EXECUTED cross-device runtime','V3.2 docs07 Offline grant / Q7','Concurrent-device policy/recovery window deferred; client cannot declare another device synced'),
 ('Account unavailable/state','UNDECIDED / applicability UNKNOWN','No available account-state Req','Auth required, but suspension/deactivation semantics not specified','Account unavailable if such states are scoped','Unknown applicable state transition','Generic error L-062/L-064 is not suspension flow','No state-specific AC; NOT EXECUTED','Q3 / V3.2 docs07 does not decide suspension','No invented account suspension or deactivation; scope must be verified from workbook'),
 ('Profile/preferences','APPROVED; EXPLICIT IN REPO','PRD10 / Q4','Optional goal preference; no history/eligibility rewrite','View/edit optional goal/profile','J-L11 + Q4; goal editing on L-052','L-050/L-051/L-052/L-053; durable Progress auth gate Q3','AC-A07; PRD10 QA-LRN-017/QA-BIZ-008 spec; fixture suite executed','Q3/Q4 / PRD10','AUD-009 existing default/missing-goal fixture debt retained; actual account trace UNKNOWN'),
 ('Delete account','REQUIRED BY V3.2 CONTRACT boundary; request UX/policy UNDECIDED','V3.2 docs10; formal Req UNKNOWN','Subject-generation/atomic publish/delete; replay deletion ledger before reopening restore','Deletion requested','Contract request/status/control, not completed learner UC','No learner deletion screen/state','AC-A08; original contract/SQL suite executed; native multi-session/runtime NOT EXECUTED','V3.2 docs10','No completed request/auth/status/failure BA chain; grace/recovery window not invented'),
 ('Export data','REQUIRED BY V3.2 CONTRACT boundary; request UX/policy UNDECIDED','V3.2 docs10; formal Req UNKNOWN','Pin generation; recheck with shared lock; abort/clean on deletion; block download when requested','Subject export request','Contract export-job boundary; learner UC UNKNOWN','No export request/result/failure screen','AC-A08; original contract/SQL suite executed; production export NOT EXECUTED','V3.2 docs10','No invented export SLA; request/privacy scope and necessary AC chain not complete'),
 ('Return-to-intended-destination','APPROVED','Q3; formal Req UNKNOWN','Return only if technically/semantically valid; V3 owner/eligibility respected','Successful authentication with stored intended context','Q3 guest→protected intent→auth→valid destination','No explicit auth-destination state chain; L-033 is learning Resume only','AC-A03; NOT EXECUTED auth routing','Q3 / V3.2 docs07','Invalid-context fallback destination UNDECIDED; no invented route/timeout/linking behavior'),
]
dump(E/'account_matrix_current.json',[dict(zip(['Account Capability','Status','Requirement','BR','Trigger','UC','Screen/State','Test/AC','Source','Gap'],x)) for x in account])
ah='''# Account lifecycle synchronization candidate — AUD-005

**HIGH / OPEN; gate blocking.** Q3 has decided whether authentication is required before learning evidence. That inclusion question is closed by PO authority. This does not yet establish the missing actual workbook's minimum lifecycle flows, all required P0 paths, acceptance states or failure/recovery/privacy request behavior. No auth code or tests were changed.

This is candidate documentation, not a replacement canonical workbook or approved additional account policy. The rules below synchronize existing PO/V3.2 meaning. No fictional formal Req/BR/Trigger/UC IDs are assigned. A source pointer can carry several semantic nodes when it explicitly defines their relationship; missing implementation UI may be deferred, but missing required business definition remains visible.

'''
ah+=table(['Account Capability','Status','Requirement','BR','Trigger','UC','Screen/State','Test/AC','Source','Gap'],account)+'\n## Source-derived acceptance candidate\n\n'
for id,text,q in ac:
 src=po(q) if q>0 else link(C/'docs/07_SECURITY_PERMISSION_V3.md','Server authority') if q==0 else link(C/'docs/10_RETENTION_DELETE_RESTORE_V3.md','V3.2 atomic deletion/publish gate')
 ah+=f'- **{id} — specification-only candidate, NOT EXECUTED:** {text} Source: {src}.\n'
ah+='''
## Approved gate flow and state boundary

Guest may preview the approved surfaces. When requesting a protected learning operation, authentication must precede that operation; identity/object scope comes from verified auth. Successful auth returns to intended context only if technically/semantically valid. Failure to authenticate does not authorize the protected operation. Exact recovery/cancel/invalid-destination UI and session mechanics are not supplied by Q3; they remain explicit gaps rather than guessed product behavior. Neither opening a preview nor a retry creates canonical progress.

```mermaid
flowchart TD
    G[Guest browse / preview: Q3 approved] --> I[Protected learning intent: Q3]
    I --> A[Auth required before learning evidence]
    A --> E[Email required supported method]
    A --> GO[Google target supported method]
    A -. future .-> FB[Facebook DEFERRED-FUTURE]
    E --> V[Verified identity / object scope: V3.2]
    GO --> V
    V --> K{Intended context valid?}
    K -->|Yes| D[Return to intended destination: Q3]
    K -->|No| U[Fallback behavior UNDECIDED]
    A -->|Auth unsuccessful| F[Protected operation remains gated]
    F -. missing BA flow .-> R[Failure / recovery / cancel specification UNKNOWN]
```

## Policy questions and safe deferral

| Policy | Classification | Reason | Target / owner |
| --- | --- | --- | --- |
| Mandatory email verification; Email mechanism | UNDECIDED; exact mechanism deferred | Q3 requires supported Email, not password/OTP/magic-link or mandatory verification. | GĐ4 identity BA/design before implementation; PO + security owner |
| Exact recovery proof/window | UNDECIDED; exact policy deferred | No approved recovery mechanism; do not invent. Minimum recovery capability/flow still requires source confirmation. | GĐ4 identity BA/design; PO + security owner |
| Session expiry/concurrent devices/logout revocation | UNDECIDED; exact numbers/policy deferred | Verified owner boundary known; session mechanics are not fixed. Minimum returning/logout flow remains a BA gap. | GĐ4; PO + Tech Lead |
| Suspended/deactivated account behavior | Applicability UNKNOWN | Do not invent account states. Inspect actual workbook before requesting a new rule. | Workbook reconciliation, then GĐ4 if necessary |
| Export SLA; deletion grace/recovery window | Exact policy deferred; contract controls REQUIRED | V3.2 generation/race/restore semantics remain fixed. Deferring SLA does not waive learner request/auth/status/failure BA. | Before GĐ4/data-rights implementation and external pilot; PO + privacy reviewer |
| Provider linking/unlinking | DEFERRED decision | Supported Email/Google does not determine linking semantics. Not necessary to synchronize Q3. | GĐ4 before introducing provider-link feature; PO + security owner |

No new CR-GD1-001 is raised for copying the approved Account Gate, methods, Home order or other Q4–Q11 principles. The old broad scope CR is superseded **within the candidate** as NOT REQUIRED for those decisions. No evidence proves a new semantic amendment is necessary now: first inspect the actual workbook. If necessary minimum business policy remains undecided after reconciliation, a narrowly scoped DRAFT CR must state the exact question, affected P0 path and alternatives; no automatic approval or invented answer.

## AUD-005 closure checklist

| Condition | Result |
| --- | --- |
| Account Gate traceable | PASS at PO/V3.2/source-derived candidate level (AC-A01..06); formal workbook chain UNKNOWN |
| Minimum MVP account behavior scoped | PARTIAL: protected learning boundary/methods/return intent approved; full creation/logout/restore/recovery/request flows unavailable |
| Every necessary lifecycle specified/deferred/escalated | PARTIAL: exact policy decisions deferred; necessity and completeness of minimum behavior cannot be proven from missing workbook |
| No P0 learning path depends on undefined auth behavior | UNKNOWN: actual priority/requirements absent; cannot certify this condition |
| Deletion/export/privacy not falsely implemented | PASS reporting boundary: contract/spec/check differs from runtime/learner flow |
| Auth implementation later GĐ4/appropriate stage | DEFERRED; engineering Phase3 remains HOLD, distinct numbering |
| No auth implementation in this task | PASS source preservation; no source edits |

AUD-005 stays HIGH/OPEN because required closure conditions remain unverified. The blocker is incomplete available BA evidence, not whether account is required or absence of runtime Auth. Exact numeric policies alone do not become GĐ1 blockers; the missing minimum paths/source completeness do.
'''
report('ACCOUNT_LIFECYCLE_CANDIDATE.md',ah)

# Exact, reviewable candidate doc edits; originals byte-preserved.
candidate_dir=O/'candidate_docs'; candidate_dir.mkdir(exist_ok=True)
changes=[]
def candidate(p,transform):
 original=read(p); updated=transform(original); assert updated!=original
 # Preserve canonical-relative destinations when the full candidate is moved.
 def absolutize(m):
  destination=m[1]
  if destination.startswith(('http://','https://','C:/','C:\\','#')): return m[0]
  target=(p.parent/destination).resolve()
  return ']('+target.as_posix()+')' if target.exists() else m[0]
 updated=re.sub(r'\]\(([^\n\)]+)\)',absolutize,updated)
 target=candidate_dir/p.name; target.write_text(updated,encoding='utf-8')
 diff=''.join(difflib.unified_diff(original.splitlines(keepends=True),updated.splitlines(keepends=True),fromfile=str(p),tofile=str(target)))
 (candidate_dir/(p.stem+'.patch')).write_text(diff,encoding='utf-8')
 changes.append({'canonical':str(p),'canonical_sha256':sha(p),'candidate':str(target),'candidate_sha256':sha(target),'patch':str(candidate_dir/(p.stem+'.patch'))})
def decfix(t):
 old='Exact duration, Vietnam 18–35/beginner-rebuilder wedge, placement count, goal categories, retry/replay/skip/challenge/focus limits, streak/rewards/pricing and exact Home ranking'
 assert old in t; t=t.replace(old,'Exact duration, placement count, goal categories, retry/replay/skip/challenge/focus limits and exact streak/reward mechanics; Q1 wedge is APPROVED OPERATING HYPOTHESIS, Q13 pricing remains RESEARCH')
 old='| Account lifecycle MVP boundary and specific role-assignment/segregation policies absent from inspected sources | CHƯA QUYẾT ĐỊNH; candidate scope CR, no invented policy |'
 assert old in t; t=t.replace(old,'| Account Gate/methods/destination and Home order | ĐÃ CHỐT by authoritative PO packet Q3/Q6; detailed lifecycle and role-assignment policies remain explicitly undecided where source absent |')
 return t+'\n## PO targeted-closure packet — 2026-10-05 (candidate synchronization)\n\nV3.2 remains highest authority. Q3: guest browse/preview is allowed; authenticate before Start Learning, Attempt, independent Check, durable Progress, offline learning download and learning sync. Email is a required supported method, Google a target supported method, Facebook DEFERRED-FUTURE. Return to intended destination only if technically/semantically valid. Q6 approved Home order: valid unfinished Resume → due Review → next eligible path → goal-matched eligible → deterministic fallback → honest empty. No numeric policy is added. Q12 advanced Speaking AI/chatbot/social/community/leaderboard/advanced gamification/production Risk Prediction/ML ranking/adaptive optimization/advanced Intervention are DEFERRED-FUTURE and OUT OF CURRENT MVP IMPLEMENTATION, not permanently rejected. Q15 discovery remains VALIDATION DEBT. Detailed account policy is not inferred from supported methods. See the targeted audit candidate account matrix and source packet.\n'
candidate(G/'DECISION_REGISTER.md',decfix)
def prdfix(t):
 old='account lifecycle scope still require reconciliation'; assert old in t
 t=t.replace(old,'account lifecycle trace still require reconciliation against Q3 (Account Gate already approved)')
 return t+'\n## Approved PO Account Gate and Home order — candidate synchronization 2026-10-05\n\nGuest may browse Welcome/product intro/demo Home/catalog/Course/Lesson preview. Authentication is required before Start Learning, Attempt, independent Check, durable Progress, offline learning download and learning sync. Email is required supported; Google is target supported; Facebook is DEFERRED-FUTURE. After auth, return to the intended context only if technically/semantically valid. This does not decide Email mechanism, session expiry, recovery, provider linking or deletion/export timing.\n\nHome next-action order approved by Q6: valid unfinished Resume; due Review; next eligible path; goal-matched eligible; deterministic fallback; honest empty. Goal does not bypass prerequisites. Item selection/in-cycle insertion thresholds remain separate dated hypotheses. Advanced future capabilities in Q12 are out of current MVP implementation, not permanently rejected. Account/trace completeness remains unverified pending actual BA workbook; auth runtime remains later stage.\n'
candidate(P/'MVP_PRD.md',prdfix)
def crfix(t):
 start=t.index('## Candidate CR-GD1-001'); end=t.index('## Candidate CR-GD1-002',start)
 new='''## Candidate CR-GD1-001 — superseded broad inclusion question

- Candidate synchronization disposition: **NOT REQUIRED for approved PO Q3–Q11 semantics**, 2026-10-05. Guest browse, learning Account Gate, Email/Google targets, Facebook future and valid intended-destination return are approved; copy these decisions into documentation without requesting them again.
- AUD-005 remains HIGH/OPEN for incomplete available lifecycle BA evidence. No necessary new business policy or V3.2 conflict is proven by the missing workbook.
- First reconcile the actual BA workbook. Exact Email verification/mechanism, recovery, session/concurrent-device, suspension, provider-linking and deletion/export timing remain undecided or deferred to appropriate GĐ4 decision/design before implementation.
- If a required P0 path demonstrably depends on an unapproved new policy after source reconciliation, prepare a narrowly scoped **DRAFT** CR with exact questions and impact. Do not invent answers or silently amend V3.2.
- Original canonical text and previous audit remain preserved; this candidate is not applied.

'''
 t=t[:start]+new+t[end:]
 t=t.replace('Exact Home ranking and goal categories remain hypotheses.','Q6 now approves Home next-action order; exact goal categories remain hypotheses.')
 t=t.replace('Do not change numerical policies or freeze candidate Home ranking.','Do not change numerical policies; synchronize Q6 approved Home order.')
 t=t.replace('Introducing a fixed ranking would prematurely freeze a hypothesis.','The candidate UI must respect Q6 approved Home order; item-policy thresholds remain hypotheses.')
 return t
candidate(G/'CHANGE_REQUESTS.md',crfix)
dump(E/'candidate_doc_hashes.json',changes)
report('CANDIDATE_DOC_PATCHES.md','# Candidate documentation patches and before/after disposition\n\nAll three canonical documents remain untouched. Full candidate copies and unified patches are reviewable under candidate_docs; hashes distinguish source and proposed output. These edits synchronize explicit PO authority; no new account mechanism, ranking threshold or V3.2 semantic is introduced. The original broad CR-GD1-001 question is not repeated. AUD-009/AUD-010 and all prior FIXED/PASS findings retain their status.\n\n'+table(['Canonical source / SHA-256','Candidate / SHA-256','Patch'],[[x['canonical']+' / '+x['canonical_sha256'],x['candidate']+' / '+x['candidate_sha256'],x['patch']] for x in changes])+'\n'+table(['Location','Observed BEFORE','Disposition AFTER','CR required','Canonical applied?'],[['DECISION_REGISTER GĐ1 table','Account inclusion undecided, exact Home ranking hypothesis','Candidate Q3/Q6 approved; policy gaps visible; Q1 operating hypothesis/Q12 future/Q15 debt synchronized','NO','NO'],['MVP_PRD release/account scope','Account scope reconciliation pending; no explicit Q3 gate','Candidate explicit guest/protected operations/methods/valid return and approved Home order','NO','NO'],['CHANGE_REQUESTS CR-GD1-001','Broad new account inclusion question','Candidate superseded as NOT REQUIRED for already-approved semantics; narrow CR only if later proven necessary','NO new CR now','NO'],['CHANGE_REQUESTS CR-GD1-002','Home order described as hypothesis','Candidate recognizes approved Q6 order; existing non-gating fixture debt unchanged','NO semantic amendment','NO'],['Workbook RTM N-06→WF-10','UNKNOWN: no actual workbook','No replacement guessed; candidate targets documented only','UNKNOWN if semantic change necessary','NO'],['Workbook WBS1.11','UNKNOWN actual status','Conditional DONE→ACTIVE patch plan if DoD unmet; never claimed fixed','NO for supported status correction','NO']]))

# Mandatory consistency matrix: broad areas reviewed only as boundary checks for target findings.
snapshot=dis['snapshots'][0]['path'] if dis['snapshots'] else 'NOT FOUND'
areas=[
 ('Architecture','01_MASTER_BASELINE_V3.md','Protected baseline','README.md','Architecture remains frozen'),
 ('Authority','13_FREEZE_LIST_V3.md','Level1→5 hierarchy','MVP_PRD.md','PO Q3/Q6 supersede old account/order prose'),
 ('Content versioning','02_MVP_INVARIANTS.md','Q11 immutable published revision','MVP_PRD.md','PRD14 + J-S01/J-S02; published pin boundary'),
 ('Learning evidence','02_MVP_INVARIANTS.md','Q3/Q7; first response/assistance/skip principles','MVP_PRD.md','PRD01–04/10 + Evidence model; no mastery from skip'),
 ('Assessment','02_MVP_INVARIANTS.md','Q5 optional/provisional; independent Check','MVP_PRD.md','PRD02/03/05/09; no full offline authoritative score'),
 ('Offline','04_OFFLINE_CONTENT_ACCESS_PROTOCOL.md','Q3/Q10 eligible download/auth owner/pending≠synced','MVP_PRD.md','PRD15 + J-L09/J-L12; fixture≠durable runtime'),
 ('Telemetry','03_RECEIPT_SYNC_PROTOCOL.md','No psychological inference; command≠telemetry','MVP_PRD.md','PRD15; purpose/minimization and disabled collection remain'),
 ('Analytics','05_POINT_IN_TIME_SOURCE_CAPTURE.md','Source capture and event≠known-at','MVP_PRD.md','PRD15 historical read-view; no current-data backfill claim'),
 ('Recommendation','09_RECOMMENDATION_AUDIT_V3.md','Q6 approved Home order / Q4 eligible goals','MVP_PRD.md','PRD13/16 + Feed; Home priority and within-cycle policy distinct'),
 ('ML optionality','06_ML_CONTRACT_V3.md','Q12 production ML DEFERRED-FUTURE','MVP_PRD.md','PRD16 rule/fallback; research≠ML efficacy'),
 ('Privacy','10_RETENTION_DELETE_RESTORE_V3.md','No invented SLA/grace/recovery','GD1_INTERNAL_BA_CLOSURE_NOTES_20261005.md','Generation/delete/export/restore fixed; learner request flow UNKNOWN'),
 ('Actors','07_SECURITY_PERMISSION_V3.md','Q11 staff roles; Q14 guardian future','GD1_INTERNAL_BA_CLOSURE_NOTES_20261005.md','Assigned advisor/content admin/platform admin/worker boundaries; AUD004 retained FIXED'),
 ('Account','07_SECURITY_PERMISSION_V3.md','Q3 approved gate/methods/valid return','MVP_PRD.md','Candidate account matrix; minimum lifecycle gaps remain'),
 ('Staff/content','07_SECURITY_PERMISSION_V3.md','Q11 Author→Reviewer→Publisher/Admin','MVP_PRD.md','PRD14/J-S01..02; no enterprise CMS; auth later'),
 ('NFR','12_ACCEPTANCE_TESTS_V3.md','No arbitrary numeric policy; no runtime overclaim','GD1_INTERNAL_BA_CLOSURE_NOTES_20261005.md','AUD006 retained FIXED consolidation; native/runtime checks pending'),
 ('Scope','01_MASTER_BASELINE_V3.md','Q1 operating hypothesis/Q2 English-first/Q12/Q14 future/Q15 debt','MVP_PRD.md','No future capability promoted; no permanently rejected Q12 interpretation'),
 ('Traceability','12_ACCEPTANCE_TESTS_V3.md','Actual priority only; semantic chain required','MVP_PRD.md','16 repo PRDs/61 screens/175 states; actual workbook unknown'),
]
matrix=[]
for area,doc,poText,repo,comment in areas:
 result='PARTIAL — repo boundaries consistent; workbook UNKNOWN'
 finding='AUD-001/AUD-003'
 if area in ['Account','Privacy']: finding+='; AUD-005'
 matrix.append([area,link(C/'docs'/doc),poText+'; '+link(request), 'NOT FOUND; actual sheet/cell UNKNOWN',link(P/repo)+'; '+comment,snapshot+' (prior continuity, lower authority)',result,finding])
report('CONSISTENCY_MATRIX.md','# Targeted consistency matrix\n\nThis matrix preserves prior FIXED/PASS findings. It reviews authority and semantic boundaries relevant to AUD-001/003/005; no new general audit or implementation is claimed. Workbook absence prevents cross-artifact PASS even when repo/V3.2 source is structurally consistent. Q3/Q6 lower-document drift has a candidate synchronization patch; canonical documents remain unchanged.\n\n'+table(['Area','V3.2','PO Decision','Workbook','Repo','Snapshot','Result','Finding'],matrix))

# Findings: exact required schema and preserved IDs. No replacement IDs or reopened fixed items.
fields=['ID','Severity','Status','Area','Artifact','Location','Observed','Expected','Evidence','Source of truth','Impact','Recommended action','Change Request required','Gate blocking','Before fix','After fix']
findings=[]
for old in prior['findings']:
 x={f:old.get(f,'') for f in fields}; x['Before fix']=old.get('Observed','')+' Previous status='+old['Status']; x['After fix']='Prior disposition retained; outside targeted scope. '+old.get('After audit','')
 if x['ID']=='AUD-001':
  x.update(Observed='NOT FOUND after recursive hidden/ignored search: 116 Excel paths, 12 unique contents; every plausible candidate inspected; no expected BA sheet family or exact hash anchor.',Evidence='workbook_discovery.json; WORKBOOK_DISCOVERY.md; artifact_candidates.txt',Location='C:/Mingo entire tree including 02_Tai_lieu_du_an, 99_Luu_tru, outputs, .local; expected canonical BA zone',Artifact='Mingo GD1 — Quản lý Phân tích Nghiệp vụ.xlsx (absent)',Status='OPEN',Severity='BLOCKER')
  x['After fix']='No fabrication/candidate workbook. Known A–E observations UNKNOWN. AUD-001 not closed.'
 elif x['ID']=='AUD-003':
  x.update(Observed='16 current repo requirement statements/AC inspected; all actual priorities UNKNOWN. Current explicit screen/QA mappings have zero dangling references; complete formal workbook Need/BR/Trigger/UC/WF/AC/Test chains not available.',Evidence='requirement_inventory_before.json; semantic_trace_current.json; structural_audit_current.json; TRACEABILITY_AUDIT.md; ORPHAN_REGISTER.md',Status='OPEN',Severity='HIGH')
  x['After fix']='Source-cited repo semantic table/orphan register and safe repair plan supplied. Fingerprint ordering does not set priority. Candidate trace does not close actual workbook chain.'
 elif x['ID']=='AUD-005':
  x.update(Observed='Q3 definitively approves Guest/Account Gate, Email required supported/Google target/Facebook future and valid intended return. Full minimum registration/logout/session/failure/recovery/device/privacy request BA chain remains unavailable; actual P0 dependency completeness UNKNOWN.',Expected='Trace approved gate and every necessary minimum lifecycle capability, explicitly scoped/deferred or narrowly escalated without invented policies.',Evidence='PO_TARGETED_REQUEST.txt Q3; V3.2 docs07/docs10; account_matrix_current.json; ACCOUNT_LIFECYCLE_CANDIDATE.md; candidate_docs/CHANGE_REQUESTS.patch',Status='OPEN',Severity='HIGH')
  x['Change Request required']='NO for approved PO synchronization; conditional DRAFT only if a necessary new unapproved business policy is proven after source reconciliation'
  x['Recommended action']='Inspect actual workbook first; reconcile approved Q3 gate and source-derived AC, resolve minimum lifecycle/necessary P0 gaps. Exact policy decisions may defer to GĐ4 with owner; do not request account inclusion again.'
  x['After fix']='Approved gate/method/destination inclusion synchronized in candidate; 17-capability account matrix and 8 source-derived spec-only AC supplied. Broad CR-GD1-001 superseded as not required for approved semantics in candidate. AUD-005 remains OPEN; runtime auth not implemented.'
 findings.append(x)
dump(O/'FINDING_REGISTER.json',{'date':'2026-10-05','verdict':'FAIL','source_hierarchy':'V3.2 > explicit PO packet > actual BA workbook > repo > snapshot','findings':findings})
ft='# Findings — before/after targeted closure\n\nExisting IDs and prior FIXED/PASS dispositions are preserved; no new distinct issue requiring AUD-013 was confirmed. Candidate synchronization is not canonical application.\n\n'
for x in findings:
 ft+='## '+x['ID']+'\n\n'+'\n\n'.join(f'**{f}:** {x[f]}' for f in fields)+'\n\n'
report('FINDING_REGISTER.md',ft)
dump(E/'semantic_pack_counts.json',{'requirements':len(reqs),'trace_rows':len(trace),'account_capabilities':len(account),'candidate_acceptance':len(ac),'consistency_areas':len(matrix),'orphans':len(orphans),'candidate_docs':len(changes),'critical_open':[x['ID'] for x in findings if x['Severity'] in ['BLOCKER','HIGH'] and x['Status']=='OPEN']})
print(json.dumps({'structure':struct,'reports':len(list(O.glob('*.md'))),'findings_open':[x['ID'] for x in findings if x['Gate blocking']=='YES']},ensure_ascii=False))
