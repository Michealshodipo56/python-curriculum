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

    sections = [
        "# Gauntlex Python Curriculum",
        "",
        "> Single-file learner-facing curriculum assembled from the existing challenge briefs.",
        "> Follow challenge IDs in numeric order, including the project checkpoints.",
        "> No solutions or answer keys are included.",
        "",
        "**409 challenges across 23 sections.**",
        "",
        "Navigation: [Learning path](GAUNTLEX_LEARNING_PATH.md) · "
        "[Curriculum order](CURRICULUM_ORDER.md) · [Audit report](CURRICULUM_AUDIT_REPORT.md)",
        "",
        "Each assignment's file paths are relative to its linked challenge directory. "
        "Challenges 311–314 are core projects; challenges 405–409 are final projects. "
        "This preserves the prerequisite from 314 to 315 without renumbering any package.",
        "",
    ]
    current = None
    for number, path in entries:
        module = path.parent.parent.name
        if module != current:
            current = module
            title = module.split("-", 1)[1].replace("-", " ").title()
            if module == "18-capstones":
                title += " — Core Projects" if number < 405 else " — Final Projects"
            sections.extend(["---", "", "## " + title, ""])
        body = path.read_text(encoding="utf-8").strip().splitlines()
        # Nest assignment headings beneath the section, leaving fenced examples intact.
        in_fence = False
        for index, line in enumerate(body):
            if line.startswith(("```", "~~~")):
                in_fence = not in_fence
            elif not in_fence and re.match(r"^#{1,4} ", line):
                body[index] = "##" + line
        if body and body[0].startswith("### "):
            body[0] = "### " + str(number).zfill(3) + " — " + body[0][4:]
        source = path.relative_to(ROOT).as_posix()
        content = body[1:]
        if content and not content[0]:
            content = content[1:]
        sections.extend([*body[:1], "", "Assignment: [" + path.parent.name + "](" + source + ")", "", *content, ""])
    OUT.write_text("\n".join(sections) + "\n", encoding="utf-8")
    print("Wrote", OUT, "with", len(entries), "tasks")


if __name__ == "__main__":
    main()
