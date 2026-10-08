# usage: python3 finalize.py ID "index row" ; run from repo root
import sys, re
ID, row = sys.argv[1], sys.argv[2]
p='literature_memory/00_记忆映射_INDEX.md'
s=open(p,encoding='utf-8').read()
if f'| {ID} |' not in s:
    if not s.endswith('\n'): s+='\n'
    s+=row.strip()+'\n'
    open(p,'w',encoding='utf-8').write(s)
p='literature_memory/00_PROGRESS_断点续联.md'
s=open(p,encoding='utf-8').read()
s2=re.sub(r'\[ \] '+re.escape(ID)+r'(?=[ _])', '[x] '+ID, s, count=1)
open(p,'w',encoding='utf-8').write(s2)
print('ticked' if s2!=s else 'NOT ticked (check id)')
