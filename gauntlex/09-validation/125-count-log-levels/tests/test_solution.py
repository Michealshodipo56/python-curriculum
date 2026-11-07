import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_examples():
    assert module.count_log_levels(["INFO|2024-01-01|ok", "WARN|2024-01-02|slow", "INFO|2024-01-03|ok", "bad"]) == {"INFO": 2, "WARN": 1, "ERROR": 0}
    assert module.count_log_levels([]) == {"INFO": 0, "WARN": 0, "ERROR": 0}
