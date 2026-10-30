import importlib.util
import json
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        for incoming,expected in [("abc123","abc123"),("bad value","generated"),("x"*33,"generated")]:
            calls=[]
            module.application({"PATH_INFO":"/request","HTTP_X_REQUEST_ID":incoming},lambda s,h:calls.append((s,h)))
            assert ("X-Request-ID",expected) in calls[0][1]
