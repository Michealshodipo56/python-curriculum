import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        assert module.snapshot_matches({"b":2,"a":[1,2]},{"a":[1,2],"b":2}) is True
        assert module.snapshot_matches([1,2],[2,1]) is False
