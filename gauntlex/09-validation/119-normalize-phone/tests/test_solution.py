import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_examples():
    assert module.normalize_phone("+1 (555) 123-4567") == "+15551234567"
    assert module.normalize_phone("080-123 456") == "080123456"
    with pytest.raises(ValueError):
        module.normalize_phone("abc")
