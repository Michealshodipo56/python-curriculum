import importlib.util
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_examples():
    assert module.bucket_count([0, 1, 2, 3, 4, 5], 2, 3) == [2, 2, 2]
    assert module.bucket_count([-1, 0, 10], 5, 2) == [1, 0]
