import json
import os
import subprocess
import sys
from pathlib import Path
import pytest

MAIN=Path(__file__).resolve().parents[1]/"starter"/"main.py"

def test_end_to_end(tmp_path):
    src=tmp_path/"in.csv";dst=tmp_path/"out.jsonl"
    src.write_text("id,name,amount_cents\n1, Ada ,50\n2,Bob,-1\n1,Duplicate,99\n3,Lin,0\n")
    r=subprocess.run([sys.executable,str(MAIN),str(src),str(dst)],capture_output=True,text=True,timeout=5)
    assert r.returncode==0,r.stderr
    assert json.loads(r.stdout)=={"written":2,"skipped":2}
    assert [json.loads(x) for x in dst.read_text().splitlines()]==[{"id":"1","name":"Ada","amount_cents":50},{"id":"3","name":"Lin","amount_cents":0}]
