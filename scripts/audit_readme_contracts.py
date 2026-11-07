"""Check learner-facing assignment contracts against package entrypoints.

This is a static audit: it does not execute unfinished learner programs.
"""
import ast
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "gauntlex"
FUNCTION = re.compile(r"Implement `([A-Za-z_]\w*)\([^\n`]*\)`")
REQUIRED = ("## Description", "## Requirements", "## Tips")


def main():
    problems = []
    checked = 0
    for readme in sorted(ROOT.glob("*/[0-9][0-9][0-9]-*/README.md")):
        task = readme.parent
        checked += 1
        content = readme.read_text(encoding="utf-8")
        meta = json.loads((task / "metadata.json").read_text(encoding="utf-8"))
        for heading in REQUIRED:
            if heading not in content:
                problems.append(f"{task.name}: missing {heading}")
        if not any(h in content for h in ("## Example Behavior", "## Example Input", "## Example Output", "## Deliverables")):
            problems.append(f"{task.name}: missing example or deliverable")
        entry = task / meta["entrypoint"]
        if not entry.exists():
            problems.append(f"{task.name}: missing entrypoint {meta['entrypoint']}")
            continue
        try:
            tree = ast.parse(entry.read_text(encoding="utf-8"))
        except SyntaxError as exc:
            problems.append(f"{task.name}: starter syntax error {exc}")
            continue
        declared = set(FUNCTION.findall(content))
        defined = {node.name for node in ast.walk(tree) if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))}
        for name in declared - defined:
            problems.append(f"{task.name}: README specifies {name} but starter does not define it")
    print(f"README contract audit: {checked} challenges; {len(problems)} issue(s)")
    for issue in problems:
        print(issue)
    return int(bool(problems))


if __name__ == "__main__":
    raise SystemExit(main())
