# usage: python3 -I numcheck.py card.md source.txt [source2 ...]
# Lists numeric tokens in the card that cannot be found in the source text(s).
import sys, re
card = open(sys.argv[1], encoding='utf-8').read()
src = ''
for p in sys.argv[2:]:
    src += open(p, encoding='utf-8').read()
def norm(s):
    s = s.replace('−', '-').replace('–', '-').replace(',', '').replace('，','')
    return re.sub(r'\s+', '', s)
S = norm(src)
# drop LaTeX blocks and code spans from card to reduce noise
c = re.sub(r'\$\$.*?\$\$', ' ', card, flags=re.S)
c = re.sub(r'`[^`]*`', ' ', c)
toks = re.findall(r'(?<![\w.])[-−]?\d[\d,]*\.\d+|(?<![\w.])\d{1,3}(?:,\d{3})+(?![\d])|(?<![\w.])\d{3,}(?![\d.])', c)
miss, seen = [], set()
for t in toks:
    n = norm(t).lstrip('-')
    if n in seen: continue
    seen.add(n)
    if re.fullmatch(r'(19|20)\d\d', n): continue
    if n not in S:
        # try trailing-zero variants
        alt = n.rstrip('0').rstrip('.') if '.' in n else n
        if alt and alt in S: continue
        miss.append(t)
print('numbers checked:', len(seen), '| not found in source:', len(miss))
print(' '.join(miss))
