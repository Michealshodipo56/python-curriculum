"""Verify Markdown Link Checker acceptance tests against an isolated reference."""
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
TASK = ROOT / "gauntlex/18-capstones/409-markdown-link-checker"
REFERENCE = r'''
import json
from pathlib import Path
import re
import sys
from urllib.parse import urlsplit

LINK = re.compile(r"\[[^\]\n]*\]\(([^\s()]+)\)")

def main():
    if len(sys.argv) != 2:
        return 2
    root = Path(sys.argv[1]).resolve()
    broken = []
    for markdown in sorted(root.rglob("*.md")):
        if not markdown.is_file():
            continue
        relative = markdown.relative_to(root).as_posix()
        for target in LINK.findall(markdown.read_text(encoding="utf-8")):
            if target.startswith("#") or target.lower().startswith(("http:", "https:", "mailto:")):
                continue
            path = urlsplit(target).path
            if not path:
                continue
            candidate = root / path.lstrip("/") if path.startswith("/") else markdown.parent / path
            resolved = candidate.resolve()
            if not resolved.is_relative_to(root) or not resolved.exists():
                broken.append({"file": relative, "target": target})
    broken.sort(key=lambda item: (item["file"], item["target"]))
    print(json.dumps(broken, sort_keys=True, separators=(",", ":")))
    return 1 if broken else 0

if __name__ == "__main__":
    raise SystemExit(main())
'''

def run_suite(folder):
    return subprocess.run([sys.executable, "-m", "pytest", "tests", "-q"],
                          cwd=folder, capture_output=True, text=True, timeout=90)

def main():
    with tempfile.TemporaryDirectory(prefix="gauntlex-links-check-") as temporary:
        folder = Path(temporary)
        (folder / "starter").mkdir()
        shutil.copytree(TASK / "tests", folder / "tests",
                        ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
        target = folder / "starter/main.py"
        target.write_text(REFERENCE, encoding="utf-8")
        result = run_suite(folder)
        print("Reference implementation:")
        print(result.stdout)
        if result.returncode:
            print(result.stderr, file=sys.stderr)
            return 1
        shutil.copy2(TASK / "starter/main.py", target)
        starter = run_suite(folder)
        if starter.returncode == 0:
            print("ERROR: unfinished starter passed acceptance tests", file=sys.stderr)
            return 1
        print("Unfinished starter correctly fails acceptance tests.")
        return 0

if __name__ == "__main__":
    raise SystemExit(main())
