import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        assert module.valid_ipv4("192.168.0.1") is True
        assert module.valid_ipv4("01.2.3.4") is False
        assert module.valid_ipv4("256.1.1.1") is False
        assert module.valid_ipv4(" 1.2.3.4") is False
