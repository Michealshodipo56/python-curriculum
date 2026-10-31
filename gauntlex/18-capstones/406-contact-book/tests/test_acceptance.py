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


def test_contact_sorting_and_search_by_email(tmp_path):
    env = dict(os.environ, CONTACT_DB=str(tmp_path / "contacts.db"))
    def run(*args):
        return subprocess.run([sys.executable, str(MAIN), *args],
                              capture_output=True, text=True, env=env, timeout=5)
    assert run("add", "Zed", "Z@Example.org").stdout == "ok\n"
    assert run("add", "Amy", "a@example.org").stdout == "ok\n"
    assert [c["name"] for c in json.loads(run("list").stdout)] == ["Amy", "Zed"]
    assert [c["name"] for c in json.loads(run("find", "EXAMPLE.ORG").stdout)] == ["Amy", "Zed"]
    assert run("delete", "missing@example.org").stdout == "not found\n"
    assert run("add", "", "blank@example.org").returncode == 2
    assert run("add", "Nobody", "").returncode == 2
    assert len(json.loads(run("list").stdout)) == 2
