import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        assert module.regressions({"a":True,"b":False,"c":True},{"a":False,"b":False,"c":True}) == ["a"]
        assert module.regressions({},{"x":False}) == []
