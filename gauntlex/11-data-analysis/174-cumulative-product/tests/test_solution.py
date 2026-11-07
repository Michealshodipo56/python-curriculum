import importlib.util
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_examples():
    assert module.cumulative_product([2, 3, 4]) == [2, 6, 24]
    assert module.cumulative_product([2, 0, 4]) == [2, 0, 0]
    assert module.cumulative_product([]) == []
