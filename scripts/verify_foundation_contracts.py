"""Verify first ten task contracts against private in-memory reference programs.

No reference solution files are written to the learner repository. Each
reference program is executed in a temporary directory by the existing pytest
acceptance tests. This validates test satisfiability, not all edge cases.
"""
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
TASKS = {
    "001-hello": "print('Hello, world!')\n",
    "002-displaynumber": "print(42)\n",
    "003-two-lines": "print('Python')\nprint('Gauntlex')\n",
    "004-addition": "a=int(input())\nb=int(input())\nprint(a+b)\n",
    "005-greeting": "name=input()\nprint(f'Hello, {name}!')\n",
    "006-name-card": "name=input()\ncity=input()\nprint(f'Name: {name}')\nprint(f'City: {city}')\n",
    "007-rectangle": "w=int(input())\nh=int(input())\nprint(f'Area: {w*h}')\nprint(f'Perimeter: {2*(w+h)}')\n",
    "008-remainder": "n=int(input())\ng=int(input())\nprint(f'Groups: {n//g}')\nprint(f'Leftover: {n%g}')\n",
    "009-initials": "first=input()\nlast=input()\nprint(f'{first[0].upper()}.{last[0].upper()}.')\n",
    "010-shout": "print(input().strip().upper())\n",
}


def main():
    with tempfile.TemporaryDirectory(prefix="gauntlex-contracts-") as tmp:
        for task, reference in TASKS.items():
            original = ROOT / "gauntlex" / "01-foundations" / task
            sandbox = Path(tmp) / task
            (sandbox / "starter").mkdir(parents=True)
            shutil.copytree(original / "tests", sandbox / "tests")
            (sandbox / "starter" / "main.py").write_text(reference, encoding="utf-8")
            result = subprocess.run(
                [sys.executable, "-m", "pytest", str(sandbox / "tests"), "-q", "--tb=short"],
                capture_output=True, text=True, timeout=45, cwd=sandbox,
            )
            if result.returncode:
                print(f"FAIL {task}: reference implementation rejected")
                print((result.stdout + result.stderr)[-3000:])
                return 1
            print(f"PASS {task}: reference accepted")
    print("Ten foundational contracts passed private reference verification.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
