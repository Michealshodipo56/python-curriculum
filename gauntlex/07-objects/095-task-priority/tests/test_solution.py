import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
PriorityTasks = module.PriorityTasks


def test_behavior():
    p = PriorityTasks()
    p.add("low",5)
    p.add("high",1)
    p.add("also high",1)
    assert p.pop() == "high"
    assert p.pop() == "also high"
    assert p.pop() == "low"
    with pytest.raises(IndexError): p.pop()
