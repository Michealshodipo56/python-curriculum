import importlib.util
import json
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        for method,expected in [("GET",b"ready"),("HEAD",b"")]:
            calls=[]
            got=b"".join(module.application({"PATH_INFO":"/status","REQUEST_METHOD":method},lambda s,h:calls.append((s,h))))
            assert got == expected and calls[0][0] == "200 OK"
