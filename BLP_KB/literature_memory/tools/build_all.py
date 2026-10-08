# Regenerate literature_memory/ALL_记忆卡合集_for_Codex.md from the index and all cards.
# usage (from repo root): python3 literature_memory/tools/build_all.py
import os, re, glob
root = 'literature_memory'
order = []
idx = open(os.path.join(root, '00_记忆映射_INDEX.md'), encoding='utf-8').read()
for line in idx.splitlines():
    m = re.match(r'\| ([ACFM]\d+b?) \|', line)
    if m: order.append(m.group(1))
def find(card_id):
    for sub in ('CN_中文与英文PDF', 'BLP_结构模型原文'):
        hits = sorted(glob.glob(os.path.join(root, sub, card_id + '_*.md')))
        if hits: return hits[0]
out = ['# 文献记忆卡合集（供 Codex 导入）', '',
       '> 自动生成：`python3 literature_memory/tools/build_all.py`。内容 = 总目录 + 全部单篇记忆卡（按目录顺序）。单篇卡片是权威版本，修改请改单篇后重新生成。', '',
       '## 总目录', '']
out.append(idx.split('| ID |', 1)[1].join(['| ID |', '']) if False else '| ID |' + idx.split('| ID |', 1)[1])
for cid in order:
    p = find(cid)
    if not p: continue
    out += ['', '---', '', f'<!-- 源文件：{p} -->', '']
    out.append(open(p, encoding='utf-8').read().rstrip())
open(os.path.join(root, 'ALL_记忆卡合集_for_Codex.md'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print(len(order), 'cards')
