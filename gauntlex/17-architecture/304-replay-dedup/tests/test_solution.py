import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        assert module.replay_unique([{"id":"1","account":"a","delta":5},{"id":"1","account":"a","delta":100},{"id":"2","account":"a","delta":-1}]) == {"a":4}
