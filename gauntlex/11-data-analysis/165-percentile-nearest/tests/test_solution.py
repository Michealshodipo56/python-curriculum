import importlib.util
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_examples():
    assert module.nearest_rank_percentile([10, 20, 30, 40], 50) == 20
    assert module.nearest_rank_percentile([10, 20, 30, 40], 100) == 40
    assert module.nearest_rank_percentile([2], 1) == 2
