"""Extract full numbered exercise blocks for semantic review, never sequence them.

Indented subquestions remain part of their parent assignment. Exact source line
locators distinguish unnamed questions sharing a single chapter file.
"""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]

def extract(path):
    lines = path.read_text(encoding="utf-8-sig").splitlines()
    minima = {}
    section_line = None
    in_fence = False
    for number, line in enumerate(lines, 1):
        if line.lstrip().startswith(("```", "~~~")):
            in_fence = not in_fence
        if not in_fence and re.match(r"^#{1,6} .*Exercises?", line, re.I):
            section_line = number
        match = re.match(r"^( {0,3})\d+\.\s+", line) if not in_fence else None
        if match and section_line is not None:
            minima[section_line] = min(minima.get(section_line, 4), len(match[1]))
    active = False
    fence = False
    section = ""
    current = None
    base_indent = None
    tasks = []
    for number, line in enumerate(lines, 1):
        if line.lstrip().startswith(("```", "~~~")):
            fence = not fence
        if not fence and re.match(r"^#{1,6} .*Exercises?", line, re.I):
            if current:
                tasks.append(current)
                current = None
            active = True
            section = line.lstrip("# ")
            base_indent = minima.get(number)
        if not active:
            continue
        match = re.match(r"^( {0,3})(\d+)\.\s+(.*)", line) if not fence else None
        if match and base_indent is None:
            base_indent = len(match[1])
        # A few source lists vary by one space at the top level. A nested
        # three-space list after unindented parents remains a subquestion.
        if match and len(match[1]) > base_indent + (1 if base_indent == 0 else 0):
            match = None
        if match:
            if current:
                tasks.append(current)
            current = {"path": path.relative_to(ROOT).as_posix(), "line": number,
                       "section": section, "item": int(match[2]), "lines": [line]}
        elif current:
            current["lines"].append(line)
    if current:
        tasks.append(current)
    for task in tasks:
        text = "\n".join(task.pop("lines")).strip()
        text = re.split(r"\n(?:🎉|🌕|\[<<|\[ <<)", text)[0].rstrip()
        task["text"] = text
        task["id"] = f"{task['path']}#L{task['line']}"
    return tasks

if __name__ == "__main__":
    units = json.loads((ROOT / "review/candidates.json").read_text(encoding="utf-8"))
    all_tasks = []
    for unit in units:
        if unit["source"] != "30-Days-Of-Python": continue
        tasks = extract(ROOT / unit["path"])
        all_tasks.extend(tasks)
        print(unit["path"], len(tasks))
    (ROOT / "review/.cache/30days_questions.json").write_text(json.dumps(all_tasks, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
    print("Numbered parent questions:", len(all_tasks))
