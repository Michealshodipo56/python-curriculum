"""Smoke-check the first learner assignments without publishing reference solutions.

The starter files are intentionally incomplete. These tests should fail with
ordinary assertions, not crash during collection. This is NOT a correctness
check against reference implementations.
"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TASKS = [
    "001-hello",
    "002-displaynumber",
    "003-two-lines",
    "004-addition",
    "005-greeting",
    "006-name-card",
    "007-rectangle",
    "008-remainder",
    "009-initials",
    "010-shout",
    "011-next-year",
    "012-even-or-odd",
    "013-larger",
    "014-grade",
    "015-access",
    "016-count",
    "017-sum-range",
    "018-countdown",
]


def main():
    for task in TASKS:
        module = "01-foundations" if int(task[:3]) <= 13 else "02-control-flow"
        tests = ROOT / "gauntlex" / module / task / "tests"
        result = subprocess.run(
            [sys.executable, "-m", "pytest", str(tests), "-q", "--tb=short"],
            capture_output=True, text=True, timeout=45,
            cwd=ROOT,
        )
        output = result.stdout + "\n" + result.stderr
        if result.returncode != 1 or " failed" not in output or "ERROR " in output:
            print(f"{task}: unexpected test outcome (exit {result.returncode})")
            print(output[-2500:])
            return 1
        print(f"{task}: starter correctly rejected")
    print("Eighteen introductory starter-negative checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
