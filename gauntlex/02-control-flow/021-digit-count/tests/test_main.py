import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASES = [["0\n","1\n"],["-1204\n","4\n"],["9\n","1\n"],["100\n","3\n"]]


def test_cases():
    for supplied, expected in CASES:
        result = subprocess.run([sys.executable, str(ROOT / "starter" / "main.py")], input=supplied, text=True, capture_output=True, timeout=3)
        assert result.returncode == 0, result.stderr
        assert result.stdout == expected
        assert result.stderr == ""
