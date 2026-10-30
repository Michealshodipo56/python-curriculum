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
        body=b"".join(module.application({"PATH_INFO":"/data"},lambda s,h:calls.append((s,h))))
        assert body == b'{"name":"Gauntlex","ready":true}'
        assert calls[0][0] == "200 OK"
        assert ("Content-Type","application/json") in calls[0][1]
