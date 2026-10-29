import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Rectangle = module.Rectangle


def test_behavior():
    r = Rectangle(3,4)
    assert r.area() == 12
    assert r.perimeter() == 14
    with pytest.raises(ValueError): Rectangle(0,2)
