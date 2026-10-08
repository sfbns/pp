import sys,re
for p in sys.argv[1:]:
    t=open(p,encoding='utf-8',errors='ignore').read()
    cjk=r'[　-〿一-鿿＀-￯“”‘’（）《》、，。：；！？]'
    for _ in range(3):
        t=re.sub(f'({cjk}) ({cjk})',r'\1\2',t)
    t=re.sub(r'\n[ \t]*\n+','\n',t)
    open(p,'w',encoding='utf-8').write(t)
