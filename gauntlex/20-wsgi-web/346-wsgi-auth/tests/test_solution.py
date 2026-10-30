import importlib.util
import json
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        for header,code,body in [("Bearer secret-token","200 OK",b"welcome"),("Bearer bad","401 Unauthorized",b"unauthorized")]:
            calls=[]
            got=b"".join(module.application({"PATH_INFO":"/private","HTTP_AUTHORIZATION":header},lambda s,h:calls.append((s,h))))
            assert got == body and calls[0][0] == code
