import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASES = [["{\"active\":true}\n{\"active\":1}\n{\"active\":false}\n","1\n"],["","0\n"],["{\"active\":true}\n\n{\"x\":1}\n","1\n"]]


def test_cli_cases():
    for supplied, expected in CASES:
        result = subprocess.run([sys.executable, str(ROOT / "starter" / "main.py")], input=supplied, text=True, capture_output=True, timeout=3)
        assert result.returncode == 0, result.stderr
        assert result.stdout == expected
        assert result.stderr == ""
