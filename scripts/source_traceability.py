"""Trace source activities to independently verified Gauntlex task IDs.

The source order is authoritative. No title-based fuzzy matches are accepted as
proof of equivalent educational coverage.
"""
import argparse
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "CURRICULUM_ORDER.md"
MAPPING = ROOT / "gauntlex" / "source_traceability.json"
TASKS = ROOT / "gauntlex"

ITEM = re.compile(r"^(\\d+)\\. \\*\\*(.+?)\\*\\*.*?— \\[([^]]+)\\]\\(([^)]+)\\)")
PHASE = re.compile(r"^## (\\d{2}) · (.+)$")


def read_source():
    phase = None
    items = []
    for line in SOURCE.read_text(encoding="utf-8").splitlines():
        heading = PHASE.match(line)
        if heading:
            phase = heading.group(1)
        match = ITEM.match(line)
        if match:
            number, title, _, path = match.groups()
            items.append({"order": int(number), "title": title,
                          "phase": phase, "source_path": path})
    return items


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true", help="Print full traceability report")
    parser.add_argument("--strict", action="store_true", help="Fail while any source is unmapped")
    args = parser.parse_args()
    items = read_source()
    mappings = json.loads(MAPPING.read_text(encoding="utf-8"))
    task_ids = {p.name for p in TASKS.glob("*/[0-9][0-9][0-9]-*") if p.is_dir()}
    errors = []
    if len(items) != 693 or len({x["source_path"] for x in items}) != len(items):
        errors.append("Expected 693 unique source paths")
    expected = {x["source_path"] for x in items}
    if set(mappings) - expected:
        errors.append("Mapping includes unknown source paths")
    mapped = 0
    for item in items:
        assigned = mappings.get(item["source_path"], [])
        if not isinstance(assigned, list) or not all(isinstance(x, str) for x in assigned):
            errors.append(f"Invalid mapping: {item['source_path']}")
            continue
        if len(assigned) != len(set(assigned)):
            errors.append(f"Duplicate task mapping: {item['source_path']}")
        for task_id in assigned:
            if task_id not in task_ids:
                errors.append(f"Missing Gauntlex task {task_id} for {item['source_path']}")
        if assigned:
            mapped += 1
        item["gauntlex_task_ids"] = assigned
        item["status"] = "mapped-unreviewed" if assigned else "unmapped"
    summary = {"source_activities": len(items), "mapped_unreviewed": mapped,
               "unmapped": len(items) - mapped, "errors": errors}
    if args.json:
        print(json.dumps({"summary": summary, "activities": items}, indent=2, ensure_ascii=False))
    else:
        print(json.dumps(summary, indent=2))
    return 1 if errors or (args.strict and mapped != len(items)) else 0


if __name__ == "__main__":
    sys.exit(main())
