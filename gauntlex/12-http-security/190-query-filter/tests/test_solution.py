import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_examples():
    assert module.filter_records([{"x": 1, "y": 2}, {"x": 1, "y": 3}, {"x": 2}], {"x": 1}) == [{"x": 1, "y": 2}, {"x": 1, "y": 3}]
    assert module.filter_records([{"a": 1}], {}) == [{"a": 1}]
