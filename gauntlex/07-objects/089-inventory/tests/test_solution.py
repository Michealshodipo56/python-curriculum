import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Inventory = module.Inventory


def test_behavior():
    i = Inventory()
    i.stock("pen",5)
    i.sell("pen",2)
    assert i.quantity("pen") == 3
    assert i.quantity("missing") == 0
    with pytest.raises(ValueError): i.sell("pen",4)
