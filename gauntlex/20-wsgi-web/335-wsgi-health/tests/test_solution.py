import importlib.util
import json
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        calls=[]
        body=b"".join(module.application({},lambda status,headers:calls.append((status,headers))))
        assert body == b'{"status":"ok"}'
        assert calls == [("200 OK",[("Content-Type","application/json")])]
