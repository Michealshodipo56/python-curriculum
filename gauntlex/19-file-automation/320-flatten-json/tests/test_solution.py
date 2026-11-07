import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract(tmp_path):
        assert module.flatten_json({"a":{"b":2},"c":[1,2]}) == {"a.b":2,"c":[1,2]}
        assert module.flatten_json({"a":{}}) == {"a":{}}
        assert module.flatten_json({}) == {}
