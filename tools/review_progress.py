"""Validate saved review decisions without claiming unfinished source coverage."""
import csv
from collections import Counter
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
with (ROOT / "review/task_notes.tsv").open(encoding="utf-8", newline="") as handle:
    rows = list(csv.DictReader(handle, delimiter="\t"))
paths = [row["source_path"] for row in rows]
duplicates = [path for path, count in Counter(paths).items() if count > 1]
missing = [path for path in paths if not (ROOT / path).is_file()]
assert not duplicates, f"Duplicate decision paths: {duplicates}"
assert not missing, f"Missing reviewed source paths: {missing}"
assert all(row["objective"] and row["concepts"] and row["review_note"] for row in rows)
counts = Counter(path.split("/", 1)[0] for path in paths)
questions = json.loads((ROOT / "review/30days_decisions.json").read_text(encoding="utf-8"))
question_ids = [question["id"] for question in questions]
assert len(set(question_ids)) == len(question_ids), "Duplicate 30Days question IDs"
for question in questions:
    source = ROOT / question["path"]
    assert source.is_file(), question["path"]
    lines = source.read_text(encoding="utf-8-sig").splitlines()
    assert 0 < question["line"] <= len(lines), question["id"]
    assert lines[question["line"] - 1].strip() == question["text"].splitlines()[0].strip(), question["id"]
    assert question["objective"] and question["concepts"] and question["review_note"], question["id"]
candidate_path = ROOT / "review/candidates.json"
c1_prefix = 0
if candidate_path.is_file():
    candidates = json.loads(candidate_path.read_text(encoding="utf-8"))
    c1 = [unit for unit in candidates if unit["source"] == "C1-Code-Crunch-Convos" and unit["kind"] == "assignment"]
    reviewed_paths = set(paths)
    for unit in c1:
        if unit["path"] not in reviewed_paths:
            break
        c1_prefix += 1
report = {"tsv_reviewed_units": len(rows), "by_source": dict(sorted(counts.items())),
                  "separate_30days_reviewed_parent_questions": len(questions),
                  "question_line_anchors_match_source": True,
                  "source_paths_exist": True, "decision_paths_unique": True,
                  "c1_contiguous_reviewed_assignment_prefix": c1_prefix,
                  "final_curriculum_validated": False}
(ROOT / "review/review_progress.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, indent=2))
