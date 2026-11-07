import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract(tmp_path):
        data={"user":{"name":"Ada","age":0}}
        assert module.json_path_get(data,"user.name") == "Ada"
        assert module.json_path_get(data,"user.missing") is None
        assert module.json_path_get(data,"") is data
