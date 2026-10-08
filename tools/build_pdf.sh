#!/usr/bin/env bash
# md -> PDF：pandoc + XeLaTeX（xeCJK + amsmath）。用法：tools/build_pdf.sh deliverables/X.md [out.pdf]
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
IN="$1"; OUT="${2:-${IN%.md}.pdf}"
pandoc "$IN" -f markdown+tex_math_dollars+raw_tex-implicit_figures --pdf-engine=xelatex \
  -H "$ROOT/tools/header.tex" -V documentclass=article -V fontsize=11pt \
  -V mainfont="Latin Modern Roman" -V toc-title="目录" --toc --toc-depth=2 -o "$OUT"
echo "built $OUT"
