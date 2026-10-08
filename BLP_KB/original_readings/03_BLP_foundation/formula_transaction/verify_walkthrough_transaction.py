from pathlib import Path
import sys, json, hashlib, difflib, shutil, subprocess, os

ROOT = Path(__file__).resolve().parent
TX = ROOT / 'package' / '03_BLP_foundation' / 'formula_transaction'
TARGET = Path(r'D:\codex\research-memory\BLP_structural_models_memory_skills_configs_2026-08-24\03_economics_theory_agent\kb\03_structural_models\foundations\01-user-verified-blp-model-construction-walkthrough-2026-05-20.md')
PY = sys.executable
GIT = Path(r'C:\Users\于舒奕\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\git\cmd\git.exe')
SH = GIT.parent.parent / 'usr' / 'bin' / 'sh.exe'

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest().upper()

def evaluate(path, inp):
    data = json.loads(Path(inp).read_text(encoding='utf-8'))
    text = Path(path).read_text(encoding='utf-8')
    part = text.split('### 33.', 1)[1].split('## 十二', 1)[0]
    expression = part.split('s_j[\\theta,P_h^*(\\theta\')_{ns}]', 1)[1].split('意思是', 1)[0]
    normalized = '\\frac{1}{ns}' in expression or '\\frac1{ns}' in expression
    total = sum(data['bar_s'] / fbar * fj for fbar, fj in zip(data['fbar'], data['fj']))
    estimate = total / data['ns'] if normalized else total
    print(json.dumps({'input': data, 'normalization': '1/ns' if normalized else 'missing',
                      'share_estimate': round(estimate, 12), 'expected_share': data['expected'],
                      'normalization_check': 'PASS' if abs(estimate-data['expected']) < 1e-12 else 'FAIL'}, ensure_ascii=False))
    # An observed wrong formula is still a successfully executed numerical evaluation.
    return 0

if len(sys.argv)>1 and sys.argv[1]=='evaluate':
    raise SystemExit(evaluate(sys.argv[2], sys.argv[3]))

TX.mkdir(parents=True, exist_ok=True)
original_hash = sha(TARGET)
baseline = TX / 'ORIGINAL_BASELINE.md'
modified = TX / 'MODIFIED_FILE.md'
patch = TX / 'DIFF_FILE.patch'
rollback = TX / 'ROLLBACK.sh'
verification = TX / 'VERIFICATION.txt'
shutil.copyfile(TARGET, baseline)
input_file = TX / 'same_input.json'
input_file.write_text(json.dumps({'ns':4,'bar_s':0.6,'fbar':[0.6]*4,'fj':[0.3]*4,'expected':0.3}, indent=2), encoding='utf-8')
shutil.copyfile(Path(__file__), TX / 'verify_walkthrough_transaction.py')
events=[]
def run(label, args, cwd=None):
    env=os.environ.copy()
    env['PATH']=str(SH.parent)+os.pathsep+env.get('PATH','')
    result = subprocess.run([str(v) for v in args], cwd=cwd, env=env, capture_output=True, text=True, encoding='utf-8', errors='replace')
    events.append({'label':label,'command':[str(v) for v in args], 'cwd':str(cwd) if cwd else None,
                   'stdout':result.stdout,'stderr':result.stderr,'exit_status':result.returncode})
    (ROOT/'transaction_execution_events.json').write_text(json.dumps(events,ensure_ascii=False,indent=2),encoding='utf-8')
    if result.returncode: raise RuntimeError(f'{label}: {result.returncode}: {result.stderr}')
    return result

run('BASELINE',[PY,__file__,'evaluate',TARGET,input_file])
raw = TARGET.read_bytes()
text = raw.decode('utf-8')
newline = '\r\n' if '\r\n' in text else '\n'
old = '\\sum_{i=1}^{ns}' + newline + '\\frac{\\bar s(\\theta\',P_0)}{\\bar f(\\nu_i,\\theta\')}'
assert text.count(old)==1, 'Expected exactly one literal (6.13) source site'
new = '\\frac{1}{ns}' + newline + old
text = text.replace(old,new,1)
needle='意思是：**过度抽样可能买车的人，再用权重校正回来。**'
note=(newline+newline+'**2026-10-07 本包修订（standard-derived，不冒充原文逐字式）。** '
      '已重新观察 PDF 第28页／期刊第867页：原印式(6.13)的求和没有 `1/ns`。'
      '这里明确令 `ns` 为固定数量的已接受抽样，抽样密度为 '
      '`h(ν)=f̄(ν,θ′)p₀(ν)/s̄(θ′,P₀)`；标准重要性抽样估计必须取加权样本均值，故补上 `1/ns`。'
      '若 `ns` 指总提议抽样数而非接受数，不能照搬这一归一化。'
      '本次仅修订该公式的归一化，保留此前已修正的(6.9b)及其他内容；未宣称全篇每式新审。')
assert text.count(needle)==1
text=text.replace(needle,needle+note,1)
modified.write_bytes(text.encode('utf-8'))
patch.write_bytes(''.join(difflib.unified_diff(raw.decode('utf-8').splitlines(True),text.splitlines(True),
                     fromfile='a/walkthrough.md',tofile='b/walkthrough.md')).encode('utf-8'))
rollback.write_text('#!/bin/sh\nset -eu\n[ "$#" -eq 1 ] || { printf "%s\\n" "Usage: ROLLBACK.sh TARGET_COPY" >&2; exit 64; }\n'
                    'here=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)\n'
                    'cp -- "$here/ORIGINAL_BASELINE.md" "$1"\n'
                    'printf "%s\\n" "ROLLBACK restored pristine baseline bytes"\n',encoding='utf-8',newline='\n')
rollback.chmod(0o755)
run('MODIFIED',[PY,__file__,'evaluate',modified,input_file])
restored = TX / 'rollback_test_copy.md'
shutil.copyfile(modified,restored)
def msys(p):
    p=Path(p).resolve().as_posix()
    return '/'+p[0].lower()+p[2:] if len(p)>2 and p[1]==':' else p
run('ROLLBACK_EXECUTION',[SH,msys(rollback),msys(restored)])
run('ROLLBACK',[PY,__file__,'evaluate',restored,input_file])
assert sha(restored)==original_hash
reconstruct = ROOT / 'patch_reconstruction'
reconstruct.mkdir(exist_ok=True)
shutil.copyfile(baseline,reconstruct/'walkthrough.md')
run('PATCH_RECONSTRUCTION',[GIT,'-c','core.autocrlf=false','apply','--whitespace=nowarn',patch],cwd=reconstruct)
assert sha(reconstruct/'walkthrough.md')==sha(modified)
assert sha(TARGET)==original_hash
assert '\\frac{1}{ns}' in modified.read_text(encoding='utf-8').split('### 33.',1)[1].split('## 十二',1)[0]
result={'target':str(TARGET),'changed_symbol':'BLP (1995) equation (6.13): fixed-accepted-draw importance-sampling normalization 1/ns',
        'target_sha256_before':original_hash,'target_sha256_after':sha(TARGET),
        'modified_sha256':sha(modified),'rollback_sha256':sha(restored),
        'rollback_hash_matches_original':True,'diff_reconstructs_modified':True,
        'same_input':str(input_file),'events':events,
        'scope':'Numerical evaluation of the formula transcribed in the Markdown, not execution of the authors\' estimation code. All other source files remain unchanged.',
        'prior_tool_errors':[{'command':'bundled Python -c import fitz; render BLP pages','stderr':"ModuleNotFoundError: No module named 'fitz'",'exit_status':1,
                            'correction':'Used existing system Python312 with PyMuPDF 1.27.2.2; render exited 0.'},
                            {'command':'Git runtime sh.exe ROLLBACK.sh rollback_test_copy.md (sandboxed)',
                             'stderr':'fatal error - NtCreateDirectoryObject(\\BaseNamedObjects\\msys-2.0S5-0cff3f3dc099f6c2): 0xC0000022',
                             'exit_status':3221225794,'correction':'Repeat the same self-contained transaction in an approved unsandboxed execution; no source bytes are modified.'},
                            {'command':'Git runtime sh.exe ROLLBACK.sh rollback_test_copy.md (approved unsandboxed)',
                             'stderr':'line 4: dirname: command not found\nline 5: cp: command not found',
                             'exit_status':127,'correction':'Prepend the bundled Git usr/bin to the child PATH; rerun unchanged rollback script.'}]}
verification.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
for p in (modified,patch,verification,rollback):
    data=p.read_bytes()
    assert data
    print(json.dumps({'role_path':str(p.resolve()),'bytes':len(data),'sha256':sha(p)},ensure_ascii=False))
print(json.dumps({'BASELINE':json.loads(events[0]['stdout'])['share_estimate'],
                  'MODIFIED':json.loads(events[1]['stdout'])['share_estimate'],
                  'ROLLBACK':json.loads(events[3]['stdout'])['share_estimate'],
                  'original_unchanged':sha(TARGET)==original_hash,'rollback_hash_match':True,'patch_reconstruction':True}))
