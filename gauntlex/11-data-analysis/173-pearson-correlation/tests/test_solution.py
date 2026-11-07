import importlib.util
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_examples():
    assert module.pearson_correlation([1, 2, 3], [2, 4, 6]) == 1
    assert module.pearson_correlation([1, 1, 1], [2, 3, 4]) == None
    assert module.pearson_correlation([1, 2, 3], [3, 2, 1]) == -1
