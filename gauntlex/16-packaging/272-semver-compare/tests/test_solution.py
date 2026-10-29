import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        assert module.compare_version("1.2.9","1.3.0") == -1
        assert module.compare_version("2.0.0","1.99.99") == 1
        assert module.compare_version("1.0.0","1.0.0") == 0
