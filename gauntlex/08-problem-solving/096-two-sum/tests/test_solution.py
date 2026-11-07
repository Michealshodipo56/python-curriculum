import importlib.util
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_examples():
    assert module.two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert module.two_sum([3, 3], 6) == [0, 1]
    assert module.two_sum([1, 2, 3], 9) == []
