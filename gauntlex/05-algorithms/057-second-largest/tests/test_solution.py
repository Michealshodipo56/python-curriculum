import importlib.util
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_examples():
    assert module.second_largest([3, 1, 3, 2]) == 2
    assert module.second_largest([5, 5]) == None
    assert module.second_largest([-5, -1, -3]) == -3
