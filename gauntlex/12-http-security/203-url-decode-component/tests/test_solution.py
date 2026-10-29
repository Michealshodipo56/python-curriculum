import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_examples():
    assert module.decode_component("hello%20world") == "hello world"
    assert module.decode_component("a%2Fb") == "a/b"
    assert module.decode_component("a+b") == "a+b"
