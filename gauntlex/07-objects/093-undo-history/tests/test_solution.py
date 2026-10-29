import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
UndoHistory = module.UndoHistory


def test_behavior():
    h = UndoHistory(1)
    h.set(2)
    h.set(3)
    assert h.current == 3
    assert h.undo() == 2
    assert h.undo() == 1
    with pytest.raises(IndexError): h.undo()
