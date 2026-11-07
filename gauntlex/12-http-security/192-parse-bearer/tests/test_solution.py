import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_examples():
    assert module.parse_bearer("Bearer abc123") == "abc123"
    assert module.parse_bearer(" bearer   XYZ ") == "XYZ"
    assert module.parse_bearer("Basic xyz") == None
    assert module.parse_bearer("Bearer") == None
