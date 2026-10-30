"""Static validation of authored Gauntlex task packages.

This does not execute learner tests: starter functions are intentionally unfinished.
"""
import ast
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1] / "gauntlex"
REQUIRED = ("README.md", "metadata.json", "starter/solution.py", "tests/test_solution.py")
CAPSTONE = ("README.md", "metadata.json", "starter/main.py", "tests/test_acceptance.py")
PROGRAM = ("README.md", "metadata.json", "starter/main.py", "tests/test_main.py")


def main():
    errors = []
    count = 0
    ids = set()
    metadata_by_id = {}
    task_numbers = set()
    for meta_path in sorted(ROOT.glob("*/[0-9][0-9][0-9]-*/metadata.json")):
        task = meta_path.parent
        count += 1
        try:
            meta = json.loads(meta_path.read_text(encoding="utf-8"))
        except (ValueError, OSError) as exc:
            errors.append(f"{task}: invalid metadata: {exc}")
            continue
        expected_id = task.name
        if meta.get("id") != expected_id:
            errors.append(f"{task}: metadata id mismatch: {meta.get('id')!r}")
        if expected_id in ids:
            errors.append(f"{task}: duplicate id")
        ids.add(expected_id)
        metadata_by_id[expected_id] = meta
        task_numbers.add(int(expected_id[:3]))
        if meta.get("module") != task.parent.name:
            errors.append(f"{task}: module mismatch")
        if not isinstance(meta.get("prerequisites"), list):
            errors.append(f"{task}: prerequisites must be a list")
        task_type = meta.get("task_type")
        files = CAPSTONE if task_type == "capstone" else PROGRAM if task_type == "program" else REQUIRED
        for rel in files:
            path = task / rel
            if not path.is_file():
                errors.append(f"{task}: missing {rel}")
                continue
            if path.suffix == ".py":
                try:
                    ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
                except (SyntaxError, UnicodeError) as exc:
                    errors.append(f"{path}: syntax/encoding error: {exc}")
        if meta.get("status") != "draft-tests-not-run":
            errors.append(f"{task}: unexpected validation status")
        if not isinstance(meta.get("guide"), dict) or not isinstance(meta.get("auditor"), dict):
            errors.append(f"{task}: missing guide/auditor configuration")
    for path in ROOT.glob("*/[0-9][0-9][0-9]-*/"):
        if not (path / "metadata.json").exists():
            errors.append(f"{path}: missing metadata.json")
    if task_numbers:
        expected_numbers = set(range(1, max(task_numbers) + 1))
        missing = sorted(expected_numbers - task_numbers)
        if missing:
            errors.append(f"missing task numbers: {missing}")
    for task_id, meta in metadata_by_id.items():
        for prerequisite in meta.get("prerequisites", []):
            if prerequisite not in ids:
                errors.append(f"{task_id}: missing prerequisite {prerequisite}")
            elif int(prerequisite[:3]) >= int(task_id[:3]):
                errors.append(f"{task_id}: prerequisite must precede task: {prerequisite}")
    print(f"Static audit: {count} task packages, {len(errors)} issue(s)")
    for error in errors:
        print(error, file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
