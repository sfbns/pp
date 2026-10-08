import sys, zipfile, re, os
zp, out = sys.argv[1], sys.argv[2]
def dec(n):
    return re.sub(r'#U([0-9a-fA-F]{4})', lambda m: chr(int(m.group(1),16)), n)
with zipfile.ZipFile(zp) as z:
    for info in z.infolist():
        name = info.filename
        if not (info.flag_bits & 0x800):
            try: name = name.encode('cp437').decode('utf-8')
            except Exception: pass
        name = dec(name)
        if name.endswith('/'): continue
        dest = os.path.join(out, name)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with z.open(info) as src, open(dest,'wb') as f: f.write(src.read())
        print(dest)
