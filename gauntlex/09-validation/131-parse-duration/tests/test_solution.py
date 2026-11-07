import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_examples():
    assert module.parse_duration("1:02:03") == 3723
    assert module.parse_duration("0:00:05") == 5
    with pytest.raises(ValueError):
        module.parse_duration("1:60:00")
    with pytest.raises(ValueError):
        module.parse_duration("1:2:03")
