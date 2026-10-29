import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASES = [["17\n5\n","Groups: 3\nLeftover: 2\n"],["12\n4\n","Groups: 3\nLeftover: 0\n"],["0\n8\n","Groups: 0\nLeftover: 0\n"]]


def test_cases():
    for supplied, expected in CASES:
        result = subprocess.run([sys.executable, str(ROOT / "starter" / "main.py")], input=supplied, text=True, capture_output=True, timeout=3)
        assert result.returncode == 0, result.stderr
        assert result.stdout == expected
        assert result.stderr == ""
