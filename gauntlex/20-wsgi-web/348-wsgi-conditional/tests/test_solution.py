import importlib.util
import json
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        for tag,code,body in [("","200 OK",b"version one"),('"v1"',"304 Not Modified",b"")]:
            calls=[]
            got=b"".join(module.application({"PATH_INFO":"/version","HTTP_IF_NONE_MATCH":tag},lambda s,h:calls.append((s,h))))
            assert got == body and calls[0][0] == code
            assert ("ETag",'"v1"') in calls[0][1]
