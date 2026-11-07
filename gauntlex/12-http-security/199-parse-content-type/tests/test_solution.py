import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_examples():
    assert module.media_type("Application/JSON; charset=utf-8") == "application/json"
    assert module.media_type("text/plain") == "text/plain"
    assert module.media_type("") == ""
