import importlib.util
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_examples():
    assert module.linear_regression([1, 2, 3], [2, 4, 6]) == [2, 0]
    assert module.linear_regression([1, 1], [2, 3]) == None
