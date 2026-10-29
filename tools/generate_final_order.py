"""Generate the reviewed, source-linked Python curriculum order.

The source repositories are pinned submodules. This generator reads each primary
task file and its local starter/test contract before assigning it to one phase.
It intentionally excludes lessons, indexes, solutions and answer keys.
"""
from __future__ import annotations

import ast
import csv
import hashlib
import json
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "CURRICULUM_ORDER.md"


PHASES = [
    ("01", "Start here: terminal, REPL and first programs", "Run Python, read tracebacks, print values, and save a script before introducing abstractions."),
    ("02", "Values, input and expressions", "Variables, numeric operations, strings, booleans, conversion and user input."),
    ("03", "Decisions and repetition", "Comparisons, conditionals, loops and small stateful programs."),
    ("04", "Collections and data shaping", "Lists, tuples, dictionaries, sets, comprehensions and nested data."),
    ("05", "Functions, modules and decomposition", "Return values, parameters, scope, recursion, imports and reusable program structure."),
    ("06", "Files, errors, dates and text parsing", "Path handling, CSV/JSON, exceptions, regular expressions, validation and robust I/O."),
    ("07", "Objects, typing and Python protocols", "Classes, dataclasses, inheritance, iterators, generators and type contracts."),
    ("08", "Algorithms and data structures", "Complexity, search, sorting, stacks, queues, trees, graphs and dynamic programming."),
    ("09", "Testing, debugging and code quality", "pytest, fixtures, parametrization, mocking, refactoring and quality gates."),
    ("10", "Command-line tools and automation", "CLI design, filesystem automation, scheduling, subprocesses and resilient batch work."),
    ("11", "HTTP, scraping and API clients", "HTTP fundamentals, requests, authentication, pagination, scraping and client design."),
    ("12", "Databases and durable data", "SQLite, SQL, ORM patterns, migrations, idempotency and data pipelines."),
    ("13", "Web applications and services", "Flask, FastAPI, Django, forms, sessions, CRUD services and API delivery."),
    ("14", "Data analysis, statistics and machine learning", "NumPy, pandas, visualization, statistics, model training and evaluation."),
    ("15", "Async and concurrent Python", "Coroutines, producer-consumer systems, concurrent I/O and process coordination."),
    ("16", "Packaging, delivery and operations", "Packages, Docker, CI, deployment, configuration and operational readiness."),
    ("17", "Architecture, security and reliability", "System boundaries, observability, policy, performance, resilience and technical leadership."),
    ("18", "Capstones", "Integrate multiple domains into portfolio-scale, tested and documented systems."),
]

PHASE_BY_NUMBER = {number: (index, title, description) for index, (number, title, description) in enumerate(PHASES)}


@dataclass
class Task:
    path: str
    source: str
    kind: str
    title: str
    phase: int
    difficulty: str
    objective: str
    source_rank: int
    local_rank: str
    bytes: int
    sha256: str
    contract_files: int
    excluded_reason: str = ""


def read_text(path: Path) -> str:
    raw = path.read_bytes()
    if raw.startswith((b"\xff\xfe", b"\xfe\xff")):
        return raw.decode("utf-16")
    try:
        return raw.decode("utf-8-sig")
    except UnicodeDecodeError:
        return raw.decode("cp1252")


def clean_title(value: str) -> str:
    value = re.sub(r"[*_`#]", "", value)
    value = re.sub(r"\s+", " ", value).strip(" -—:|")
    return value


def title_for(path: Path, text: str, unit: dict) -> str:
    if unit["source"] == "python-curriculum":
        authored_name = unit.get("metadata", {}).get("name")
        if authored_name:
            return clean_title(authored_name)
        slug = unit.get("metadata", {}).get("slug") or path.parent.parent.name
        return clean_title(slug.replace("-", " ").title())
    if unit["kind"] == "beginner-exercise":
        slug = re.sub(r"^\d+-", "", path.parent.name)
        return clean_title(slug.replace("-", " ").title())
    if path.suffix.lower() == ".py":
        try:
            doc = ast.get_docstring(ast.parse(text))
        except SyntaxError:
            doc = None
        if doc:
            first = clean_title(doc.splitlines()[0])
            if first and len(first) <= 100 and re.search(r"[A-Za-z0-9]", first):
                return first
    for match in re.finditer(r"^#\s+(.+)$", text, re.MULTILINE):
        title = clean_title(match.group(1))
        if title.lower() not in {"instructions", "exercise", "exercises"} and re.search(r"[A-Za-z0-9]", title):
            return title
    slug = path.parent.name if path.name.lower() in {"readme.md", "instructions.md"} else path.stem
    return clean_title(slug.replace("_", " ").replace("-", " ").title())


def first_objective(text: str) -> str:
    scrubbed = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    scrubbed = re.sub(r"<!--.*?-->", "", scrubbed, flags=re.DOTALL)
    lines = [re.sub(r"\s+", " ", line).strip() for line in scrubbed.splitlines()]
    for index, line in enumerate(lines):
        if line.lower() in {"## focus", "# focus", "## objective", "## goal", "## your task"}:
            for candidate in lines[index + 1 : index + 8]:
                candidate = candidate.lstrip("-* ")
                if candidate and not candidate.startswith("#"):
                    return candidate[:220]
    for line in lines:
        candidate = line.lstrip("-* ")
        if len(candidate) >= 35 and not candidate.startswith(("#", "[", "|", "<")):
            return candidate[:220]
    return "Complete the authored task and satisfy its source contract."


def companion_count(unit: dict, path: Path) -> int:
    folder = ROOT / unit.get("folder", str(path.parent.relative_to(ROOT)))
    companions: set[Path] = set()
    for pattern in ("*.py", "tests/*.py", "test*.py", "*_test.py"):
        companions.update(item for item in folder.glob(pattern) if item.is_file() and item != path)
    if unit["source"] == "python-curriculum":
        companions.update(item for item in (folder / ".docs").glob("*.md") if item.is_file() and item != path and item.name != "hints.md")
    # Reading every companion here makes missing/unreadable contracts fail generation.
    for companion in sorted(companions):
        read_text(companion)
    return len(companions)


def load_notes() -> dict[str, dict[str, str]]:
    with (ROOT / "review/task_notes.tsv").open(encoding="utf-8", newline="") as handle:
        return {row["source_path"]: row for row in csv.DictReader(handle, delimiter="\t")}


NOTE_PHASE = {
    "first-programs": 0,
    "functions": 4,
    "function-arguments": 4,
    "advanced-functions": 6,
    "logic-functions": 2,
    "sequence-text": 2,
    "iteration": 2,
    "collections": 3,
    "collections-logic": 3,
    "collections-mutation": 3,
    "nested-collections": 3,
    "mapping": 3,
    "mappings": 3,
    "set-algebra": 3,
    "formatting": 3,
    "formatting-datetime": 5,
    "validation": 5,
    "errors": 5,
    "exceptions": 5,
    "dates": 5,
    "text-parsing": 5,
    "reporting": 5,
    "classes": 6,
    "objects": 6,
    "classes-validation": 6,
    "object-protocols": 6,
    "iterators": 6,
    "enums": 6,
    "higher-order-functions": 6,
    "context-managers": 6,
    "recursion": 7,
    "binary": 7,
    "binary-encoding": 7,
    "numeric-algorithms": 7,
    "number-algorithms": 7,
    "search-algorithms": 7,
    "sequence-algorithms": 7,
    "stacks": 7,
    "queues": 7,
    "linked-structures": 7,
    "trees": 7,
    "trees-refactoring": 7,
    "graphs": 7,
    "dynamic-programming": 7,
    "combinatorics": 7,
    "constraint-solving": 7,
    "composite-algorithms": 7,
    "grid-search": 7,
    "state-search": 7,
    "decomposition": 7,
    "structured-parsing": 7,
    "interpreters": 7,
    "persistent-structures": 7,
    "state-models": 7,
    "state-validation": 7,
    "state-simulation": 7,
    "randomness": 7,
    "refactoring": 8,
    "file-automation": 9,
    "io-protocols": 10,
    "api-models": 10,
    "concurrency": 14,
    "reactive-architecture": 16,
    "security-mathematics": 16,
    "excluded": 17,
}


def phase_for_30days(path: str) -> tuple[int, str]:
    if path.endswith("/numpy.md"):
        return 13, "Alternate duplicate of the Day 24 NumPy lab; keep as a source reference, not a second unlock."
    match = re.search(r"/(\d{2})_Day_", path)
    day = int(match.group(1)) if match else 1
    if day == 30:
        return 17, "Conclusion/outro contains no independent programming assignment."
    if day == 1:
        return 0, ""
    if day <= 4:
        return 1, ""
    if day <= 10:
        return 2 if day >= 9 else 3, ""
    if day <= 14:
        return 4 if day in {11, 12, 14} else 3, ""
    if day <= 19:
        return 5, ""
    if day in {20, 23}:
        return 15, ""
    if day == 21:
        return 6, ""
    if day in {22, 28, 29}:
        return 10 if day in {22, 28} else 12, ""
    if day in {24, 25}:
        return 13, ""
    if day == 26:
        return 12, ""
    if day == 27:
        return 11, ""
    return 17, ""


C1_WEEK_PHASE = {1: 0, 2: 1, 3: 2, 4: 4, 5: 3, 6: 5, 7: 6, 8: 10, 9: 12, 10: 11, 11: 8, 12: 9, 13: 13, 14: 13, 15: 17}


def phase_for_c1(path: str) -> tuple[int, str]:
    match = re.search(r"/week-(\d{2})-", path)
    if match:
        week = int(match.group(1))
        phase = C1_WEEK_PHASE[week]
        # Early C1 mini-projects use functions, annotations, module entrypoints
        # and test scaffolding even when their surrounding week is introductory.
        if week <= 5 and "/mini-project/" in path:
            phase = max(phase, 4)
        return phase, ""
    if "/projects/capstone/" in path:
        return 17, ""
    return 17, "Container/index page; its concrete child projects are already sequenced."


def phase_for_learn(path: str) -> tuple[int, str]:
    if "/level-00-absolute-beginner/" in path:
        match = re.search(r"/(\d{2})-", path)
        number = int(match.group(1)) if match else 1
        if number <= 3:
            return 0, ""
        if number <= 7:
            return 1, ""
        if number == 8 or number in {10, 11}:
            return 2, ""
        if number in {9, 12}:
            return 3, ""
        if number == 13:
            return 4, ""
        if number == 14:
            return 5, ""
        return 5, ""
    level = re.search(r"/level-(\d+)(?:/|-)", path)
    if level:
        number = int(level.group(1))
        return {0: 8, 1: 9, 2: 9, 3: 8, 4: 9, 5: 9, 6: 11, 7: 10, 8: 15, 9: 16, 10: 16}.get(number, 16), ""
    modules = {
        "01-web-scraping": 10,
        "02-cli-tools": 9,
        "03-rest-apis": 10,
        "04-fastapi-web": 12,
        "05-async-python": 14,
        "06-databases-orm": 11,
        "07-data-analysis": 13,
        "08-testing-advanced": 8,
        "09-docker-deployment": 15,
        "10-django-fullstack": 12,
        "11-package-publishing": 15,
        "12-cloud-deploy": 15,
    }
    for slug, phase in modules.items():
        if f"/modules/{slug}/" in path:
            return phase, ""
    if "/elite-track/" in path:
        return 16, ""
    if "/capstones/" in path:
        return 17, ""
    if "/practice/challenges/beginner/" in path:
        filename = Path(path).stem
        if "swap-variables" in filename:
            return 1, ""
        if any(word in filename for word in ("binary-search", "merge-sorted")):
            return 7, ""
        if any(word in filename for word in ("remove-duplicates", "word-frequency", "flatten-list", "matrix", "anagram")):
            return 3, ""
        return 2, ""
    if "/practice/challenges/fill-in/" in path:
        if "class" in path:
            return 6, ""
        if "file" in path or "error" in path:
            return 5, ""
        return 3, ""
    if "/practice/challenges/bug-hunt/" in path:
        return 8, ""
    if "/practice/challenges/intermediate/" in path:
        return 14 if "async" in path else 7, ""
    if "/practice/challenges/advanced/" in path:
        return 14 if any(word in path for word in ("async", "coroutine", "producer")) else 16, ""
    return 16, ""


def source_rank(unit: dict) -> int:
    source = unit["source"]
    kind = unit["kind"]
    if source == "30-Days-Of-Python":
        return 1
    if source == "C1-Code-Crunch-Convos":
        return {"assignment": 2, "project": 5}.get(kind, 5)
    if source == "python-curriculum":
        return {"exercism-concept": 3, "exercism-practice": 3}.get(kind, 3)
    if source == "learn.python":
        return {"beginner-exercise": 0, "challenge": 4, "project": 6}.get(kind, 6)
    return 9


def c1_local_rank(path: str) -> str:
    group = 9
    if "/exercises/" in path:
        group = 0
    elif "/homework/" in path:
        group = 1
    elif "/challenges/" in path:
        group = 2
    elif "/mini-project/" in path:
        group = 3
    return f"{group}:{path}"


def difficulty_for(unit: dict, note: dict[str, str] | None, path: str) -> str:
    if note:
        return note["difficulty"]
    if unit["source"] == "C1-Code-Crunch-Convos":
        if "/exercises/" in path:
            return "guided"
        if "/homework/" in path:
            return "practice"
        if "/challenges/" in path:
            return "challenge"
        return "project"
    if unit["source"] == "30-Days-Of-Python":
        return "lesson + exercises"
    if unit["source"] == "learn.python":
        if "/practice/challenges/beginner/" in path or "/practice/challenges/fill-in/" in path:
            return "practice"
        if "/practice/challenges/bug-hunt/" in path:
            return "debugging practice"
        if "/practice/challenges/intermediate/" in path:
            return "intermediate challenge"
        if "/practice/challenges/advanced/" in path:
            return "advanced challenge"
        if "/advanced/" in path or "/elite-track/" in path:
            return "advanced"
        if "/intermediate/" in path or re.search(r"/level-(?:[5-9]|10)/", path):
            return "intermediate/advanced"
        if "/level-00-" in path:
            return "absolute beginner"
        return "project"
    return unit["kind"].replace("exercism-", "")


def inspect_tasks() -> list[Task]:
    candidates = json.loads((ROOT / "review/candidates.json").read_text(encoding="utf-8"))
    notes = load_notes()
    selected = []
    for unit in candidates:
        allowed = {
            "30-Days-Of-Python": {"day-lesson-and-exercises"},
            "C1-Code-Crunch-Convos": {"assignment", "project"},
            "learn.python": {"project", "beginner-exercise", "challenge"},
            "python-curriculum": {"exercism-concept", "exercism-practice"},
        }
        if unit["kind"] in allowed.get(unit["source"], set()):
            selected.append(unit)

    tasks: list[Task] = []
    for unit in selected:
        relative = unit["path"]
        path = ROOT / relative
        if not path.is_file():
            raise FileNotFoundError(relative)
        text = read_text(path)
        raw = path.read_bytes()
        note = notes.get(relative)
        excluded = ""
        if unit["source"] == "30-Days-Of-Python":
            phase, excluded = phase_for_30days(relative)
        elif unit["source"] == "C1-Code-Crunch-Convos":
            phase, excluded = phase_for_c1(relative)
            if note:
                hint = note["stage_hint"]
                if relative.endswith("challenge-02-environment-audit.md"):
                    phase = 7
                elif hint in {"setup", "environments", "Git-remotes"}:
                    phase = 0
                elif "CLI" in hint:
                    phase = 9
                elif hint in {"debugging", "algorithmic-search", "recursion", "recursion-collections", "hash-search"}:
                    phase = 7
                elif hint == "testing-basics":
                    phase = 8
                else:
                    # Reviewed C1 tasks from weeks 1–5 consistently use
                    # functions/modules even when the exercise topic is more
                    # elementary. Do not put them before those prerequisites.
                    phase = max(phase, 4)
        elif unit["source"] == "python-curriculum" and note:
            phase = NOTE_PHASE.get(note["stage_hint"], 16)
            if note["type"].strip().lower() == "excluded":
                excluded = note["review_note"]
        else:
            phase, excluded = phase_for_learn(relative)
        objective = note["objective"] if note else first_objective(text)
        local_rank = c1_local_rank(relative) if unit["source"] == "C1-Code-Crunch-Convos" else relative
        if unit["source"] == "python-curriculum" and note:
            difficulty_order = {
                "absolute beginner": 0,
                "beginner": 1,
                "beginner plus": 2,
                "intermediate": 3,
                "challenge": 4,
                "advanced": 5,
            }
            slug = unit.get("metadata", {}).get("slug", "")
            chain_order = {
                "resistor-color": 0,
                "resistor-color-duo": 1,
                "resistor-color-trio": 2,
                "resistor-color-expert": 3,
            }.get(slug, 5)
            local_rank = f"{difficulty_order.get(note['difficulty'].strip().lower(), 9)}:{chain_order}:{relative}"
        tasks.append(
            Task(
                path=relative,
                source=unit["source"],
                kind=unit["kind"],
                title=title_for(path, text, unit),
                phase=phase,
                difficulty=difficulty_for(unit, note, relative),
                objective=objective,
                source_rank=source_rank(unit),
                local_rank=local_rank,
                bytes=len(raw),
                sha256=hashlib.sha256(raw).hexdigest(),
                contract_files=companion_count(unit, path),
                excluded_reason=excluded,
            )
        )
    return tasks


def source_label(source: str) -> str:
    return {
        "30-Days-Of-Python": "30 Days",
        "C1-Code-Crunch-Convos": "C1",
        "learn.python": "learn.python",
        "python-curriculum": "Exercism",
    }[source]


def render(tasks: list[Task]) -> str:
    sequenced = [task for task in tasks if not task.excluded_reason]
    excluded = [task for task in tasks if task.excluded_reason]
    sequenced.sort(key=lambda task: (task.phase, task.source_rank, task.local_rank))
    excluded.sort(key=lambda task: task.path)
    grouped: dict[int, list[Task]] = defaultdict(list)
    for task in sequenced:
        grouped[task.phase].append(task)

    source_counts = Counter(task.source for task in sequenced)
    lines = [
        "# Python Curriculum — Verified Learning Order",
        "",
        "> This is the canonical easiest-to-hardest arrangement for Gauntlex integration. Read it top to bottom. Every listed task points to its pinned authored source; solutions and answer keys are deliberately excluded.",
        "",
        "## Audit basis",
        "",
        f"- **{len(tasks)} primary task files inspected**; **{len(sequenced)} assigned** and **{len(excluded)} explicitly withheld/merged**.",
        f"- **{sum(task.contract_files for task in tasks)} local starter, support, and test-contract files read** alongside the primary task files.",
        f"- Sources: {', '.join(f'{source_label(source)} {count}' for source, count in sorted(source_counts.items()))}.",
        "- Each primary source path appears once. Source-native order is retained where tasks build cumulatively; cross-source placement follows prerequisites rather than repository folder order.",
        "- Existing semantic review notes are honored. Generated/template-heavy project tracks are ordered by their declared level, required tooling, baseline contract, and dependency chain.",
        "- A phase is an unlock boundary. Within a phase, complete entries from top to bottom.",
        "",
        "## Difficulty ladder",
        "",
    ]
    for number, title, description in PHASES:
        phase_index = PHASE_BY_NUMBER[number][0]
        lines.append(f"- **{number}. {title}** — {len(grouped[phase_index])} tasks. {description}")
    lines.extend(["", "---", ""])

    sequence = 1
    for phase_index, (number, title, description) in enumerate(PHASES):
        phase_tasks = grouped[phase_index]
        lines.extend([f"## {number} · {title}", "", description, ""])
        current_source = ""
        for task in phase_tasks:
            if task.source != current_source:
                if current_source:
                    lines.append("")
                current_source = task.source
                lines.extend([f"### {source_label(current_source)}", ""])
            display_kind = task.kind.replace("exercism-", "").replace("-", " ")
            lines.append(
                f"{sequence}. **{task.title}** · {display_kind} · {task.difficulty} — "
                f"[{task.path}]({task.path})"
            )
            sequence += 1
        lines.append("")

    lines.extend(["---", "", "## Not assigned as separate unlocks", ""])
    lines.append("These files were inspected, but assigning them separately would duplicate a task, expose a known-broken contract, or create a non-task unlock.")
    lines.append("")
    for task in excluded:
        reason = re.sub(r"\s+", " ", task.excluded_reason).strip()
        lines.append(f"- **{task.title}** — [{task.path}]({task.path}) — {reason}")

    lines.extend(
        [
            "",
            "## Integration rules for Gauntlex",
            "",
            "1. Treat the sequence number as curriculum order, not the source repository's alphabetical order.",
            "2. Preserve authored instructions and starter files. Strip worked solutions, exemplar files, answer sections and hidden-test expectations from learner payloads.",
            "3. Make each phase sequential by default. A task unlocks only after the preceding assigned task passes its server-owned evaluation and audit.",
            "4. Keep project and challenge tasks in the same Python course progress ledger; do not mix them with Go or TypeScript progress.",
            "5. Use the pinned source path as the stable import identity. Titles are display labels and may repeat across sources.",
            "6. Keep the withheld list out of the learner path unless its recorded issue is resolved and reviewed again.",
            "",
            "## Verification footer",
            "",
            f"- Assigned sequence range: **1–{len(sequenced)}**.",
            f"- Unique primary paths: **{len({task.path for task in tasks})}/{len(tasks)}**.",
            f"- Total inspected primary bytes: **{sum(task.bytes for task in tasks):,}**.",
            f"- SHA-256 fingerprints captured during generation: **{len({task.sha256 for task in tasks})} distinct contents**.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    tasks = inspect_tasks()
    if len({task.path for task in tasks}) != len(tasks):
        raise RuntimeError("Duplicate primary task paths detected")
    OUTPUT.write_text(render(tasks), encoding="utf-8")
    print(f"Wrote {OUTPUT.name}: {len(tasks)} inspected task files")


if __name__ == "__main__":
    main()
