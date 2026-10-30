import importlib.util
import json
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        for path,method,code,body in [("/resource","GET","200 OK",b"resource"),("/resource","POST","405 Method Not Allowed",b"method not allowed"),("/missing","GET","404 Not Found",b"not found")]:
            calls=[]
            got=b"".join(module.application({"PATH_INFO":path,"REQUEST_METHOD":method},lambda s,h:calls.append((s,h))))
            assert got == body and calls[0][0] == code
