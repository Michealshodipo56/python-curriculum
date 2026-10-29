import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        a = {"host":"localhost","port":8000}
        assert module.merge_config(a,{"port":9000,"extra":1}) == {"host":"localhost","port":9000}
        assert a["port"] == 8000
