import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_exact_output():
    result = subprocess.run([sys.executable, str(ROOT / "starter" / "main.py")], text=True, capture_output=True, timeout=3)
    assert result.returncode == 0
    assert result.stdout == "Hello, world!\\n"
    assert result.stderr == ""
