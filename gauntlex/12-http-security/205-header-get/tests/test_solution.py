import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_examples():
    assert module.header_get([["X-ID", "1"], ["x-id", "2"]], "X-Id") == "2"
    assert module.header_get([["A", "b"]], "X") == None
