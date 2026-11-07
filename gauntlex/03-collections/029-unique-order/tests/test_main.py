import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASES = [["a b a c b\n","a b c\n"],["A a A\n","A a\n"],["\n","\n"]]


def test_cases():
    for supplied, expected in CASES:
        result = subprocess.run([sys.executable, str(ROOT / "starter" / "main.py")], input=supplied, text=True, capture_output=True, timeout=3)
        assert result.returncode == 0, result.stderr
        assert result.stdout == expected
        assert result.stderr == ""
