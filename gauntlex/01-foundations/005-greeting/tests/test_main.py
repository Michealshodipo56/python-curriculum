import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_greeting():
    for name in ("Ada", "Lin", "Grace Hopper"):
        result = subprocess.run([sys.executable, str(ROOT / "starter" / "main.py")], input=name + "\n", text=True, capture_output=True, timeout=3)
        assert result.returncode == 0
        assert result.stdout == f"Hello, {name}!\n"
