"""Find candidate teaching units; this step makes no sequencing decisions."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
units = []

def add(source, path, kind, **metadata):
    relative = path.relative_to(ROOT).as_posix()
    units.append({"id": relative, "source": source, "path": relative, "kind": kind, **metadata})

source = "python-curriculum"
config = json.loads((ROOT / source / "config.json").read_text())
for kind, exercises in config["exercises"].items():
    if kind not in {"concept", "practice"}: continue
    for exercise in exercises:
        folder = ROOT / source / "exercises" / kind / exercise["slug"]
        instructions = folder / ".docs" / "instructions.md"
        if not instructions.exists(): instructions = folder / "README.md"
        add(source, instructions, "exercism-" + kind, metadata=exercise, folder=folder.relative_to(ROOT).as_posix())
# Include on-disk exercises omitted from the track registry, if any.
registered = {unit.get("folder") for unit in units}
for path in sorted((ROOT / source / "exercises").glob("*/*/.docs/instructions.md")):
    if path.parent.parent.relative_to(ROOT).as_posix() not in registered:
        add(source, path, "unregistered-exercise", folder=path.parent.parent.relative_to(ROOT).as_posix())

source = "C1-Code-Crunch-Convos"
for path in sorted((ROOT / source).rglob("*.md")):
    rel = path.relative_to(ROOT / source).as_posix()
    if rel.startswith("curriculum/"):
        if "/lecture-notes/" in rel: kind = "lesson"
        elif re.search(r"/(exercises|challenges|homework)/(exercise|challenge|problem)-", rel): kind = "assignment"
        elif rel.endswith("/quiz.md"): kind = "assessment"
        elif "/mini-project/" in rel and path.name == "README.md": kind = "project"
        elif path.name in {"rubric.md", "submission-checklist.md", "starter.md", "reading-list.md", "project-brief.md"}: kind = "support"
        elif path.name == "README.md": kind = "index"
        else: kind = "review-candidate"
        add(source, path, kind)
    elif rel.startswith("projects/") and not rel.startswith("projects/solutions/"):
        add(source, path, "project" if path.name == "README.md" else "project-support")
    elif rel.startswith("resources/"):
        add(source, path, "guide")

source = "learn.python"
for path in sorted((ROOT / source / "projects").rglob("README.md")):
    folder = path.parent
    # Containers and indexes do not count as standalone projects.
    rel = folder.relative_to(ROOT / source / "projects").parts
    if any((folder / name).is_file() for name in ["project.py", "app.py", "exercise.py", "manage.py", "setup_guide.py", "build_and_test.py", "publish_guide.py"]) or (len(rel) == 2 and rel[0] == "capstones") or (len(rel) == 3 and rel[1] == "11-package-publishing"):
        add(source, path, "project", folder=folder.relative_to(ROOT).as_posix())
for path in sorted((ROOT / source / "projects").rglob("exercise.py")):
    if not (path.parent / "README.md").exists():
        add(source, path, "beginner-exercise", folder=path.parent.relative_to(ROOT).as_posix())
for path in sorted((ROOT / source / "practice" / "challenges").rglob("*.py")):
    rel = path.relative_to(ROOT / source / "practice" / "challenges")
    kind = "solution" if "solutions" in rel.parts else "test" if "tests" in rel.parts else "challenge"
    add(source, path, kind)
for path in sorted((ROOT / source / "concepts").glob("*.md")):
    add(source, path, "concept-guide" if path.name != "README.md" else "index")
for path in sorted((ROOT / source / "concepts" / "quizzes").glob("*.py")):
    add(source, path, "assessment")
for path in sorted((ROOT / source).glob("*.md")):
    add(source, path, "root-guide")
for path in sorted((ROOT / source / "curriculum").glob("*.md")):
    add(source, path, "advanced-guide")
for path in sorted((ROOT / source / "practice" / "code-reading").rglob("*")):
    if path.is_file(): add(source, path, "code-reading")

source = "30-Days-Of-Python"
for path in [ROOT / source / "readme.md", *sorted((ROOT / source).glob("[0-9][0-9]_Day_*/*.md")), ROOT / source / "numpy.md"]:
    if path.exists(): add(source, path, "day-lesson-and-exercises")

(ROOT / "review" / "candidates.json").write_text(json.dumps(units, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
from collections import Counter
for source in sorted({unit["source"] for unit in units}):
    print(source, Counter(unit["kind"] for unit in units if unit["source"] == source))
print("Candidate units:", len(units))
