import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASES = [["name\n{\"name\":\"Ada\",\"age\":3}\n{\"age\":4}\n{\"name\":null}\n","\"Ada\"\nnull\n"],["x\n{}\n",""]]


def test_cli_cases():
    for supplied, expected in CASES:
        result = subprocess.run([sys.executable, str(ROOT / "starter" / "main.py")], input=supplied, text=True, capture_output=True, timeout=3)
        assert result.returncode == 0, result.stderr
        assert result.stdout == expected
        assert result.stderr == ""
