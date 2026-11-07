import importlib.util
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_examples():
    assert module.merge_intervals([[1, 3], [2, 6], [8, 10], [10, 12]]) == [[1, 6], [8, 12]]
    assert module.merge_intervals([]) == []
