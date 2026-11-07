import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Temperature = module.Temperature


def test_behavior():
    t = Temperature(0)
    assert t.celsius == 0
    assert t.fahrenheit == 32
    assert Temperature.from_fahrenheit(212).celsius == 100
