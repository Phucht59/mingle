"""Executable contract checks. No network, model loading, or production mutation.
Shape validation is always followed by named semantic checks. Runtime auth,
transactions, model quality and deployments require separate integration gates.
"""
import copy, hashlib, json, math, re, sys
from datetime import datetime, timezone
from pathlib import Path
import rfc8785
from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://contracts.invalid/schemas/'

def fail(message): raise ValueError(message)
def require(ok, message):
    if not ok: fail(message)
def strict_json(text):
    def pairs(items):
        result={}
        for k,v in items:
            require(k not in result, 'duplicate JSON object key: '+k);result[k]=v
        return result
    return json.loads(text, object_pairs_hook=pairs,
                      parse_constant=lambda x: fail('non-finite JSON number: '+x))
def load(rel): return strict_json((ROOT/rel).read_text(encoding='utf-8'))
def digest(obj): return hashlib.sha256(rfc8785.dumps(obj)).hexdigest()
def file_hash(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def instant(s):
    d=datetime.fromisoformat(s.replace('Z','+00:00'))
    require(d.tzinfo is not None,'timezone required')
    return d.astimezone(timezone.utc)
def near(a,b,tol=1e-9):return math.isclose(a,b,rel_tol=tol,abs_tol=tol)

def schema_environment():
    schemas={};registry=Registry()
    for p in sorted((ROOT/'schemas').rglob('*.json')):
        key=p.relative_to(ROOT/'schemas').as_posix();s=strict_json(p.read_text());s['$id']=BASE+key
        Draft202012Validator.check_schema(s);schemas[key]=s
        registry=registry.with_resource(BASE+key,Resource.from_contents(s))
    return schemas,registry
SCHEMAS,REGISTRY=schema_environment()
def shape(name,obj):
    key=name if name.endswith('.json') else name+'_v1.schema.json'
    errors=list(Draft202012Validator(SCHEMAS[key],registry=REGISTRY,format_checker=FormatChecker()).iter_errors(obj))
    require(not errors,'schema '+key+': '+('; '.join(e.message for e in errors[:3])))

def command_digest(command):
    shape('submit_attempt_command',command)
    ids=[a['question_revision_id'] for a in command['answers']]
    require(len(ids)==len(set(ids)),'duplicate answer question IDs')
    data={k:copy.deepcopy(v) for k,v in command.items() if k!='command_id' and v is not None}
    data['answers'].sort(key=lambda x:x['question_revision_id'])
    return digest(data)

def validate_feature_schema(obj):
    shape('feature_schema',obj)
    for branch,features in [('static',obj['static']),('aggregate',obj['aggregate']),('temporal',obj['temporal']['features'])]:
        names=[f['name'] for f in features];positions=[f['position'] for f in features]
        require(len(names)==len(set(names)),branch+': duplicate feature name')
        require(positions==list(range(len(features))),branch+': array order must equal contiguous positions')
        for f in features:
            r=f['range']
            if r['kind']=='bounded':require(r.get('min') is not None and r.get('max') is not None and r['min']<=r['max'],'invalid bounded range')
            elif r['kind']=='categorical':require(bool(r.get('vocabulary_ref')) and f['dtype']=='category','categorical vocabulary/dtype required')
            else:require(r.get('min') is None and r.get('max') is None,'unbounded cannot carry bounds')
    if obj['temporal']['padding']!='none':require(obj['temporal']['lengths_required'] and obj['temporal']['mask_required'],'padded temporal inputs require mask and lengths')

def validate_release_manifest(obj):
    shape('content_release_manifest',obj);content=obj['manifest_content'];required=0
    seen=set();resources={r['resource_id']:r for r in content['resources']}
    require(len(resources)==len(content['resources']),'duplicate resource ID')
    unit_ids=[];lesson_ids=[]
    for u in content['units']:
        unit_ids.append(u['unit_id'])
        for lesson in u['lessons']:
            lesson_ids.append(lesson['lesson_id'])
            for a in lesson['activities']:
                require(a['release_activity_id'] not in seen,'duplicate release activity');seen.add(a['release_activity_id'])
                required+=int(a['required_for_completion'])
                require(a['content_resource_id'] in resources,'missing activity content resource')
                require(resources[a['content_resource_id']]['kind']=='json_content','activity resource must be JSON')
                media=a.get('media_resource_ids',[])
                require(len(media)==len(set(media)),'duplicate media reference')
                require(all(i in resources for i in media),'dangling media resource')
                if a['activity_type']=='listening_mcq_v1':require(any(resources[i]['kind']=='audio' for i in media),'listening needs audio')
    require(len(unit_ids)==len(set(unit_ids)) and len(lesson_ids)==len(set(lesson_ids)),'duplicate unit/lesson ID')
    require(required==content['eligible_activity_count'] and required>=1,'eligible activity count mismatch')
    require(digest(content)==obj['release_manifest_sha256'],'JCS manifest hash mismatch')

def activities(release):return [a for u in release['manifest_content']['units'] for l in u['lessons'] for a in l['activities']]
def validate_activity(content,key):
    shape('activity_content',content);shape('scoring_key',key)
    require(content['activity_revision_id']==key['activity_revision_id'],'scoring key activity mismatch')
    questions=content['questions'];ids=[q['question_revision_id'] for q in questions]
    require(len(ids)==len(set(ids)),'duplicate published question')
    keys={k['question_revision_id']:k['correct_option_id'] for k in key['keys']}
    require(len(keys)==len(key['keys']) and set(keys)==set(ids),'scoring key question set mismatch')
    for q in questions:
        options=[o['option_id'] for o in q['options']]
        require(len(options)==len(set(options)),'duplicate option')
        require(keys[q['question_revision_id']] in options,'correct answer not in options')
    if content['activity_type']=='listening_mcq_v1':require(bool(content['media_resource_ids']),'listening missing media')

def score_command(command,content,key):
    command_digest(command);validate_activity(content,key)
    require(command['activity_revision_id']==content['activity_revision_id'],'activity revision mismatch')
    questions={q['question_revision_id']:q for q in content['questions']}
    answers={a['question_revision_id']:a['option_id'] for a in command['answers']}
    require(set(questions)==set(answers),'INVALID_QUESTION_SET')
    for q,a in answers.items():require(a in {o['option_id'] for o in questions[q]['options']},'INVALID_OPTION')
    keys={k['question_revision_id']:k['correct_option_id'] for k in key['keys']}
    raw=sum(answers[q]==keys[q] for q in answers);maximum=len(questions)
    return {'raw_score':raw,'max_score':maximum,'score_fraction':raw/maximum}

def validate_progress(progress):
    shape('progress',progress)
    require(progress['completed_required_credit_count']<=progress['eligible_activity_count'],'progress overcount')
    require(near(progress['completion_fraction'],progress['completed_required_credit_count']/progress['eligible_activity_count']),'progress fraction mismatch')

def validate_receipt(receipt,command=None):
    shape('command_receipt',receipt)
    if command is not None:
        require(receipt['command_id']==command['command_id'],'receipt command mismatch')
        require(receipt['payload_digest']==command_digest(command),'receipt digest mismatch')
    if receipt['terminal_outcome']=='rejected':
        require(receipt['reason_code'] in load('contracts/reason_code_catalog_v1.json')['business_rejections'],'unknown business rejection');return
    result=receipt['canonical_result'];s=result['score'];validate_progress(result['progress_after_command'])
    require(s['raw_score']<=s['max_score'] and near(s['score_fraction'],s['raw_score']/s['max_score']),'invalid score fraction')
    if command:
        require(result['attempt']['attempt_id']==command['attempt_id'],'receipt attempt mismatch')
        require(result['progress_after_command']['enrollment_id']==command['enrollment_id'],'receipt enrollment mismatch')

def validate_sync(result):
    shape('command_sync_result',result);receipt=result.get('receipt')
    if receipt:
        validate_receipt(receipt);require(result['command_id']==receipt['command_id'],'nested command ID mismatch')
        if receipt['terminal_outcome']=='accepted':
            old=receipt['canonical_result']['progress_after_command'];cur=result['current_canonical_state']['progress'];validate_progress(cur)
            require((old['enrollment_id'],old['course_release_id'])==(cur['enrollment_id'],cur['course_release_id']),'reconciliation scope mismatch')
            require(cur['progress_revision']>=old['progress_revision'],'server current revision older than receipt')
            if cur['progress_revision']==old['progress_revision']:require(cur==old,'equal revisions disagree')
        else:require(result['reason_code']==receipt['reason_code'],'rejection reason mismatch')

def validate_grant(grant):
    shape('offline_download_grant',grant)
    require(instant(grant['issued_at'])<instant(grant['learn_until'])<instant(grant['upload_until']),'grant deadlines out of order')
    if grant.get('revoked_at'):require(instant(grant['revoked_at'])>=instant(grant['issued_at']),'grant revoked before issue')

def validate_offline(command,grant,release,status,learner_id,received_at,installation_id):
    shape('submit_attempt_command',command);validate_grant(grant);validate_release_manifest(release);shape('release_access_status',status)
    require(command['submission_mode']=='offline','not an offline command')
    require(grant['learner_id']==learner_id and grant['enrollment_id']==command['enrollment_id'],'scope denied')
    require(command['offline_grant_id']==grant['grant_id'] and command['package_id']==grant['package_id'],'grant/package mismatch')
    require(command['device_installation_id']==installation_id==grant['device_installation_id'],'installation mismatch')
    require(grant['course_release_id']==release['course_release_id']==status['course_release_id'],'release mismatch')
    require(grant['release_manifest_sha256']==release['release_manifest_sha256'],'grant manifest mismatch')
    require(any(a['release_activity_id']==command['release_activity_id'] and a['activity_revision_id']==command['activity_revision_id'] for a in activities(release)),'CONTENT_NOT_IN_ENROLLMENT_RELEASE')
    received=instant(received_at);require(received>=instant(grant['issued_at']),'OFFLINE_GRANT_INVALID')
    require(instant(status['effective_at'])<=received,'future access status is not current')
    require(status['status']!='hard_revoked','CONTENT_HARD_REVOKED')
    require(not grant.get('revoked_at') or instant(grant['revoked_at'])>received,'OFFLINE_GRANT_REVOKED')
    require(received<=instant(grant['upload_until']),'OFFLINE_UPLOAD_WINDOW_EXPIRED')
    if status['status']=='soft_revoked':require(instant(grant['issued_at'])<instant(status['effective_at']),'OFFLINE_GRANT_INVALID')

def safe_artifact(ref):
    p=(ROOT/ref).resolve();require(p.is_relative_to(ROOT.resolve()) and p.is_file(),'artifact missing or outside package: '+ref);return p

def validate_source_capture(capture,evidence):
    shape('source_capture',capture)
    expected=digest({k:v for k,v in capture.items() if k!='manifest_sha256'})
    require(expected==capture['manifest_sha256'],'source capture hash mismatch')
    require(digest(evidence)==capture['evidence_manifest']['sha256'],'evidence manifest hash mismatch')
    require(len(evidence['publications'])==capture['source_count'],'source count mismatch')
    ids=[]
    for e in evidence['publications']:
        shape('evidence_publication',e);ids.append(e['evidence_publication_id'])
        require(e['learner_id']==capture['learner_id'] and e.get('enrollment_id') in [None,capture['enrollment_id']],'capture owner mismatch')
        require(instant(e['published_available_at'])<=instant(capture['knowledge_cutoff_at']),'future knowledge in capture')
        if e.get('source_occurred_at'):require(instant(e['source_occurred_at'])<=instant(capture['event_cutoff_at']),'future occurrence in capture')
    require(len(ids)==len(set(ids)),'duplicate captured publication')
    for e in evidence['publications']:
        raw=evidence.get('immutable_payloads',{}).get(e['evidence_publication_id'])
        require(raw is not None and digest(raw)==e['payload_sha256'],'missing/incorrect captured immutable payload')
    if capture['serving_mode']=='serving':
        require(instant(capture['knowledge_cutoff_at'])==instant(capture['capture_started_at']),'new serving capture must use actual read-view cutoff')
    require(set(capture['state_evidence_publication_ids'])<=set(ids),'uncaptured mutable state revision')
    require(instant(capture['knowledge_cutoff_at'])<=instant(capture['capture_started_at'])<=instant(capture['generated_at']),'capture time order')
    # Membership was recorded by the original snapshot transaction. This check
    # cannot manufacture MVCC visibility by evaluating wall-clock timestamps.

def validate_snapshot(snapshot,capture,feature,payload):
    shape('feature_snapshot',snapshot);validate_feature_schema(feature)
    require(snapshot['source_capture_id']==capture['source_capture_id'],'snapshot capture ID mismatch')
    require(snapshot['source_capture_sha256']==capture['manifest_sha256'],'snapshot capture hash mismatch')
    for k in ['learner_id','enrollment_id','serving_mode','event_cutoff_at','knowledge_cutoff_at','source_revision']:
        require(snapshot[k]==capture[k],'snapshot/capture mismatch: '+k)
    require(snapshot['feature_schema_version']==feature['feature_schema_version'] and snapshot['feature_schema_sha256']==digest(feature),'feature schema hash mismatch')
    require(snapshot['payload_sha256']==digest(payload),'feature payload hash mismatch')
    require(instant(capture['generated_at'])<=instant(snapshot['generated_at']),'snapshot predates capture')
    require(len(payload['static'])==len(feature['static']) and len(payload['aggregate'])==len(feature['aggregate']),'feature dimension mismatch')
    require(all(len(row)==len(feature['temporal']['features']) for row in payload['temporal']),'temporal dimension mismatch')
    require(0<=payload['length']<=len(payload['temporal']) and len(payload['mask'])==len(payload['temporal']),'temporal mask/length mismatch')
    require(all(isinstance(x,bool) for x in payload['mask']) and sum(payload['mask'])==payload['length'],'mask sum/type mismatch')
    length=payload['length'];mask=payload['mask'];padding=feature['temporal']['padding']
    if padding=='right_zero':require(mask==[True]*length+[False]*(len(mask)-length),'right padding mask order')
    if padding=='left_zero':require(mask==[False]*(len(mask)-length)+[True]*length,'left padding mask order')
    if padding=='none':require(length==len(mask) and all(mask),'unpadded mask mismatch')
    def values(vals,definitions):
        for value,f in zip(vals,definitions):
            if f['dtype']=='bool':require(isinstance(value,bool),'bool feature type mismatch')
            elif f['dtype']=='category':require(isinstance(value,(str,int)) and not isinstance(value,bool),'category feature type mismatch')
            else:
                require(isinstance(value,(int,float)) and not isinstance(value,bool) and math.isfinite(value),'numeric feature type/finite mismatch')
                if f['dtype'] in ('int32','int64'):require(isinstance(value,int),'integer feature type mismatch')
                r=f['range']
                if r['kind']=='bounded':require(r['min']<=value<=r['max'],'feature value outside range')
    values(payload['static'],feature['static']);values(payload['aggregate'],feature['aggregate'])
    for row,valid in zip(payload['temporal'],mask):
        if valid:values(row,feature['temporal']['features'])
        else:require(all(x==0 for x in row),'nonzero padded temporal row')

def validate_bundle_release_gate(bundle,registry=None):
    shape('model_bundle',bundle)
    if bundle['release_status']=='candidate' or bundle['release_status']=='retired':return
    require(not re.search(r'tbd|placeholder|example|fixture|to_be|candidate',bundle['target_version']+' '+bundle['horizon_version'],re.I),'unresolved target/horizon')
    rt=bundle['runtime'];require(re.fullmatch(r'\d+\.\d+\.\d+',rt['python']) and re.fullmatch(r'\d+\.\d+\.\d+(?:\+[A-Za-z0-9.]+)?',rt['framework_version']),'runtime must pin exact versions')
    require(registry is not None,'promotion requires trusted artifact registry and validation evidence')
    hashes={'model':bundle['model_artifact_sha256'],'preprocessing':bundle['preprocessing_artifact_sha256'],'feature_schema':bundle['feature_schema_sha256'],'validation':bundle['validation_record']['sha256']}
    for kind,ref in bundle['artifact_refs'].items():
        entry=registry.get(ref);require(entry is not None and entry['kind']==kind and not entry.get('fixture_only',True),'unresolved/fixture artifact: '+kind)
        path=safe_artifact(entry['path']);actual=digest(strict_json(path.read_text())) if entry['encoding']=='jcs_json' else file_hash(path)
        require(actual==entry['sha256'],'registry artifact content hash mismatch')
        if kind in hashes:require(actual==hashes[kind],'bundle artifact hash mismatch: '+kind)
    validation=load(registry[bundle['artifact_refs']['validation']]['path'])
    require(validation.get('deployment_eligible') is True and bundle['release_status'] in validation.get('approved_stages',[]),'release stage not approved')
    require(validation.get('model_artifact_sha256')==bundle['model_artifact_sha256'] and validation.get('feature_schema_sha256')==bundle['feature_schema_sha256'],'validation belongs to different model/schema')
    target=load(registry[bundle['artifact_refs']['target']]['path']);horizon=load(registry[bundle['artifact_refs']['horizon']]['path'])
    require(target.get('version')==bundle['target_version'] and horizon.get('version')==bundle['horizon_version'],'target/horizon registry mismatch')
    require(target.get('ready_for_training') is True and horizon.get('ready_for_training') is True,'target/horizon gate incomplete')

def validate_prediction_bundle(pred,bundle,snapshot=None):
    shape('prediction',pred);shape('model_bundle',bundle)
    if pred['status']!='available':return
    require(pred['model_bundle_id']==bundle['bundle_id'] and pred['model_bundle_sha256']==digest(bundle),'prediction bundle identity/hash mismatch')
    require(pred['target_version']==bundle['target_version'] and pred['horizon_version']==bundle['horizon_version'],'prediction target/horizon mismatch')
    require(pred['threshold_value']==bundle['threshold']['value'] and pred['threshold_version']==bundle['threshold']['version'],'threshold mismatch')
    require(pred['label']==(pred['probability']>=pred['threshold_value']),'prediction label mismatch')
    require(near(pred['margin'],abs(pred['probability']-pred['threshold_value'])),'prediction margin mismatch')
    require(pred['uncertainty_method']==bundle['uncertainty']['method'] and pred['uncertainty_version']==bundle['uncertainty']['version'],'uncertainty identity mismatch')
    cal=bundle.get('calibration');require(pred.get('calibration_version')==(cal['version'] if cal else None),'calibration mismatch')
    if pred['uncertainty_method']=='binary_entropy':
        p=pred['probability'];u=0 if p in (0,1) else -(p*math.log2(p)+(1-p)*math.log2(1-p))
        require(near(pred['uncertainty_value'],u,1e-4),'binary entropy mismatch')
    if snapshot:
        require(pred['feature_snapshot_id']==snapshot['feature_snapshot_id'],'prediction snapshot mismatch')
        for k in ['feature_schema_version','feature_schema_sha256','preprocessing_artifact_sha256']:require(bundle[k]==snapshot[k],'snapshot/bundle mismatch: '+k)
        require(instant(pred['generated_at'])>=instant(snapshot['generated_at']),'prediction predates features')
        require(pred['as_of_at']==snapshot['as_of_at'],'prediction as-of mismatch')
    if pred.get('expires_at'):require(instant(pred['expires_at'])>=instant(pred['generated_at']),'prediction expiry precedes generation')

def validate_event(event):
    shape('client_event',event)
    entries=load('contracts/event_catalog_v1.json')['events'];entry=next((e for e in entries if e['name']==event['event_name'] and e['version']==event['event_version']),None)
    require(entry is not None,'unknown event/version');shape(entry['payload_schema'].removeprefix('schemas/'),event['payload'])
    require(all(event['context'].get(k) for k in entry['required_context']),'required event context missing')
    for k in ['decision_id','media_resource_id']:
        if k in event['payload']:require(event['context'].get(k)==event['payload'][k],'payload/context mismatch')
    require(len(rfc8785.dumps(event['payload']))<=entry['max_payload_bytes'],'event payload too large')

def validate_recommendation(obj):
    shape('recommendation_decision',obj);require(instant(obj['valid_from'])<instant(obj['valid_until']),'recommendation window invalid')

def validate_outcome(obj):
    shape('outcome_observation',obj);require(instant(obj['window_start'])<instant(obj['window_end']),'outcome window invalid')
    if obj['status']=='observed':require(instant(obj['observed_at'])>=instant(obj['window_end']),'outcome not mature')

def main():
    # Full runner includes positive/negative fixtures and validates external refs.
    import run_checks
    run_checks.main()
if __name__=='__main__':main()
