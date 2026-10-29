import json
import os
import subprocess
import sys
from pathlib import Path
import pytest

MAIN = Path(__file__).resolve().parents[1] / "starter" / "main.py"


def test_end_to_end(tmp_path):
        text="INFO|2024-02-29|started\nWARN|2024-02-29|slow|db\nERROR|2023-02-29|invalid date\n"
        result=subprocess.run([sys.executable,str(MAIN)],input=text,text=True,capture_output=True,timeout=5)
        assert result.returncode == 0, result.stderr
        assert json.loads(result.stdout) == {"total":2,"INFO":1,"WARN":1,"ERROR":0,"dates":{"2024-02-29":2}}
