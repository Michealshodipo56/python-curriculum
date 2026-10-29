import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        assert module.has_permission({"admin":["read","write"],"viewer":["read"]},["viewer"],"write") is False
        assert module.has_permission({"admin":["write"]},["admin"],"write") is True
