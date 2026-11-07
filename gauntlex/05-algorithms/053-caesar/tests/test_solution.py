import importlib.util
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_examples():
    assert module.caesar("Abc-Z!", 2) == "Cde-B!"
    assert module.caesar("xyz", 3) == "abc"
    assert module.caesar("Hello", 0) == "Hello"
