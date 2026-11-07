import json
import os
import subprocess
import sys
from pathlib import Path
import pytest

MAIN = Path(__file__).resolve().parents[1] / "starter" / "main.py"


def test_end_to_end(tmp_path):
        db=tmp_path/"expenses.db"
        env=dict(os.environ,EXPENSE_DB=str(db))
        def call(*args): return subprocess.run([sys.executable,str(MAIN),*args],capture_output=True,text=True,env=env,timeout=5)
        assert call("add","food","250").stdout == "1\n"
        assert call("add","food","150").stdout == "2\n"
        assert json.loads(call("summary").stdout) == {"food":400}
        assert json.loads(call("list").stdout) == [{"amount_cents":250,"category":"food","id":1},{"amount_cents":150,"category":"food","id":2}]
        assert call("add","food","0").returncode == 2
        assert json.loads(call("summary").stdout) == {"food":400}
