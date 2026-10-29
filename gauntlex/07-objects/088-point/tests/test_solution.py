import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Point = module.Point


def test_behavior():
    a = Point(0,0)
    b = Point(3,4)
    assert a.distance_to(b) == 5.0
    with pytest.raises((AttributeError, TypeError)):
        a.x = 9
