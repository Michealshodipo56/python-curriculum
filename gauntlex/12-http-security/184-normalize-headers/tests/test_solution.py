import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_examples():
    assert module.normalize_headers([["Content-Type", " text/plain "], ["X-KEY", " 1 "]]) == {"content-type": "text/plain", "x-key": "1"}
    assert module.normalize_headers([["X", "1"], ["x", "2"]]) == {"x": "2"}
