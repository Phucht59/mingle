from pathlib import Path
import pypdfium2 as pdf
root=Path('C:/Mingo/outputs/mingo-ui-20260927')
for f in root.glob('*-native.pdf'):
 with pdf.PdfDocument(f) as d:
  page=d[0]
  image=page.render(scale=1.6).to_pil()
  image.save(f.with_suffix('.png'))
  page.close()
 print(f.stem)
