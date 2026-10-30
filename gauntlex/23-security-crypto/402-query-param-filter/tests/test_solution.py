import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        assert module.filter_query_params("a=1&token=x&a=2",["a"]) == "a=1&a=2"
        assert module.filter_query_params("secret=x",[]) == ""
