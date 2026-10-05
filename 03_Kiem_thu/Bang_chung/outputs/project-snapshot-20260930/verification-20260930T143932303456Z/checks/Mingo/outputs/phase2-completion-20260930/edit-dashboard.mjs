import fs from 'node:fs/promises';
import { FileBlob, SpreadsheetFile } from '@oai/artifact-tool';
const dir='C:/Mingo/outputs/phase2-completion-20260930';
const source='C:/Mingo/06_quality/phase2/final_gate/2026-09-30/inputs/Mingo_Phase2_R1_Independent_QA_Control_2026-09-29.xlsx';
const wb=await SpreadsheetFile.importXlsx(await FileBlob.load(source));
const s=wb.worksheets.getItem('00_Dashboard');
const values={
 A2:'Dashboard correction derivative, 2026-09-30. R1 independent: 94/94 PASS (P0 44/44). Gate HOLD; TalkBack and signoffs pending.',
 B4:'Value', B5:'ACTIVE', B6:'HOLD / NOT PASSED', E4:'Count', I4:'Current result',
 I5:'44/44 PASS',I6:'0 open P0/P1',I7:'100% PASS',I8:'16/16 technical PASS',
 I9:'TalkBack BLOCKED',I10:'Tech Lead PENDING',I11:'Owner PENDING',
 B14:'R1 94/94 PASS; D001-D020 CLOSED. D021 FIX NOW: Windows checks PASS; Linux pending.'
};
const formulas={E5:"=COUNTA('04_QA_Test_Cases'!A5:A250)",E6:"=COUNTIF('04_QA_Test_Cases'!D5:D250,\"P0\")",E7:"=COUNTIF('04_QA_Test_Cases'!K5:K250,\"PASS\")",E8:"=COUNTIF('04_QA_Test_Cases'!K5:K250,\"FAIL\")",B10:'=E5'};
for(const [cell,value] of Object.entries(values))s.getRange(cell).values=[[value]];
for(const [cell,formula] of Object.entries(formulas))s.getRange(cell).formulas=[[formula]];
wb.recalculate();
const edits=Object.fromEntries([...Object.keys(values),...Object.keys(formulas)].map(cell=>[cell,{value:s.getRange(cell).values[0][0],formula:formulas[cell]??null}]));
for(const [cell,expected] of Object.entries({E5:94,E6:44,E7:94,E8:0,B10:94}))if(edits[cell].value!==expected)throw new Error(`${cell}=${edits[cell].value}, expected ${expected}`);
await fs.writeFile(`${dir}/dashboard-edits.json`,JSON.stringify(edits,null,2));
await fs.writeFile(`${dir}/artifact-inspection.ndjson`,(await wb.inspect({kind:'table',range:'00_Dashboard!A4:J15',include:'values,formulas',tableMaxRows:12,tableMaxCols:10,maxChars:7000})).ndjson);
const errors=await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#NUM!|#NULL!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:30},maxChars:3000});
await fs.writeFile(`${dir}/formula-error-scan.ndjson`,errors.ndjson);
await (await SpreadsheetFile.exportXlsx(wb)).save(`${dir}/artifact-working-export.xlsx`);
console.log(JSON.stringify({status:'AUTHORED',cells:Object.keys(edits),totals:[edits.E5.value,edits.E6.value,edits.E7.value],gate:edits.B6.value}));
