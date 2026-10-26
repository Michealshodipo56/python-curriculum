"""Print content-bearing packets and log exactly which views were inspected.

Packet views omit repeated navigation and explicit worked-answer sections.
Code contracts are derived from AST bodies, assertions and imports, not names.
"""
from __future__ import annotations
import ast
import hashlib
import json
from pathlib import Path
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]

def brief(text: str, source: str) -> str:
    if source == "C1-Code-Crunch-Convos":
        # Preserve requirements, starter, constraints, outputs, acceptance,
        # stretch and other student work. Answers stay in the original source.
        text = re.sub(r"(?ms)^## The Solution\b.*?(?=^## (?:Acceptance|Stretch|Deliverables|Submission|Exercises|Requirements)|\Z)", "[Worked answer and its explanation omitted from this student-brief view.]\n", text)
        text = re.sub(r"(?ms)^<details>\s*\n<summary>(?:Answer|Solution).*?</details>", "[Folded answer omitted.]", text)
    if source == "learn.python":
        for heading in ["Learn Your Way", "Worked Example", "Related Concepts", "Stuck? Ask AI"]:
            text = re.sub(r"(?ms)^#{2,3} " + re.escape(heading) + r"\b.*?(?=^## |\Z)", "", text)
        text = re.sub(r"(?ms)^\| \[← Prev\].*\Z", "", text)
        text = re.sub(r"(?m)^Home:.*$", "", text)
    return text.strip()

def contract(path: Path) -> str:
    text = path.read_text(encoding="utf-8-sig")
    if "python-curriculum/exercises/" in path.as_posix() and not (path.name.startswith("test_") or path.name.endswith("_test.py")):
        return text
    try: tree = ast.parse(text)
    except SyntaxError: return "SYNTAX ERROR\n" + text
    if path.name.startswith("test_") or path.name.endswith("_test.py") or "tests" in path.parts:
        # Preserve executable test bodies and parametrization values. Printing
        # assertion names alone would hide the actual edge-case expectations.
        class RemoveDiagnosticBoilerplate(ast.NodeTransformer):
            def visit_Assign(self, node):
                if all(isinstance(t, ast.Name) and t.id in {"error_message", "error_msg", "failure_message", "failure_msg"} for t in node.targets): return None
                return self.generic_visit(node)
            def visit_Expr(self, node):
                if isinstance(node.value, ast.Constant) and isinstance(node.value.value, str): return None
                return self.generic_visit(node)
            def visit_Call(self, node):
                node = self.generic_visit(node)
                if isinstance(node.func, ast.Attribute) and node.func.attr.startswith("assert"):
                    node.keywords = [kw for kw in node.keywords if kw.arg != "msg"]
                    node.args = [arg for arg in node.args if not isinstance(arg, ast.Name) or arg.id not in {"error_message", "error_msg", "failure_message", "failure_msg"}]
                return node
        return ast.unparse(RemoveDiagnosticBoilerplate().visit(tree))
    lines = []
    doc = ast.get_docstring(tree)
    if doc: lines.append("MODULE DOC: " + doc)
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            lines.append(ast.unparse(node))
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            if node.name.startswith("test") or isinstance(node, ast.ClassDef) and node.name.startswith("Test"):
                continue
            signature = ast.unparse(node).splitlines()[0]
            lines.append(signature)
            doc = ast.get_docstring(node)
            if doc: lines.append(doc)
        elif isinstance(node, ast.Assert): lines.append("ASSERT " + ast.unparse(node))
        elif isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr.startswith("assert"):
            lines.append("EXPECT " + ast.unparse(node))
        elif isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr in {"raises", "parametrize"}:
            lines.append("CASE " + ast.unparse(node))
    return "\n".join(dict.fromkeys(lines))

def show(unit):
    path = ROOT / unit["path"]
    source = unit["source"]
    print(f"\n===== UNIT {unit['path']} [{unit['kind']}] =====")
    if "metadata" in unit: print("TRACK METADATA", json.dumps(unit["metadata"], ensure_ascii=False))
    if path.exists():
        if path.suffix == ".py": print(path.read_text(encoding="utf-8-sig"))
        else: print(brief(path.read_text(encoding="utf-8-sig"), source))
    else: print("MISSING PRIMARY FILE")
    viewed = [unit["path"]]
    folder = ROOT / unit.get("folder", str(path.parent.relative_to(ROOT)))
    if source == "python-curriculum" and (unit["kind"] == "exercism-practice" or "--introductions" in sys.argv):
        for extra in sorted((folder / ".docs").glob("*.md")):
            if extra != path and extra.name != "hints.md":
                print(f"\nSUPPORT {extra.relative_to(ROOT).as_posix()}\n{extra.read_text(encoding='utf-8-sig')}")
                viewed.append(extra.relative_to(ROOT).as_posix())
    extras = []
    if source == "learn.python" and path.suffix == ".py":
        companion = folder / "TRY_THIS.md"
        if companion.exists(): extras.append(companion)
    if unit["kind"] in {"project", "exercism-concept", "exercism-practice", "beginner-exercise"}:
        extras += sorted(folder.glob("*.py")) + sorted(folder.glob("tests/*.py"))
    for extra in extras:
        if extra == path: continue
        print(f"\nCONTRACT {extra.relative_to(ROOT).as_posix()}\n{contract(extra) if extra.suffix == '.py' else extra.read_text(encoding='utf-8-sig')}")
        viewed.append(extra.relative_to(ROOT).as_posix())
    for name in ["requirements.txt", "pyproject.toml", "docker-compose.yml", "compose.yaml"]:
        extra = folder / name
        if extra.exists():
            print(f"\nCONFIG {extra.relative_to(ROOT).as_posix()}\n{extra.read_text(encoding='utf-8-sig')}")
            viewed.append(extra.relative_to(ROOT).as_posix())
    return {"unit": unit["id"], "view": "student-brief+AST-contracts", "files": viewed, "primary_sha256": hashlib.sha256(path.read_bytes()).hexdigest() if path.exists() else None}

if __name__ == "__main__":
    units = json.loads((ROOT / "review/candidates.json").read_text(encoding="utf-8"))
    source, kind, start, count = sys.argv[1:5]
    selected = [u for u in units if (source == "*" or u["source"] == source) and (kind == "*" or u["kind"] == kind)]
    start, count = int(start), int(count)
    print(f"PACKET {source}/{kind}: {start}:{start+count} of {len(selected)}")
    logs = [show(u) for u in selected[start:start+count]]
    packet_dir = ROOT / "review/.cache/packets"
    packet_dir.mkdir(parents=True, exist_ok=True)
    log_path = packet_dir / f"{source.replace('*', 'all')}-{kind.replace('*', 'all')}-{start}-{count}.json"
    log_path.write_text(json.dumps(logs, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
