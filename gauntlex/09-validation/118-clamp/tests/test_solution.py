import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_examples():
    assert module.clamp(12, 0, 10) == 10
    assert module.clamp(-3, 0, 10) == 0
    assert module.clamp(4, 0, 10) == 4
    with pytest.raises(ValueError):
        module.clamp(4, 10, 0)
