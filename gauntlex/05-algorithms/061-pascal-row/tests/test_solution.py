import importlib.util
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_examples():
    assert module.pascal_row(0) == [1]
    assert module.pascal_row(1) == [1, 1]
    assert module.pascal_row(4) == [1, 4, 6, 4, 1]
