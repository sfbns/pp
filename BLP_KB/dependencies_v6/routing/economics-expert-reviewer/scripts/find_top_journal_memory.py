from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


AER_CARD_INDEX = Path(
    r"D:\codex\research-memory\deep-reading\aer_full_ocr_20260407\cards\themes\thematic_clusters_index_001_100.json"
)
AER_MANIFEST = Path(
    r"D:\codex\research-memory\deep-reading\aer_full_ocr_20260407\third_pass_agent_memory_20260608\indexes\paper_memory_manifest.json"
)
AEJ_CARD_INDEX = Path(
    r"D:\codex\research-memory\deep-reading\aej_full_ocr_20260406\cards\second_pass_cards_index_001_107.json"
)


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def normalize(value: object) -> str:
    if isinstance(value, list):
        value = " ".join(str(item) for item in value)
    return " ".join(str(value or "").lower().replace("_", " ").split())


def load_records() -> list[dict]:
    aer_cards = {item["number"]: item for item in read_json(AER_CARD_INDEX)}
    aer_items = read_json(AER_MANIFEST)["items"]
    records: list[dict] = []

    for item in aer_items:
        card = aer_cards.get(item["number"], {})
        records.append(
            {
                **card,
                **item,
                "corpus": "AER",
                "evidence_layer": "third-pass memory plus second-pass card",
            }
        )

    for item in read_json(AEJ_CARD_INDEX):
        records.append(
            {
                **item,
                "corpus": "AEJ",
                "evidence_layer": "full-OCR second-pass card",
            }
        )
    return records


def searchable_text(record: dict) -> str:
    fields = [
        "title",
        "story_ladder",
        "framework",
        "innovation_source",
        "reusable_move",
        "tags",
        "themes",
        "primary_theme",
    ]
    return normalize(" ".join(normalize(record.get(field)) for field in fields))


def query_score(record: dict, query: str | None) -> int:
    if not query:
        return 1
    phrase = normalize(query)
    title = normalize(record.get("title"))
    haystack = searchable_text(record)
    tokens = phrase.split()
    if not all(token in haystack for token in tokens):
        return 0
    score = sum(haystack.count(token) for token in tokens)
    if phrase == title:
        score += 100
    elif phrase in title:
        score += 40
    elif phrase in haystack:
        score += 15
    return score


def record_matches(record: dict, args: argparse.Namespace) -> tuple[bool, int]:
    if args.corpus != "all" and normalize(record["corpus"]) != args.corpus:
        return False, 0
    if args.number is not None and record.get("number") != args.number:
        return False, 0
    tags = {normalize(tag) for tag in record.get("tags", [])}
    if args.tag and normalize(args.tag) not in tags:
        return False, 0
    themes = {normalize(theme) for theme in record.get("themes", [])}
    primary_theme = normalize(record.get("primary_theme"))
    if args.theme and normalize(args.theme) not in themes | {primary_theme}:
        return False, 0
    score = query_score(record, args.query)
    return score > 0, score


def batch_card_path(record: dict) -> str | None:
    batch = record.get("batch")
    if not batch:
        return None
    corpus = normalize(record["corpus"])
    root = Path(r"D:\codex\research-memory\deep-reading")
    if corpus == "aer":
        return str(root / "aer_full_ocr_20260407" / "cards" / f"second_pass_cards_batch_{batch}.md")
    return str(root / "aej_full_ocr_20260406" / "cards" / f"second_pass_cards_batch_{batch}.md")


def render(record: dict) -> str:
    corpus = record["corpus"]
    number = int(record["number"])
    lines = [
        f"[{corpus} {number:03d}] {record['title']}",
        f"Evidence layer: {record['evidence_layer']}",
    ]
    if record.get("story_ladder"):
        lines.append(f"Story ladder: {record['story_ladder']}")
    if record.get("innovation_source"):
        lines.append(f"Innovation source: {record['innovation_source']}")
    if record.get("reusable_move"):
        lines.append(f"Reusable move: {record['reusable_move']}")
    if record.get("tags"):
        lines.append("Tags: " + ", ".join(record["tags"]))
    if record.get("themes"):
        lines.append("Themes: " + ", ".join(record["themes"]))

    next_paths = []
    for label, field in (
        ("paper memory", "memory"),
        ("source pack", "source_pack"),
        ("OCR artifact", "artifact_md"),
        ("batch card", None),
    ):
        value = batch_card_path(record) if field is None else record.get(field)
        if value:
            next_paths.append(f"  - {label}: {value}")
    if next_paths:
        lines.append("Open next:")
        lines.extend(next_paths)
    if record.get("source_pdf"):
        lines.append(f"Clean-PDF path recorded by memory: {record['source_pdf']}")
    return "\n".join(lines)


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(
        description="Search the local AER third-pass and AEJ second-pass research memories."
    )
    parser.add_argument("--query", help="Words that must all appear in searchable card fields.")
    parser.add_argument("--corpus", choices=("all", "aer", "aej"), default="all")
    parser.add_argument("--number", type=int, help="Paper number within the selected corpus.")
    parser.add_argument("--tag")
    parser.add_argument("--theme", help="AER thematic-cluster label.")
    parser.add_argument("--limit", type=int, default=5)
    args = parser.parse_args()

    ranked = []
    for record in load_records():
        matched, score = record_matches(record, args)
        if matched:
            ranked.append((score, record))
    ranked.sort(key=lambda pair: (-pair[0], pair[1]["corpus"], pair[1]["number"]))

    if not ranked:
        print("No matching top-journal memory found.")
        return

    for index, (_, record) in enumerate(ranked[: args.limit]):
        if index:
            print("\n" + "-" * 88 + "\n")
        print(render(record))


if __name__ == "__main__":
    main()
