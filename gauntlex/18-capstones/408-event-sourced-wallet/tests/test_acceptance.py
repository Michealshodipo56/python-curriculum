import json
import os
import subprocess
import sys
from pathlib import Path
import pytest

MAIN=Path(__file__).resolve().parents[1]/"starter"/"main.py"

def test_end_to_end(tmp_path):
    env=dict(os.environ,WALLET_DB=str(tmp_path/"wallet.db"))
    def run(*a):return subprocess.run([sys.executable,str(MAIN),*a],capture_output=True,text=True,env=env,timeout=5)
    assert run("credit","alice","500").stdout=="ok\n"
    assert run("debit","alice","700").stdout=="insufficient\n"
    assert run("debit","alice","125").stdout=="ok\n"
    assert run("balance","alice").stdout=="375\n"
    events=json.loads(run("history","alice").stdout)
    assert [e["delta"] for e in events]==[500,-125]
