import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        assert module.upper_bound([1,2,2,4],2) == 3
        assert module.upper_bound([1,2,2,4],0) == 0
        assert module.upper_bound([],0) == 0
