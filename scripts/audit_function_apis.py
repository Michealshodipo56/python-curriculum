"""Check public function names in function-module briefs and learner stubs."""
import ast
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "gauntlex" / "04-functions"


def main():
    failures = []
    for task in sorted(ROOT.glob("[0-9][0-9][0-9]-*")):
        brief = (task / "README.md").read_text(encoding="utf-8")
        match = re.search(r"Implement `([A-Za-z_][A-Za-z_0-9]*)\(", brief)
        if not match:
            failures.append(f"{task.name}: no named function in brief")
            continue
        expected = match.group(1)
        starter = task / "starter" / "solution.py"
        tree = ast.parse(starter.read_text(encoding="utf-8"))
        names = {node.name for node in tree.body if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))}
        if expected not in names:
            failures.append(f"{task.name}: README expects {expected}, starter exports {sorted(names)}")
        tests = (task / "tests" / "test_solution.py").read_text(encoding="utf-8")
        if f"module.{expected}(" not in tests:
            failures.append(f"{task.name}: tests do not invoke {expected}")
    for failure in failures:
        print(failure)
    print(f"Function API audit: {len(list(ROOT.glob('[0-9][0-9][0-9]-*')))} tasks, {len(failures)} issue(s)")
    return bool(failures)


if __name__ == "__main__":
    raise SystemExit(main())
