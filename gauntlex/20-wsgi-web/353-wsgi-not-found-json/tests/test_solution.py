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
        got=b"".join(module.application({"PATH_INFO":"/missing"},lambda s,h:calls.append((s,h))))
        assert json.loads(got) == {"error":"not found","path":"/missing"}
        assert calls[0][0] == "404 Not Found"
