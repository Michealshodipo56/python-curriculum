import importlib.util
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_examples():
    assert module.count_islands([["1", "1", "0"], ["0", "1", "0"], ["0", "0", "1"]]) == 2
    assert module.count_islands([]) == 0
