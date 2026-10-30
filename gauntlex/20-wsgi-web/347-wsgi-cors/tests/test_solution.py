import importlib.util
import json
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        for origin,allowed in [("https://gauntlex.example",True),("https://evil-gauntlex.example",False)]:
            calls=[]
            module.application({"PATH_INFO":"/public","HTTP_ORIGIN":origin},lambda s,h:calls.append((s,h)))
            assert (("Access-Control-Allow-Origin","https://gauntlex.example") in calls[0][1]) is allowed
