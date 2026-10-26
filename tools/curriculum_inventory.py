"""Inventory source bytes and produce reproducible, content-bearing review packets.

Reading a file here is a machine scan, not a claim of human semantic review.
Semantic review decisions are recorded separately in review/tasks.json.
"""
from __future__ import annotations
import ast
import collections
import hashlib
import json
import os
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ["python-curriculum", "30-Days-Of-Python", "C1-Code-Crunch-Convos", "learn.python"]
AUDIT = ROOT / "review"

def scan():
    records = []
    for source in SOURCES:
        source_paths = []
        for directory, names, files in os.walk(ROOT / source):
            names[:] = sorted(name for name in names if name != ".git")
            source_paths.extend(Path(directory) / name for name in sorted(files))
        print(f"Scanning {source}: {len(source_paths)} files", flush=True)
        for path in source_paths:
            relative = path.relative_to(ROOT)
            if ".git" in relative.parts or not path.is_file():
                continue
            raw = path.read_bytes()
            record = {"path": relative.as_posix(), "source": source, "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest(), "suffix": path.suffix.lower()}
            text = None
            if raw.startswith((b"\xff\xfe", b"\xfe\xff")):
                try: text = raw.decode("utf-16"); record["encoding"] = "utf-16"
                except UnicodeDecodeError: pass
            elif b"\0" not in raw[:8192]:
                try: text = raw.decode("utf-8-sig")
                except UnicodeDecodeError:
                    try: text = raw.decode("cp1252"); record["encoding"] = "cp1252"
                    except UnicodeDecodeError: pass
            record["scan"] = "text" if text is not None else "binary"
            if text is not None:
                record["lines"] = len(text.splitlines())
                record["headings"] = re.findall(r"^#{1,6}\s+(.+)$", text, re.M)
                record["links"] = re.findall(r"\]\(([^)]+)\)", text)
                if path.suffix == ".py":
                    try:
                        tree = ast.parse(text)
                        record["python"] = {"imports": sorted({node.module or "" for node in ast.walk(tree) if isinstance(node, ast.ImportFrom)} | {alias.name for node in ast.walk(tree) if isinstance(node, ast.Import) for alias in node.names}), "definitions": [node.name for node in ast.walk(tree) if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))], "docstrings": [ast.get_docstring(node) for node in ast.walk(tree) if isinstance(node, (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)) and ast.get_docstring(node)], "stub_count": sum(isinstance(node, ast.Pass) or (isinstance(node, ast.Raise) and "NotImplementedError" in ast.unparse(node)) for node in ast.walk(tree))}
                    except SyntaxError as error: record["syntax_error"] = {"line": error.lineno, "message": error.msg}
                if path.suffix in {".json", ".ipynb"}:
                    try:
                        data = json.loads(text)
                        record["json"] = {"type": type(data).__name__, "items": len(data) if isinstance(data, (list, dict)) else 1}
                        if isinstance(data, dict): record["json"]["keys"] = list(data)[:30]
                        if path.suffix == ".ipynb": record["json"]["cells"] = [{"type": cell.get("cell_type"), "source": cell.get("source", [])} for cell in data.get("cells", [])]
                    except ValueError as error: record["json_error"] = str(error)
            records.append(record)
    AUDIT.mkdir(exist_ok=True)
    (AUDIT / "files.json").write_text(json.dumps(records, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    for source in SOURCES:
        rows = [row for row in records if row["source"] == source]
        print(source, json.dumps({"files": len(rows), "bytes": sum(row["bytes"] for row in rows), "types": collections.Counter(row["suffix"] or "[no extension]" for row in rows), "text_bytes": sum(row["bytes"] for row in rows if row["scan"] == "text"), "syntax_errors": [row["path"] for row in rows if "syntax_error" in row]}))

def packet(paths: list[str]):
    for name in paths:
        path = ROOT / name
        print(f"\n===== {name} =====\n")
        text = path.read_text(encoding="utf-8-sig")
        print(text)

if __name__ == "__main__":
    if len(sys.argv) == 1: scan()
    else: packet(sys.argv[1:])
