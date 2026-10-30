import json
import os
import subprocess
import sys
from pathlib import Path
import pytest

MAIN=Path(__file__).resolve().parents[1]/"starter"/"main.py"

def test_end_to_end(tmp_path):
    env=dict(os.environ,CONTACT_DB=str(tmp_path/"contacts.db"))
    def run(*a):return subprocess.run([sys.executable,str(MAIN),*a],capture_output=True,text=True,env=env,timeout=5)
    assert run("add","Ada Lovelace","Ada@Example.com").stdout=="ok\n"
    assert run("add","Other","ada@example.com").stdout=="exists\n"
    assert json.loads(run("find","LOVE").stdout)==[{"name":"Ada Lovelace","email":"Ada@Example.com"}]
    assert run("delete","ADA@example.com").stdout=="ok\n"
    assert json.loads(run("list").stdout)==[]
