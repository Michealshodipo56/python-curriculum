import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_examples():
    assert module.retry_delay(0, 0.5, 10) == 0.5
    assert module.retry_delay(3, 0.5, 10) == 4
    assert module.retry_delay(10, 1, 8) == 8
