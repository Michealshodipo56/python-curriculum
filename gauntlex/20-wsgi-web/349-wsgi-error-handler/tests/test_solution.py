import importlib.util
import json
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        for path,code,body in [("/safe","200 OK",b"ok"),("/crash","500 Internal Server Error",b"internal error")]:
            calls=[]
            got=b"".join(module.application({"PATH_INFO":path},lambda s,h:calls.append((s,h))))
            assert got == body and calls[0][0] == code
