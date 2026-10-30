import json
import os
import subprocess
import sys
from pathlib import Path
import pytest

MAIN=Path(__file__).resolve().parents[1]/"starter"/"main.py"

def test_end_to_end(tmp_path):
    env=dict(os.environ,INVENTORY_DB=str(tmp_path/"inv.db"))
    def run(*a):return subprocess.run([sys.executable,str(MAIN),*a],capture_output=True,text=True,env=env,timeout=5)
    assert run("add","book","3").stdout=="ok\n"
    assert run("add","book","3").stdout=="exists\n"
    assert run("adjust","book","-4").stdout=="insufficient\n"
    assert run("adjust","book","-2").stdout=="ok\n"
    assert json.loads(run("get","book").stdout)=={"sku":"book","quantity":1}
    assert json.loads(run("list").stdout)==[{"sku":"book","quantity":1}]
