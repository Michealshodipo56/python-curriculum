import json
import os
import subprocess
import sys
from pathlib import Path
import pytest

MAIN=Path(__file__).resolve().parents[1]/"starter"/"main.py"

def test_end_to_end(tmp_path):
    (tmp_path/"docs").mkdir()
    (tmp_path/"docs"/"ok.txt").write_text("ok")
    (tmp_path/"docs"/"index.md").write_text("[yes](ok.txt) [no](missing.txt) [web](https://example.com) [escape](../../secret.txt)")
    r=subprocess.run([sys.executable,str(MAIN),str(tmp_path)],capture_output=True,text=True,timeout=5)
    assert r.returncode==1,r.stderr
    assert json.loads(r.stdout)==[{"file":"docs/index.md","target":"../../secret.txt"},{"file":"docs/index.md","target":"missing.txt"}]
