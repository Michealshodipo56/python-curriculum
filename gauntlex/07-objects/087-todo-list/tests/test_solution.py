import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
TodoList = module.TodoList


def test_behavior():
    t = TodoList()
    t.add("  read  ")
    t.add("code")
    assert t.pending() == ["read","code"]
    t.complete(0)
    assert t.pending() == ["code"]
    assert t.completed() == ["read"]
    with pytest.raises(IndexError): t.complete(8)
