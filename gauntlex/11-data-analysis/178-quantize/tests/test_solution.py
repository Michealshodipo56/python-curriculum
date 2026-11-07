import importlib.util
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_examples():
    assert module.quantize([0.2, 0.7, 1.2], 0.5) == [0, 0.5, 1]
    assert module.quantize([2, 4], 2) == [2, 4]
