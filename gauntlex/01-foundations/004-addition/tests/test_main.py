import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(data):
    return subprocess.run([sys.executable, str(ROOT / "starter" / "main.py")], input=data, text=True, capture_output=True, timeout=3)


def test_positive_numbers():
    result = run("7\n5\n")
    assert result.returncode == 0
    assert result.stdout == "12\n"


def test_negative_numbers():
    result = run("-8\n3\n")
    assert result.returncode == 0
    assert result.stdout == "-5\n"


def test_zero():
    result = run("0\n0\n")
    assert result.returncode == 0
    assert result.stdout == "0\n"
