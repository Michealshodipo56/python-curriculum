import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_examples():
    assert module.constant_time_compare("abc", "abc") == True
    assert module.constant_time_compare("abc", "abd") == False
    assert module.constant_time_compare("é", "é") == True
