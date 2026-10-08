# Top-Journal Hypothesis Packaging Memory

This package contains a question-led 45-paper AER training corpus for economics theory, model choice, hypothesis design, identification boundaries, structural judgment, and economics writing.

## Entry points

- `QUESTION_PROTOCOL.md`: mandatory reading questions and evidence rules.
- `selection_manifest.csv`: 45-paper source and status ledger.
- `cards/`: one bridge card per paper.
- `synthesis/`: cross-paper hypothesis-packaging patterns and failure modes.
- `agent_memories/`: specialist-specific durable memories.
- `agent_card_coverage.csv`: 13 × 45 agent–paper relevance, hash, source-status, and promotion ledger.
- `audits/`: coverage, path, schema, and configuration checks.

## Current integration

- shared skill: `D:\codex\.codex-home\skills\top-journal-hypothesis-packaging`
- current personal custom agents: `D:\codex\.codex-home\agents` (13 roles)
- legacy project custom agents: `D:\codex\economics_theory_agent_complete_gpt55_xhigh\.codex\agents` (13 roles)
- collaboration contract: `D:\codex\.codex-home\skills\top-journal-hypothesis-packaging\references\orchestration-contract.md`
- private memory policy: each specialist loads its own file under `agent_memories/`; the active expert owns conflict resolution and the final synthesis.

## Status

- selected papers: 45
- journal: American Economic Review
- publication years: 2025-2026
- source stack at selection: 45/45 PDF paths, 45/45 third-pass memories, 45/45 source packs present
- completion claim: bridge-card production only; underlying paper evidence status remains governed by each source package
- bridge cards: 45/45 complete and schema-validated
- specialist memories: 13/13 complete and role-distinct
- agent–paper coverage decisions: 585/585 complete with card hashes
- personal custom agents: 13/13 TOML-parse valid
- legacy project custom agents: 13/13 TOML-parse valid
- shared skill: validation passed with the UTF-8 wrapper
- orchestration: four-wave contract registered; specialist conditions and evidence handoffs explicit
- release audit: `audits/2026-08-28_validation_report.md` with companion SHA256; final validator result `pass: true`
