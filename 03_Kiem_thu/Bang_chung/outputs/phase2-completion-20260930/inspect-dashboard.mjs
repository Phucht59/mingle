import fs from 'node:fs/promises';
import { FileBlob, SpreadsheetFile } from '@oai/artifact-tool';
const source='C:/Mingo/06_quality/phase2/final_gate/2026-09-30/inputs/Mingo_Phase2_R1_Independent_QA_Control_2026-09-29.xlsx';
const wb=await SpreadsheetFile.importXlsx(await FileBlob.load(source));
console.log((await wb.inspect({kind:'table',range:'00_Dashboard!A1:J24',include:'values,formulas',tableMaxRows:24,tableMaxCols:10,maxChars:10000})).ndjson);
console.log((await wb.inspect({kind:'table',range:'04_QA_Test_Cases!A1:L7',include:'values,formulas',tableMaxRows:7,tableMaxCols:12,maxChars:4500})).ndjson);
const preview=await wb.render({sheetName:'00_Dashboard',range:'D4:E11',scale:1,format:'png'});
await fs.writeFile('C:/Mingo/outputs/phase2-completion-20260930/dashboard-before.png',new Uint8Array(await preview.arrayBuffer()));
