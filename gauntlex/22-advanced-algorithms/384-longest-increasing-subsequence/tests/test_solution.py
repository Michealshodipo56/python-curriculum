import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        assert module.lis_length([10,9,2,5,3,7,101,18]) == 4
        assert module.lis_length([2,2,2]) == 1
        assert module.lis_length([]) == 0
