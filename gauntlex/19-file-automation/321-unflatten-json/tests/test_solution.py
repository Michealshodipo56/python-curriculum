import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract(tmp_path):
        assert module.unflatten_json({"a.b":2,"a.c":3,"d":1}) == {"a":{"b":2,"c":3},"d":1}
        assert module.unflatten_json({}) == {}
