import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        assert module.circuit_state(2,3,False) == "closed"
        assert module.circuit_state(3,3,False) == "open"
        assert module.circuit_state(3,3,True) == "half-open"
