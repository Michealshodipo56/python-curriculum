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
    "011-next-year": "name=input()\\nage=int(input())\\nprint(f'{name} will be {age+1} next year.')\\n",
    "012-even-or-odd": "n=int(input())\\nprint('even' if n%2==0 else 'odd')\\n",
    "013-larger": "a=int(input())\\nb=int(input())\\nprint(max(a,b))\\n",
    "014-grade": "n=int(input())\nprint('Grade: '+('A' if n>=90 else 'B' if n>=80 else 'C' if n>=70 else 'D' if n>=60 else 'F'))\n",
    "015-access": "age=int(input())\nstatus=input()\nprint('allowed' if age>=16 and status=='yes' else 'denied')\n",
    "016-count": "n=int(input())\nfor i in range(1,n+1): print(i)\n",
    "017-sum-range": "n=int(input())\nprint(sum(range(1,n+1)))\n",
    "018-countdown": "n=int(input())\nwhile n>0:\n print(n)\n n-=1\nprint('Go!')\n",
    "019-even-sum": "n=int(input())\nprint(sum(i for i in range(1,n+1) if i%2==0))\n",
    "020-multiplication-table": "n=int(input())\nfor i in range(1,11): print(f'{n} x {i} = {n*i}')\n",
    "021-digit-count": "n=int(input())\nprint(len(str(abs(n))))\n",
    "022-number-guess": "while True:\n n=int(input())\n if n==7:\n  print('correct')\n  break\n print('low' if n<7 else 'high')\n",
    "023-list-length": "print(len(input().split()))\n",
    "024-list-ends": "words=input().split()\nprint(words[0])\nprint(words[-1])\n",
    "025-list-total": "print(sum(map(int,input().split())))\n",
    "026-list-maximum": "print(max(map(int,input().split())))\n",
    "027-reverse-words": "print(' '.join(reversed(input().split())))\n",
    "028-filter-even": "nums=map(int,input().split())\nprint(' '.join(str(n) for n in nums if n%2==0))\n",
}


def main():
    with tempfile.TemporaryDirectory(prefix="gauntlex-contracts-") as tmp:
        for task, reference in TASKS.items():
            module = ("01-foundations" if int(task[:3]) <= 13 else
                      "02-control-flow" if int(task[:3]) <= 22 else "03-collections")
            original = ROOT / "gauntlex" / module / task
            sandbox = Path(tmp) / task
            (sandbox / "starter").mkdir(parents=True)
            shutil.copytree(original / "tests", sandbox / "tests")
            (sandbox / "starter" / "main.py").write_text(reference.replace("\\n", "\n"), encoding="utf-8")
            result = subprocess.run(
                [sys.executable, "-m", "pytest", str(sandbox / "tests"), "-q", "--tb=short"],
                capture_output=True, text=True, timeout=45, cwd=sandbox,
            )
            if result.returncode:
                print(f"FAIL {task}: reference implementation rejected")
                print((result.stdout + result.stderr)[-3000:])
                return 1
            print(f"PASS {task}: reference accepted")
    print("Twenty-eight introductory contracts passed private reference verification.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
