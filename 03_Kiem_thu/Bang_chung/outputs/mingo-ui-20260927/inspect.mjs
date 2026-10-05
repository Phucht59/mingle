import fs from 'node:fs/promises';
import { FileBlob, SpreadsheetFile } from '@oai/artifact-tool';
const w=await SpreadsheetFile.importXlsx(await FileBlob.load('C:/Mingo/Manage Project.xlsx'));
console.log((await w.inspect({kind:'workbook,sheet,table',maxChars:6500,tableMaxRows:2,tableMaxCols:6})).ndjson);
await fs.writeFile('before.png',new Uint8Array(await (await w.render({sheetName:'01_TONG_QUAN',range:'A1:G22',scale:1})).arrayBuffer()));
const d=JSON.parse(await fs.readFile('source.json','utf8'));
for(const s of d.slice(3)) console.log(JSON.stringify({name:s.name,data:s.data}));
