import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        assert module.interval_intersection([[1,5],[10,12]],[[3,7],[8,10]]) == [[3,5],[10,10]]
        assert module.interval_intersection([],[[1,2]]) == []
