import importlib.util
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_examples():
    assert module.product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert module.product_except_self([0, 1, 2]) == [2, 0, 0]
    assert module.product_except_self([]) == []
