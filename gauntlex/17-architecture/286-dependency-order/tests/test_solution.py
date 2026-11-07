import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        assert module.dependency_order({"deploy":["build"],"build":["test"],"test":[]}) == ["test","build","deploy"]
        assert module.dependency_order({"b":[],"a":[]}) == ["a","b"]
        with pytest.raises(ValueError): module.dependency_order({"a":["b"],"b":["a"]})
