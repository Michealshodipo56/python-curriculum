import importlib.util
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_examples():
    assert module.iqr_outliers([1, 2, 2, 3, 3, 4, 5, 6, 100]) == [100]
    assert module.iqr_outliers([1, 2, 3]) == []
