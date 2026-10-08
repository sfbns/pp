# BLP CSV / Manifest / Fulltext Audit

- Audit date: `2026-04-18`
- Audit scope: `D:/codex/导出的条目.csv` versus `D:/codex/blp_structural_memory_2026-04-18/manifests/blp_zotero_collection_manifest.json`
- Audit goal: verify whether the current BLP corpus should truthfully be described as a fulltext-grounded durable-memory corpus and where that claim should stop.

## Coverage Result
- CSV rows: `28`
- CSV unique Zotero keys: `28`
- Manifest papers: `28`
- Keys missing in manifest: `0`
- Keys missing in CSV: `0`

## Asset Result
- Papers missing original PDF: `0`
- Papers missing `fulltext.json`: `0`
- Papers missing `fulltext.txt`: `0`
- Papers missing per-paper memory: `0`
- Papers with non-empty page-level fulltext: `28/28`

## Memory Structure Result
- Papers missing required per-paper memory blocks: `0`
- Required block family checked: `Read Basis`, `APA Citation Memory`, `Story Memory`, `Theory And Research Design`, `Baseline Regression / Baseline Structural Core`, `Mechanism And Further Analysis Logic`, `Result Interpretation`, `BLP Structural Memory`, `Writing Logic And Style`, `Writing Memory`, `Claude Stop-Hook Writeback`, `Fulltext Structure`, `Evidence Anchors`

## OCR / Source Mix
- Papers with newly linked MinerU `llm_json_rel`: `9`
- Papers using previously prepared legacy fulltext layers: `19`
- Fulltext page-count range across the corpus: `13` to `91`
- Non-empty page-count range across the corpus: `13` to `91`

## Honest Claim Boundary
- This corpus may truthfully be described as a `fulltext-grounded durable-memory corpus`.
- This corpus may truthfully be described as having per-paper memory for story logic, model design, baseline structural core, mechanism logic, result interpretation, writing logic, vocabulary, APA citation forms, and Claude stop-hook writeback.
- This audit does **not** justify saying that every paper received uniform sentence-by-sentence manual close reading.
- This audit does **not** justify saying that every equation or derivation was manually rechecked against the original PDF.
- When stronger claims are needed, the paper must be re-opened and manually validated at the section, equation, or proof level.
