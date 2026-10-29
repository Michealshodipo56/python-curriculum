import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_examples():
    assert module.build_query({"b": "two words", "a": "1"}) == "a=1&b=two+words"
    assert module.build_query({}) == ""
    assert module.build_query({"q": "a+b"}) == "q=a%2Bb"
