import importlib.util
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_examples():
    assert module.move_zeros([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
    assert module.move_zeros([0, 0]) == [0, 0]
    assert module.move_zeros([2, -1]) == [2, -1]
