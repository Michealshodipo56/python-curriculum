import importlib.util
import json
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        for cookie,expected in [("theme=dark; session=abc",b"seen"),("session=",b"missing"),("other=x",b"missing")]:
            got=b"".join(module.application({"PATH_INFO":"/cookie","HTTP_COOKIE":cookie},lambda s,h:None))
            assert got == expected
