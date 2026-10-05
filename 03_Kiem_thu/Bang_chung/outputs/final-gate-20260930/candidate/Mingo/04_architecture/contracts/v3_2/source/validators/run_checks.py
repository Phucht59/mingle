"""Run: python validators/run_checks.py. Nonzero exit means failed validation."""
import copy,json,math,re,sys
from pathlib import Path
import yaml
from openapi_spec_validator import OpenAPIV31SpecValidator
from pglast import parse_sql
import validate_contracts as v

def main():
    lines=[];failures=[]
    def check(name,fn):
        try:fn();lines.append('PASS '+name)
        except Exception as e:failures.append(name);lines.append('FAIL '+name+': '+str(e))
    def rejected(fn):
        try:fn()
        except ValueError:return
        raise AssertionError('invalid value was accepted')
    def same(a,b):
        if a!=b:raise AssertionError(f'{a!r} != {b!r}')
    def modified(x,**kw):y=copy.deepcopy(x);y.update(kw);return y
    for key in v.SCHEMAS:check('meta-schema '+key,lambda k=key:v.Draft202012Validator.check_schema(v.SCHEMAS[k]))
    bindings=v.load('tests/example_schema_bindings.json')
    for name,schema in bindings.items():check('example '+name,lambda n=name,s=schema:v.shape(s,v.load('examples/'+n+'.example.json')))
    example=lambda n:v.load('examples/'+n+'.example.json')
    command=example('submit_attempt_command');release=example('content_release_manifest');grant=example('offline_download_grant');status=example('release_access_status');content=v.load('artifacts/activity_content.json');key=v.load('artifacts/server_only/scoring_key.json');receipt=example('command_receipt.accepted');sync=example('command_sync_result.duplicate');feature=example('feature_schema');snapshot=example('feature_snapshot');capture=example('source_capture');evidence=v.load('artifacts/evidence_manifest.json');bundle=example('model_bundle');prediction=example('prediction.available');payload=v.load('artifacts/feature_payload.json')
    check('release semantic/JCS/resource graph',lambda:v.validate_release_manifest(release))
    check('activity/questions/server scoring key',lambda:v.validate_activity(content,key))
    check('score exact command',lambda:same(v.score_command(command,content,key),{'raw_score':2,'max_score':2,'score_fraction':1.0}))
    check('receipt/digest/state cross-links',lambda:v.validate_receipt(receipt,command))
    check('accepted duplicate semantics',lambda:v.validate_sync(sync))
    check('rejected duplicate semantics',lambda:v.validate_sync(example('command_sync_result.duplicate_rejected')))
    check('retryable unknown commit semantics',lambda:v.validate_sync(example('command_sync_result.retryable')))
    check('grant deadlines',lambda:v.validate_grant(grant))
    offline=lambda c=command,g=grant,s=status,at='2026-09-16T09:01:00Z':v.validate_offline(c,g,release,s,g['learner_id'],at,'android-install-abc')
    check('offline published valid',offline)
    check('offline exact upload boundary',lambda:offline(at=grant['upload_until']))
    check('source capture membership/hash',lambda:v.validate_source_capture(capture,evidence))
    check('feature schema order/range',lambda:v.validate_feature_schema(feature))
    check('snapshot lineage/dimensions/hashes',lambda:v.validate_snapshot(snapshot,capture,feature,payload))
    check('prediction model snapshot numeric consistency',lambda:v.validate_prediction_bundle(prediction,bundle,snapshot))
    check('candidate fixture allowed as fixture',lambda:v.validate_bundle_release_gate(bundle))
    check('recommendation rule has audit/window',lambda:v.validate_recommendation(example('recommendation_decision.rule')))
    check('JCS numeric equivalence',lambda:same(v.digest({'a':1.0}),v.digest({'a':1})))
    check('JCS negative zero equivalence',lambda:same(v.digest({'a':-0.0}),v.digest({'a':0})))
    check('JCS unicode reference ordering',lambda:same(v.rfc8785.dumps({'\ue000':1,'\U0001f600':2}),'{"😀":2,"":1}'.encode()))
    reordered=copy.deepcopy(command);reordered['answers'].reverse();reordered.pop('expected_state_version')
    check('command answer order/null normalization',lambda:same(v.command_digest(command),v.command_digest(reordered)))
    check('changed answer changes digest',lambda:v.require(v.command_digest(modified(command,answers=[dict(command['answers'][0],option_id='A'),command['answers'][1]]))!=v.command_digest(command),'same digest'))
    # Negative checks assert rejection, not merely execution of validation functions.
    cases={
      'duplicate raw JSON keys':lambda:v.strict_json('{"a":1,"a":2}'),
      'NaN JSON':lambda:v.strict_json('{"x":NaN}'),
      'non-null expected progress version':lambda:v.command_digest(modified(command,expected_state_version=1)),
      'duplicate answer question':lambda:v.command_digest(modified(command,answers=[command['answers'][0]]*2)),
      'missing question answer':lambda:v.score_command(modified(command,answers=[command['answers'][0]]),content,key),
      'foreign option':lambda:v.score_command(modified(command,answers=[dict(command['answers'][0],option_id='Z'),command['answers'][1]]),content,key),
      'receipt wrong command hash':lambda:v.validate_receipt(modified(receipt,payload_digest='0'*64),command),
      'sync nested command mismatch':lambda:v.validate_sync(modified(sync,command_id='90000000-0000-4000-8000-000000000001')),
      'accepted transport with rejected receipt':lambda:v.validate_sync(modified(sync,delivery_status='accepted',receipt=example('command_receipt.rejected'))),
      'retryable missing retry flag':lambda:v.shape('command_sync_result',{'command_id':command['command_id'],'delivery_status':'retryable','reason_code':'TEMPORARY_UNAVAILABLE'}),
      'offline expired upload':lambda:offline(at='2026-09-24T08:30:01Z'),
      'offline revoked grant':lambda:offline(g=modified(grant,revoked_at='2026-09-16T08:00:00Z')),
      'offline hard revoked release':lambda:offline(s=modified(status,status='hard_revoked')),
      'offline package mismatch':lambda:offline(c=modified(command,package_id='90000000-0000-4000-8000-000000000001')),
      'offline forged grant owner':lambda:v.validate_offline(command,grant,release,status,'90000000-0000-4000-8000-000000000001','2026-09-16T09:01:00Z','android-install-abc'),
      'wrong prediction label':lambda:v.validate_prediction_bundle(modified(prediction,label=False),bundle),
      'wrong prediction hash':lambda:v.validate_prediction_bundle(modified(prediction,model_bundle_sha256='0'*64),bundle),
      'wrong prediction margin':lambda:v.validate_prediction_bundle(modified(prediction,margin=.8),bundle),
      'wrong prediction uncertainty':lambda:v.validate_prediction_bundle(modified(prediction,uncertainty_value=.1),bundle),
      'wrong prediction uncertainty version':lambda:v.validate_prediction_bundle(modified(prediction,uncertainty_version='other'),bundle),
      'wrong prediction horizon':lambda:v.validate_prediction_bundle(modified(prediction,horizon_version='other'),bundle),
      'production fixture gate':lambda:v.validate_bundle_release_gate(modified(bundle,release_status='production'),v.load('artifacts/registry.json')),
      'shadow fixture gate':lambda:v.validate_bundle_release_gate(modified(bundle,release_status='shadow'),v.load('artifacts/registry.json')),
      'production wildcard runtime':lambda:v.validate_bundle_release_gate(modified(bundle,release_status='production',target_version='risk_v1',horizon_version='h_v1',runtime={'python':'3.x','framework':'pytorch','framework_version':'2.x-pinned-at-build'})),
      'production missing trusted registry':lambda:v.validate_bundle_release_gate(modified(bundle,release_status='production',target_version='risk_v1',horizon_version='h_v1')),
      'snapshot wrong capture hash':lambda:v.validate_snapshot(modified(snapshot,source_capture_sha256='0'*64),capture,feature,payload),
      'snapshot wrong payload hash':lambda:v.validate_snapshot(modified(snapshot,payload_sha256='0'*64),capture,feature,payload),
      'snapshot wrong owner':lambda:v.validate_snapshot(modified(snapshot,learner_id='90000000-0000-4000-8000-000000000001'),capture,feature,payload),
      'source capture wrong count':lambda:v.validate_source_capture(modified(capture,source_count=999),evidence),
      'recommendation reversed window':lambda:v.validate_recommendation(modified(example('recommendation_decision.rule'),valid_until='2026-09-01T00:00:00Z')),
    }
    bad=copy.deepcopy(sync);bad['current_canonical_state']['progress']['completion_fraction']=0;cases['inconsistent progress fraction']=lambda:v.validate_sync(bad)
    badscope=copy.deepcopy(sync);badscope['current_canonical_state']['progress']['enrollment_id']='90000000-0000-4000-8000-000000000001';cases['reconciliation wrong enrollment']=lambda:v.validate_sync(badscope)
    badfeature=copy.deepcopy(feature);badfeature['aggregate'].append(copy.deepcopy(badfeature['aggregate'][0]));cases['duplicate feature name/position']=lambda:v.validate_feature_schema(badfeature)
    permuted=copy.deepcopy(feature);f=copy.deepcopy(permuted['aggregate'][0]);f.update(name='other_feature',position=1);permuted['aggregate']=[f,permuted['aggregate'][0]];cases['permuted feature array despite contiguous set']=lambda:v.validate_feature_schema(permuted)
    oldcapture=copy.deepcopy(capture);oldcapture['knowledge_cutoff_at']='2026-09-20T09:59:00Z';oldcapture['manifest_sha256']=v.digest({k:x for k,x in oldcapture.items() if k!='manifest_sha256'})
    cases['new serving capture cannot impersonate older read view']=lambda:v.validate_source_capture(oldcapture,evidence)
    future=copy.deepcopy(evidence);future['publications'][0]['published_available_at']='2026-09-20T10:01:00Z'
    futurecapture=copy.deepcopy(capture);futurecapture['evidence_manifest']['sha256']=v.digest(future);futurecapture['manifest_sha256']=v.digest({k:x for k,x in futurecapture.items() if k!='manifest_sha256'})
    cases['future evidence rejected even with recomputed hashes']=lambda:v.validate_source_capture(futurecapture,future)
    wrongpayload=copy.deepcopy(evidence);wrongpayload['immutable_payloads'][wrongpayload['publications'][0]['evidence_publication_id']]['progress_revision']=999
    payloadcapture=copy.deepcopy(capture);payloadcapture['evidence_manifest']['sha256']=v.digest(wrongpayload);payloadcapture['manifest_sha256']=v.digest({k:x for k,x in payloadcapture.items() if k!='manifest_sha256'})
    cases['captured payload wrong hash rejected']=lambda:v.validate_source_capture(payloadcapture,wrongpayload)
    check('grant timestamps compared as instants not strings',lambda:v.validate_grant(modified(grant,issued_at='2026-09-15T09:00:00+07:00',learn_until='2026-09-15T03:00:00Z',upload_until='2026-09-15T04:00:00Z')))
    for name,fn in cases.items():check('reject '+name,lambda f=fn:rejected(f))
    fixture_bindings={'prediction_available_missing_probability':'prediction','prediction_unavailable_with_probability':'prediction','replayable_snapshot_without_source_capture':'feature_snapshot'}
    for name,schema in fixture_bindings.items():check('reject fixture '+name,lambda n=name,s=schema:rejected(lambda:v.shape(s,v.load('tests/fixtures/invalid/'+n+'.json'))))
    # All content assets are checked by bytes, not by a self-declared hash string.
    resources=release['manifest_content']['resources'];mapping=v.load('artifacts/resource_map.json')
    for resource in resources:
        check('resource bytes '+resource['resource_id'],lambda r=resource:same((v.file_hash(v.safe_artifact(mapping[r['resource_id']])),v.safe_artifact(mapping[r['resource_id']]).stat().st_size),(r['sha256'],r['size_bytes'])))
    check('package detached JCS hash',lambda:same(example('offline_package')['package_sha256'],v.digest({k:x for k,x in example('offline_package').items() if k!='package_sha256'})))
    check('OpenAPI 3.1 full validation and local references',lambda:OpenAPIV31SpecValidator(yaml.safe_load((v.ROOT/'contracts/openapi_vertical_slice_v1.yaml').read_text()),base_uri=(v.ROOT/'contracts/openapi_vertical_slice_v1.yaml').as_uri()).validate())
    check('PostgreSQL DDL parse',lambda:parse_sql((v.ROOT/'contracts/core_ddl_postgresql.sql').read_text()))
    # Catch Python-only regular expressions that fail in a JS consumer.
    patterns=[]
    def walk(x):
        if isinstance(x,dict):
            if 'pattern' in x:patterns.append(x['pattern'])
            for y in x.values():walk(y)
        elif isinstance(x,list):
            for y in x:walk(y)
    for schema in v.SCHEMAS.values():walk(schema)
    check('no Python-only inline flags in schema regex',lambda:v.require(not any('(?i)' in p for p in patterns),'nonportable regex'))
    report={'passed':len(lines)-len(failures),'failed':len(failures),'checks':lines,'not_validated':['Flutter/FastAPI implementation','real PostgreSQL multi-connection concurrency','JWT/RLS production enforcement','trained model validity','load/PITR/restore SLOs']}
    (v.ROOT/'VALIDATION_REPORT.txt').write_text('\n'.join(lines)+f'\nTOTAL passed={report["passed"]} failed={report["failed"]}\nNOT RUN: '+', '.join(report['not_validated'])+'\n')
    (v.ROOT/'validation_results.json').write_text(json.dumps(report,indent=2)+'\n')
    print('\n'.join(line for line in lines if line.startswith('FAIL')))
    print(f'Contract checks: {report["passed"]} passed, {report["failed"]} failed')
    if failures:raise SystemExit(1)
if __name__=='__main__':main()
