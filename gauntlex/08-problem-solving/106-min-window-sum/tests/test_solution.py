import importlib.util
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_examples():
    assert module.min_subarray_len(7, [2, 3, 1, 2, 4, 3]) == 2
    assert module.min_subarray_len(15, [1, 2, 3, 4, 5]) == 5
    assert module.min_subarray_len(100, [1, 2]) == 0
