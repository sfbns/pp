#!/usr/bin/env bash
# 检查溢出版心的公式/行：md -> tex -> xelatex，列出 Overfull \hbox 及其上下文。用法：tools/check_overfull.sh deliverables/X.md [工作目录]
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
IN="$1"; WD="${2:-$(mktemp -d)}"; mkdir -p "$WD"
BASE="$(basename "${IN%.md}")"
pandoc "$IN" -f markdown+tex_math_dollars+raw_tex-implicit_figures -s \
  -H "$ROOT/tools/header.tex" -V documentclass=article -V fontsize=11pt \
  -V mainfont="Latin Modern Roman" -V monofont="DejaVu Sans Mono" --toc --toc-depth=2 -o "$WD/$BASE.tex"
( cd "$WD" && xelatex -interaction=nonstopmode -halt-on-error "$BASE.tex" >/dev/null 2>&1 || true )
grep -n -A3 'Overfull \\hbox' "$WD/$BASE.log" | grep -v '^--$' | awk 'length($0)<400' || echo "no overfull hbox"
grep -c 'Overfull \\hbox' "$WD/$BASE.log" || true
