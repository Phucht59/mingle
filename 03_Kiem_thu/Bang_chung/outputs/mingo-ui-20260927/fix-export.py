from pathlib import Path
import zipfile,re,os
p=Path('C:/Mingo/outputs/mingo-ui-20260927/Manage Project - Redesigned.xlsx')
with zipfile.ZipFile(p) as z: parts={n:z.read(n) for n in z.namelist()}
key='xl/worksheets/sheet1.xml'
xml=parts[key].decode('utf-8')
def fix(m):
 text=m.group(0)
 if 'HYPERLINK is not implemented.' not in text:return text
 # Artifact Tool cannot evaluate HYPERLINK. Excel evaluates the retained formula;
 # an absent cache is valid, whereas its diagnostic is not a valid Excel error.
 return re.sub(r'<v>.*?</v>','',text.replace(' t="e"',''))
xml=re.sub(r'<c\b[^>]*>.*?</c>',fix,xml,flags=re.S)
parts[key]=xml.encode('utf-8')
temp=p.with_suffix('.tmp')
with zipfile.ZipFile(temp,'w',zipfile.ZIP_DEFLATED) as z:
 for n,b in parts.items():z.writestr(n,b)
os.replace(temp,p)
print('Removed unsupported HYPERLINK diagnostic caches; formulas retained.')
