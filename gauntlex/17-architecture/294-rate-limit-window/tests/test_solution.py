import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        assert module.rate_limit_allowed([1,2,3],4,3,3) is True
        assert module.rate_limit_allowed([2,3,4],4,3,3) is False
        assert module.rate_limit_allowed([],10,5,0) is False
