import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Stack = module.Stack


def test_behavior():
    s = Stack()
    s.push(3)
    s.push(5)
    assert s.peek() == 5
    assert s.pop() == 5
    assert s.pop() == 3
    assert s.is_empty()
    with pytest.raises(IndexError): s.pop()
