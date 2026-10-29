import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
LRUCache = module.LRUCache


def test_behavior():
    c = LRUCache(2)
    c.put("a",1)
    c.put("b",2)
    assert c.get("a") == 1
    c.put("c",3)
    assert c.get("b") is None
    assert c.get("c") == 3
    with pytest.raises(ValueError): LRUCache(0)
