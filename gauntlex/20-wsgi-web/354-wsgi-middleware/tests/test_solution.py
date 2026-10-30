import importlib.util
import json
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        def inner(environ,start_response):
            start_response("200 OK",[("Content-Type","text/plain")])
            return [b"hello"]
        calls=[]
        wrapped=module.wrap_app(inner)
        assert b"".join(wrapped({},lambda s,h:calls.append((s,h)))) == b"hello"
        assert calls == [("200 OK",[("Content-Type","text/plain"),("X-Powered-By","Gauntlex")])]
