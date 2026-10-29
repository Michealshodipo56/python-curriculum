import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
CounterMap = module.CounterMap


def test_behavior():
    c = CounterMap()
    assert c.count("x") == 0
    c.add("x")
    c.add("y")
    c.add("x")
    assert c.count("x") == 2
    assert c.count("y") == 1
    assert c.total() == 3
