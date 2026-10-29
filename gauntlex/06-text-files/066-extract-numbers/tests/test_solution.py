import importlib.util
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_examples():
    assert module.extract_numbers("a12 b003 c") == [12, 3]
    assert module.extract_numbers("no digits") == []
    assert module.extract_numbers("x9y8") == [9, 8]
