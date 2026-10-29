import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASES = [["3 1 2\n","count=3\nsum=6\nmin=1\nmax=3\n"],["","count=0\nsum=0\n"],["-4\n","count=1\nsum=-4\nmin=-4\nmax=-4\n"]]


def test_cli_cases():
    for supplied, expected in CASES:
        result = subprocess.run([sys.executable, str(ROOT / "starter" / "main.py")], input=supplied, text=True, capture_output=True, timeout=3)
        assert result.returncode == 0, result.stderr
        assert result.stdout == expected
        assert result.stderr == ""
