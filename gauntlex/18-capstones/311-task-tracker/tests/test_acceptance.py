import json
import os
import subprocess
import sys
from pathlib import Path
import pytest

MAIN = Path(__file__).resolve().parents[1] / "starter" / "main.py"


def test_end_to_end(tmp_path):
        db = tmp_path / "tasks.db"
        env = dict(os.environ, TASK_DB=str(db))
        def call(*args): return subprocess.run([sys.executable,str(MAIN),*args],capture_output=True,text=True,env=env,timeout=5)
        assert call("add","Write tests").stdout == "1\n"
        assert json.loads(call("list").stdout) == [{"done":False,"id":1,"title":"Write tests"}]
        assert call("done","1").stdout == "ok\n"
        assert json.loads(call("list").stdout)[0]["done"] is True
        assert call("delete","1").stdout == "ok\n"
        assert json.loads(call("list").stdout) == []
