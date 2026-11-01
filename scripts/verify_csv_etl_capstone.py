"""Independently verify the CSV ETL capstone's acceptance tests.

The reference implementation is constructed in a temporary directory and is
never added to learner-facing starter files.
"""
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
TASK = ROOT / "gauntlex/18-capstones/407-csv-etl-pipeline"
REFERENCE = r'''
import csv
import json
import os
from pathlib import Path
import sys
import tempfile

def main():
    if len(sys.argv) != 3:
        return 2
    source, target = Path(sys.argv[1]), Path(sys.argv[2])
    seen = set()
    written = []
    skipped = 0
    with source.open(newline="", encoding="utf-8") as stream:
        for row in csv.DictReader(stream):
            try:
                ident = row["id"].strip()
                name = row["name"].strip()
                raw = row["amount_cents"].strip()
                if not ident or not name or not raw.isascii() or not raw.isdecimal():
                    raise ValueError("invalid row")
                amount = int(raw)
                if ident in seen:
                    raise ValueError("duplicate id")
            except (ValueError, KeyError, AttributeError):
                skipped += 1
                continue
            seen.add(ident)
            written.append({"id": ident, "name": name, "amount_cents": amount})
    target.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", dir=target.parent,
            prefix=".gauntlex-", delete=False
        ) as output:
            temporary = Path(output.name)
            for row in written:
                output.write(json.dumps(row, sort_keys=True, separators=(",", ":")) + "\n")
        os.replace(temporary, target)
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()
    print(json.dumps({"written": len(written), "skipped": skipped},
                     sort_keys=True, separators=(",", ":")))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
'''

def run_suite(folder):
    command = [sys.executable, "-m", "pytest", "tests", "-q"]
    return subprocess.run(command, cwd=folder, capture_output=True, text=True, timeout=90)

def main():
    with tempfile.TemporaryDirectory(prefix="gauntlex-etl-check-") as temporary:
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
            print("ERROR: unfinished starter unexpectedly passes acceptance tests", file=sys.stderr)
            return 1
        print("Unfinished starter correctly fails acceptance tests.")
        return 0

if __name__ == "__main__":
    raise SystemExit(main())
