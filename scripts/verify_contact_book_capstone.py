"""Verify Contact Book capstone acceptance tests with a separate reference CLI."""
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
TASK = ROOT / "gauntlex/18-capstones/406-contact-book"
REFERENCE = r'''
import json
import os
import sqlite3
import sys

def main():
    args = sys.argv[1:]
    if not args:
        return 2
    command, *values = args
    counts = {"add": 2, "find": 1, "delete": 1, "list": 0}
    if command not in counts or len(values) != counts[command]:
        return 2
    if command == "add" and (not values[0].strip() or not values[1].strip()):
        return 2
    with sqlite3.connect(os.environ.get("CONTACT_DB", "contacts.db")) as db:
        db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT NOT NULL, email TEXT NOT NULL COLLATE NOCASE UNIQUE)")
        if command == "add":
            try:
                db.execute("INSERT INTO contacts (name,email) VALUES (?,?)", tuple(values))
                print("ok")
            except sqlite3.IntegrityError:
                print("exists")
        elif command == "delete":
            result = db.execute("DELETE FROM contacts WHERE email=?", (values[0],))
            print("ok" if result.rowcount else "not found")
        else:
            if command == "list":
                rows = db.execute("SELECT name,email FROM contacts ORDER BY lower(email),email").fetchall()
            else:
                term = values[0].casefold()
                rows = db.execute("SELECT name,email FROM contacts ORDER BY lower(email),email").fetchall()
                rows = [row for row in rows if term in row[0].casefold() or term in row[1].casefold()]
            print(json.dumps([{"name": name, "email": email} for name,email in rows],
                             sort_keys=True, separators=(",", ":")))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
'''

def run_suite(folder):
    return subprocess.run([sys.executable, "-m", "pytest", "tests", "-q"],
                          cwd=folder, capture_output=True, text=True, timeout=90)

def main():
    with tempfile.TemporaryDirectory(prefix="gauntlex-contacts-check-") as temporary:
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
