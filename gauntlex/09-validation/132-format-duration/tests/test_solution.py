import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_examples():
    assert module.format_duration(3723) == "1:02:03"
    assert module.format_duration(0) == "0:00:00"
    assert module.format_duration(360000) == "100:00:00"
    with pytest.raises(ValueError):
        module.format_duration(-1)
