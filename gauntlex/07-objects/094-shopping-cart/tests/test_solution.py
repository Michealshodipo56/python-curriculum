import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
ShoppingCart = module.ShoppingCart


def test_behavior():
    c = ShoppingCart()
    c.add("pen",2.5,2)
    c.add("pen",2.5,1)
    assert c.total() == 7.5
    c.remove("pen")
    assert c.total() == 0
    with pytest.raises(KeyError): c.remove("pen")
