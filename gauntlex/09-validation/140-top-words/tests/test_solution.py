import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_examples():
    assert module.top_words("Red red blue!", 2) == ["red", "blue"]
    assert module.top_words("b a b a", 1) == ["a"]
    assert module.top_words("", 3) == []
