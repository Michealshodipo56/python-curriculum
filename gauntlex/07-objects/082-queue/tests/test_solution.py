import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Queue = module.Queue


def test_behavior():
    q = Queue()
    q.enqueue("a")
    q.enqueue("b")
    assert q.dequeue() == "a"
    assert q.dequeue() == "b"
    assert q.is_empty()
    with pytest.raises(IndexError): q.dequeue()
