import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASES = [["100\n","Grade: A\n"],["90\n","Grade: A\n"],["89\n","Grade: B\n"],["70\n","Grade: C\n"],["60\n","Grade: D\n"],["0\n","Grade: F\n"]]


def test_cases():
    for supplied, expected in CASES:
        result = subprocess.run([sys.executable, str(ROOT / "starter" / "main.py")], input=supplied, text=True, capture_output=True, timeout=3)
        assert result.returncode == 0, result.stderr
        assert result.stdout == expected
        assert result.stderr == ""
