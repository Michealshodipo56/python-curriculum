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


def test_invalid_rows_do_not_reserve_duplicate_ids(tmp_path):
    src = tmp_path / "source.csv"
    dst = tmp_path / "result.jsonl"
    src.write_text(
        "id,name,amount_cents\n"
        "x,First,-5\n"
        "x,Valid,7\n"
        "x,Later,8\n"
        " ,Missing,3\n"
        "y, Other , 0 \n",
        encoding="utf-8",
    )
    r = subprocess.run([sys.executable, str(MAIN), str(src), str(dst)],
                       capture_output=True, text=True, timeout=5)
    assert r.returncode == 0, r.stderr
    assert json.loads(r.stdout) == {"written": 2, "skipped": 3}
    assert [json.loads(line) for line in dst.read_text(encoding="utf-8").splitlines()] == [
        {"id": "x", "name": "Valid", "amount_cents": 7},
        {"id": "y", "name": "Other", "amount_cents": 0},
    ]


def test_missing_cli_arguments(tmp_path):
    r = subprocess.run([sys.executable, str(MAIN)], capture_output=True,
                       text=True, timeout=5)
    assert r.returncode == 2
