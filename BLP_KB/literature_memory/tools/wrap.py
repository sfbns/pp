import sys, os, textwrap
src, dst = sys.argv[1], sys.argv[2]
for fn in sorted(os.listdir(src)):
    if not fn.endswith('.txt'): continue
    out=[]
    for line in open(os.path.join(src,fn),encoding='utf-8').read().split('\n'):
        if len(line)<=900: out.append(line)
        else:
            out.extend(textwrap.wrap(line,width=900,break_long_words=True,break_on_hyphens=False,replace_whitespace=False,drop_whitespace=False) or [''])
    open(os.path.join(dst,fn),'w',encoding='utf-8').write('\n'.join(out))
    print(fn,len(out))
