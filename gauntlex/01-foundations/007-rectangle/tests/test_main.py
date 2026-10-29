import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASES = [["4\n3\n","Area: 12\nPerimeter: 14\n"],["1\n9\n","Area: 9\nPerimeter: 20\n"],["12\n5\n","Area: 60\nPerimeter: 34\n"]]


def test_cases():
    for supplied, expected in CASES:
        result = subprocess.run([sys.executable, str(ROOT / "starter" / "main.py")], input=supplied, text=True, capture_output=True, timeout=3)
        assert result.returncode == 0, result.stderr
        assert result.stdout == expected
        assert result.stderr == ""
