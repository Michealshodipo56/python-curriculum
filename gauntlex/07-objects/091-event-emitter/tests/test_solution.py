import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
EventEmitter = module.EventEmitter


def test_behavior():
    e = EventEmitter()
    seen = []
    def first(x):
        seen.append(x)
        return x + 1
    e.on("tick",first)
    assert e.emit("tick",3) == [4]
    assert seen == [3]
    e.off("tick",first)
    assert e.emit("tick",5) == []
