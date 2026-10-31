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


def test_missing_stock_and_invalid_quantities(tmp_path):
    env = dict(os.environ, INVENTORY_DB=str(tmp_path / "inventory.db"))
    def run(*args):
        return subprocess.run([sys.executable, str(MAIN), *args],
                              capture_output=True, text=True, env=env, timeout=5)
    assert run("get", "unknown").stdout == "null\n"
    assert json.loads(run("list").stdout) == []
    assert run("adjust", "unknown", "1").stdout == "not found\n"
    assert run("add", "pen", "-1").returncode == 2
    assert run("add", "pen", "not-a-number").returncode == 2
    assert run("add", "pen", "0").stdout == "ok\n"
    assert run("adjust", "pen", "-1").stdout == "insufficient\n"
    assert json.loads(run("get", "pen").stdout)["quantity"] == 0


def test_inventory_persists_and_lists_by_sku(tmp_path):
    env = dict(os.environ, INVENTORY_DB=str(tmp_path / "inventory.db"))
    def run(*args):
        return subprocess.run([sys.executable, str(MAIN), *args],
                              capture_output=True, text=True, env=env, timeout=5)
    assert run("add", "zeta", "2").stdout == "ok\n"
    assert run("add", "alpha", "1").stdout == "ok\n"
    assert [item["sku"] for item in json.loads(run("list").stdout)] == ["alpha", "zeta"]
