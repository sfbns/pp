import sys, os, pypdfium2 as pdfium
pdf = pdfium.PdfDocument(sys.argv[1]); out=sys.argv[2]; os.makedirs(out, exist_ok=True)
pages = range(len(pdf)) if len(sys.argv)<4 else [int(x)-1 for x in sys.argv[3].split(',')]
for i in pages:
    img = pdf[i].render(scale=float(os.environ.get('SC','1.6'))).to_pil()
    img.save(f"{out}/p{i+1:02d}.png")
print(len(pdf))
