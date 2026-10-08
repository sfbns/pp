#!/usr/bin/env bash
# 将仓库根目录 zip 中的原文 PDF/页图解压到指定目录（默认 /tmp/blp_pdfs），供审稿人核对原页。
set -euo pipefail
OUT="${1:-/tmp/blp_pdfs}"; ROOT="$(cd "$(dirname "$0")/.." && pwd)"
mkdir -p "$OUT"
for z in "$ROOT"/BLP_v10_上传备份_02_文献原文与公式.zip "$ROOT"/BLP_v10_上传备份_03_文献原文与公式.zip \
         "$ROOT"/BLP公式记忆备份_20261009_part2_BLP1995原文与原页图.zip "$ROOT"/BLP公式记忆备份_20261009_part3_引用BLP的15篇原文.zip; do
  d="$OUT/$(basename "$z" .zip)"; mkdir -p "$d"
  python3 -I - "$z" "$d" <<'PY'
import zipfile, sys, os
z = zipfile.ZipFile(sys.argv[1]); d = os.path.abspath(sys.argv[2])
for i in z.infolist():
    if i.filename.lower().endswith(('.pdf', '.png')):
        p = os.path.normpath(os.path.join(d, i.filename))
        if p.startswith(d): z.extract(i, d)
PY
done
echo "PDFs extracted under $OUT"
