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


def test_wallet_isolation_and_invalid_amounts(tmp_path):
    env = dict(os.environ, WALLET_DB=str(tmp_path / "wallet.db"))
    def run(*args):
        return subprocess.run([sys.executable, str(MAIN), *args],
                              capture_output=True, text=True, env=env, timeout=5)
    assert run("balance", "unknown").stdout == "0\n"
    assert run("credit", "alice", "10").stdout == "ok\n"
    assert run("credit", "bob", "7").stdout == "ok\n"
    assert run("debit", "bob", "8").stdout == "insufficient\n"
    assert run("credit", "alice", "0").returncode == 2
    assert run("debit", "alice", "-2").returncode == 2
    assert run("credit", "alice", "1.5").returncode == 2
    assert run("balance", "alice").stdout == "10\n"
    assert run("balance", "bob").stdout == "7\n"
    assert [e["delta"] for e in json.loads(run("history", "bob").stdout)] == [7]
