import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASES = [["9 2 10 2\n","2 2 9 10\n"],["-1 -5 0\n","-5 -1 0\n"],["\n","\n"]]


def test_cases():
    for supplied, expected in CASES:
        result = subprocess.run([sys.executable, str(ROOT / "starter" / "main.py")], input=supplied, text=True, capture_output=True, timeout=3)
        assert result.returncode == 0, result.stderr
        assert result.stdout == expected
        assert result.stderr == ""
