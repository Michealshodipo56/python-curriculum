import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        assert module.project_balances([{"id":"1","account":"a","delta":5},{"id":"2","account":"a","delta":-2},{"id":"3","account":"b","delta":0}]) == {"a":3,"b":0}
        assert module.project_balances([]) == {}
