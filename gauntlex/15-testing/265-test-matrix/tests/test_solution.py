import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        assert module.test_matrix({"linux":{"a":True,"b":False},"windows":{"a":False,"b":True}}) == ["a","b"]
        assert module.test_matrix({}) == []
