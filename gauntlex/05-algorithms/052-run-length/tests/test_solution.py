import importlib.util
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_examples():
    assert module.run_length("aaabb") == [["a", 3], ["b", 2]]
    assert module.run_length("abc") == [["a", 1], ["b", 1], ["c", 1]]
    assert module.run_length("") == []
