import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        assert module.cidr_contains("10.0.0.0/8","10.1.2.3") is True
        assert module.cidr_contains("10.0.0.0/8","11.0.0.1") is False
        with pytest.raises(ValueError): module.cidr_contains("invalid","1.2.3.4")
