import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASES = [["2\n","2 x 1 = 2\n2 x 2 = 4\n2 x 3 = 6\n2 x 4 = 8\n2 x 5 = 10\n2 x 6 = 12\n2 x 7 = 14\n2 x 8 = 16\n2 x 9 = 18\n2 x 10 = 20\n"],["-1\n","-1 x 1 = -1\n-1 x 2 = -2\n-1 x 3 = -3\n-1 x 4 = -4\n-1 x 5 = -5\n-1 x 6 = -6\n-1 x 7 = -7\n-1 x 8 = -8\n-1 x 9 = -9\n-1 x 10 = -10\n"]]


def test_cases():
    for supplied, expected in CASES:
        result = subprocess.run([sys.executable, str(ROOT / "starter" / "main.py")], input=supplied, text=True, capture_output=True, timeout=3)
        assert result.returncode == 0, result.stderr
        assert result.stdout == expected
        assert result.stderr == ""
