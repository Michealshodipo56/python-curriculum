import importlib.util
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_examples():
    assert module.minmax_normalize([2, 4, 6]) == [0, 0.5, 1]
    assert module.minmax_normalize([3, 3]) == [0, 0]
    assert module.minmax_normalize([]) == []
