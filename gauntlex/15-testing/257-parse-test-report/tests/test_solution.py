import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        assert module.parse_test_report(["PASS alpha","FAIL beta","PASS gamma","PASS  wrong"]) == {"passed":2,"failed":1}
        assert module.parse_test_report([]) == {"passed":0,"failed":0}
