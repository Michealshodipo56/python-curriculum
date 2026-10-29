import importlib.util
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_examples():
    assert module.binary_search([1, 3, 5, 7], 5) == 2
    assert module.binary_search([1, 3, 5], 2) == -1
    assert module.binary_search([], 1) == -1
