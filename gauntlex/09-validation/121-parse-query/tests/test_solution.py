import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_examples():
    assert module.parse_query("a=1&b=two+words&a=3") == {"a": "3", "b": "two words"}
    assert module.parse_query("x=&y=%2B") == {"x": "", "y": "+"}
    assert module.parse_query("") == {}
