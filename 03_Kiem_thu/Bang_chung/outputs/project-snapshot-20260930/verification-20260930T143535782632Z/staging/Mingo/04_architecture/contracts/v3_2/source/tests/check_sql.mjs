// Embedded PostgreSQL constraint/rollback checks. Not multi-connection testing.
import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const {PGlite}=await import(process.env.PGLITE_MODULE || '@electric-sql/pglite');
const db=new PGlite();const checks=[];
const id=n=>`10000000-0000-4000-8000-${String(n).padStart(12,'0')}`;
const q=(text,params=[])=>db.query(text,params);
const eq=(a,b)=>{if(a!==b)throw new Error(`${a} != ${b}`);};
async function test(name,fn){try{await fn();checks.push({name,status:'PASS'});}catch(e){checks.push({name,status:'FAIL',message:e.message});}}
async function reject(sql,params=[],code='23503'){let threw=false;try{await q(sql,params);}catch(e){threw=true;eq(e.code,code);}if(!threw)throw new Error('invalid SQL mutation accepted');}
const ddl=await fs.readFile(path.join(root,'contracts/core_ddl_postgresql.sql'),'utf8');
await test('DDL executes in PostgreSQL WASM',()=>db.exec(ddl));
if(checks.some(c=>c.status==='FAIL')){console.log(checks);process.exit(1);}
await db.exec(`
 INSERT INTO learner VALUES ('${id(1)}'),('${id(101)}');
 INSERT INTO course_release VALUES ('${id(4)}','${'a'.repeat(64)}',1),('${id(104)}','${'b'.repeat(64)}',1);
 INSERT INTO enrollment VALUES ('${id(2)}','${id(1)}','${id(4)}'),('${id(102)}','${id(101)}','${id(104)}');
 INSERT INTO activity_revision VALUES ('${id(11)}','${id(14)}',2),('${id(111)}','${id(114)}',2);
 INSERT INTO release_activity VALUES ('${id(9)}','${id(4)}','${id(11)}',true),('${id(109)}','${id(104)}','${id(111)}',true),('${id(209)}','${id(4)}','${id(11)}',false);
 INSERT INTO question_option VALUES ('${id(11)}','${id(12)}','A',false),('${id(11)}','${id(12)}','B',true),('${id(11)}','${id(13)}','A',true),('${id(11)}','${id(13)}','B',false);
 INSERT INTO progress_state(enrollment_id,learner_id,course_release_id,progress_revision,completed_required_credit_count,eligible_activity_count,updated_at)
 VALUES ('${id(2)}','${id(1)}','${id(4)}',0,0,1,now()),('${id(102)}','${id(101)}','${id(104)}',0,0,1,now());
`);
const baseReceipt=JSON.parse(await fs.readFile(path.join(root,'examples/command_receipt.accepted.example.json')));
async function submit({attempt=18,receipt=19,command=17,ra=9,credit=true,wrongScore=false,missingAnswer=false,outbox=true}={}){
 const result=structuredClone(baseReceipt.canonical_result);result.attempt.attempt_id=id(attempt);result.completion_credit_created=credit;
 await q('INSERT INTO command_receipt VALUES ($1,$2,$3,$4,$5,$6,$7,NULL,now(),$8)',[id(receipt),id(1),id(command),'submit_attempt_v1','command_digest_v1','a'.repeat(64),'accepted',result]);
 await q('INSERT INTO attempt VALUES ($1,$2,$3,$4,$5,$6,$7,$8,1,now(),now())',[id(attempt),id(1),id(2),id(4),id(ra),id(11),id(receipt),'finalized']);
 await q('INSERT INTO answer_submission VALUES ($1,$2,$3,$4)',[id(attempt),id(11),id(12),'B']);
 if(!missingAnswer)await q('INSERT INTO answer_submission VALUES ($1,$2,$3,$4)',[id(attempt),id(11),id(13),'A']);
 await q('INSERT INTO scoring_record(scoring_record_id,attempt_id,activity_revision_id,scoring_record_revision,scoring_version_id,raw_score,max_score,recorded_at) VALUES ($1,$2,$3,1,$4,$5,2,now())',[id(receipt+1000),id(attempt),id(11),id(14),wrongScore?1:2]);
 if(credit){await q('INSERT INTO completion_credit VALUES ($1,$2,$3,$4,true,$5,now()) ON CONFLICT(enrollment_id,release_activity_id) DO NOTHING',[id(receipt+2000),id(2),id(ra),id(4),id(attempt)]);await q('UPDATE progress_state SET completed_required_credit_count=1,progress_revision=1 WHERE enrollment_id=$1',[id(2)]);}
 if(outbox)await q('INSERT INTO outbox_message VALUES ($1,$2,$3,$4,$5,$6,now())',[id(receipt+3000),id(receipt),'attempt_finalized','attempt',id(attempt),{}]);
}
async function txRejected(fn,code){await q('BEGIN');let error;try{await fn();await q('COMMIT');}catch(e){error=e;await q('ROLLBACK');}if(!error)throw new Error('invalid transaction committed');if(code)eq(error.code,code);}
await test('valid attempt/answers/score/credit/receipt/outbox commits atomically',async()=>{await q('BEGIN');await submit();await q('COMMIT');eq((await q('SELECT count(*)::int n FROM attempt')).rows[0].n,1);});
await test('wrong enrollment owner rejected',()=>reject('INSERT INTO attempt VALUES ($1,$2,$3,$4,$5,$6,$7,$8,1,now(),now())',[id(90),id(101),id(2),id(4),id(9),id(11),id(999),'finalized']));
await test('activity from another release rejected',()=>reject('INSERT INTO attempt VALUES ($1,$2,$3,$4,$5,$6,$7,$8,1,now(),now())',[id(90),id(1),id(2),id(4),id(109),id(111),id(999),'finalized']));
await test('duplicate command receipt rejected',()=>reject('INSERT INTO command_receipt VALUES ($1,$2,$3,$4,$5,$6,$7,$8,now(),NULL)',[id(90),id(1),id(17),'submit_attempt_v1','command_digest_v1','a'.repeat(64),'rejected','INVALID_OPTION'],'23505'));
await test('accepted receipt without attempt cannot commit',()=>txRejected(()=>q('INSERT INTO command_receipt VALUES ($1,$2,$3,$4,$5,$6,$7,NULL,now(),$8)',[id(90),id(1),id(91),'submit_attempt_v1','command_digest_v1','a'.repeat(64),'accepted',{}]),'23514'));
await test('wrong computed score cannot commit',()=>txRejected(()=>submit({attempt:92,receipt:93,command:94,credit:false,wrongScore:true}),'23514'));
await test('incomplete question set cannot commit',()=>txRejected(()=>submit({attempt:92,receipt:93,command:94,credit:false,missingAnswer:true}),'23514'));
await test('missing outbox cannot commit',()=>txRejected(()=>submit({attempt:92,receipt:93,command:94,credit:false,outbox:false}),'23514'));
await test('rollback leaves no partial attempt after deferred failure',async()=>eq((await q('SELECT count(*)::int n FROM attempt WHERE attempt_id=$1',[id(92)])).rows[0].n,0));
await test('invalid option blocked by foreign key',()=>reject('INSERT INTO answer_submission VALUES ($1,$2,$3,$4)',[id(18),id(11),id(99),'Z']));
await test('repeat attempt retains one completion credit',async()=>{await q('BEGIN');await submit({attempt:92,receipt:93,command:94,credit:false});await q('COMMIT');eq((await q('SELECT count(*)::int n FROM attempt')).rows[0].n,2);eq((await q('SELECT count(*)::int n FROM completion_credit')).rows[0].n,1);});
await test('optional activity score creates no credit',async()=>{await q('BEGIN');await submit({attempt:192,receipt:193,command:194,ra:209,credit:false});await q('COMMIT');eq((await q('SELECT count(*)::int n FROM completion_credit')).rows[0].n,1);});
await test('optional activity cannot receive required completion credit',()=>reject('INSERT INTO completion_credit VALUES ($1,$2,$3,$4,true,$5,now())',[id(295),id(2),id(209),id(4),id(192)]));
await test('credit bound to actual enrollment/activity of first attempt',()=>reject('INSERT INTO completion_credit VALUES ($1,$2,$3,$4,true,$5,now())',[id(295),id(102),id(109),id(104),id(18)]));
await test('canonical progress cannot drift from completion credits',()=>txRejected(()=>q('UPDATE progress_state SET completed_required_credit_count=0 WHERE enrollment_id=$1',[id(2)]),'23514'));
await test('attempt history cannot be overwritten',()=>reject('UPDATE attempt SET occurred_at=now() WHERE attempt_id=$1',[id(18)],'23514'));
await test('receipt history cannot be overwritten',()=>reject('UPDATE command_receipt SET payload_digest=$1 WHERE receipt_id=$2',['b'.repeat(64),id(19)],'23514'));
await test('scoring history cannot be overwritten',()=>reject('UPDATE scoring_record SET raw_score=0 WHERE attempt_id=$1',[id(18)],'23514'));
await test('job logical effect uniqueness includes timer jobs without outbox',async()=>{
 const sql='INSERT INTO durable_job VALUES ($1,NULL,$2,$3,$4,$5,NULL,0,NULL,now(),0,8,NULL,now(),now())';
 await q(sql,[id(500),'summary','v1','effect1','pending']);await reject(sql,[id(501),'summary','v1','effect1','pending'],'23505');
});
await test('stale worker generation cannot complete reacquired job',async()=>{
 await q("UPDATE durable_job SET status='leased',lease_owner='B',lease_generation=2,lease_until=now()+interval '1 minute' WHERE job_id=$1",[id(500)]);
 const r=await q("UPDATE durable_job SET status='completed' WHERE job_id=$1 AND lease_owner='A' AND lease_generation=1 AND status='leased' AND lease_until>clock_timestamp() RETURNING job_id",[id(500)]);eq(r.rows.length,0);
});
await test('exposure cannot target another learner decision',async()=>{await q('INSERT INTO recommendation_decision_identity VALUES ($1,$2)',[id(600),id(1)]);await reject('INSERT INTO recommendation_exposure VALUES ($1,$2,$3,now(),$4)',[id(601),id(101),id(600),'home']);});
const report={engine:'PGlite PostgreSQL WASM',engine_version:(await q('SELECT version()')).rows[0].version,passed:checks.filter(c=>c.status==='PASS').length,failed:checks.filter(c=>c.status==='FAIL').length,checks,not_validated:['native PostgreSQL multi-connection concurrency','FastAPI command handler','JWT/RLS','production migrations and restore']};
await fs.writeFile(path.join(root,'SQL_VALIDATION_REPORT.json'),JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify(report,null,2));await db.close();if(report.failed)process.exitCode=1;
