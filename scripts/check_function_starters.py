"""Check that unfinished function starters are rejected by their own tests."""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1] / "gauntlex" / "04-functions"


def main():
    tasks = sorted(ROOT.glob("[0-9][0-9][0-9]-*"))
    for task in tasks:
        result = subprocess.run(
            [sys.executable, "-m", "pytest", str(task / "tests"), "-q", "--tb=short"],
            capture_output=True, text=True, timeout=45,
        )
        output = result.stdout + result.stderr
        if result.returncode != 1 or " failed" not in output or "ERROR " in output:
            print(f"FAIL {task.name}: unexpected starter test result")
            print(output[-2500:])
            return 1
        print(f"PASS {task.name}: incomplete starter rejected")
    print(f"{len(tasks)} unfinished function starters correctly rejected.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
