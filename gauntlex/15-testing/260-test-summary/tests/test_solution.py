import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        assert module.test_summary([{"status":"pass"},{"status":"skip"},{"status":"pass"}]) == {"pass":2,"fail":0,"skip":1,"total":3}
        assert module.test_summary([]) == {"pass":0,"fail":0,"skip":0,"total":0}
