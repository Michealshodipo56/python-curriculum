"""Build one learner-facing Markdown document from Gauntlex task briefs.

Publishing utility only: it does not execute learner code or tests.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "GAUNTLEX_PYTHON_CURRICULUM.md"
PATTERN = re.compile(r"^(\d{3})-[^/]+$")


def main():
    entries = []
    for path in (ROOT / "gauntlex").glob("*/*/README.md"):
        match = PATTERN.fullmatch(path.parent.name)
        if match:
            entries.append((int(match.group(1)), path))
    entries.sort()
    if [number for number, _ in entries] != list(range(1, 410)):
        raise SystemExit("Expected exactly one README for each ID 001–409.")

    regular = [(n, p) for n, p in entries if p.parent.parent.name != "18-capstones"]
    capstones = [(n, p) for n, p in entries if p.parent.parent.name == "18-capstones"]
    sections = [
        "# Gauntlex Python Curriculum",
        "",
        "> Single-file learner-facing curriculum assembled from rewritten exercise briefs.",
        "> Order is provisional pending full prerequisite and source coverage review.",
        "> No solutions or answer keys are included.",
        "",
        "**Total exercises: 409**",
        "",
    ]
    current = None
    for number, path in regular + capstones:
        module = path.parent.parent.name
        if module != current:
            current = module
            sections.extend(["---", "", "## " + module.split("-", 1)[1].replace("-", " ").title(), ""])
        body = path.read_text(encoding="utf-8").strip().splitlines()
        if body and body[0].startswith("# "):
            body[0] = "### " + str(number).zfill(3) + " — " + body[0][2:]
        sections.extend(["*Source: " + path.relative_to(ROOT).as_posix() + "*", "", *body, ""])
    OUT.write_text("\n".join(sections) + "\n", encoding="utf-8")
    print("Wrote", OUT, "with", len(entries), "tasks")


if __name__ == "__main__":
    main()
