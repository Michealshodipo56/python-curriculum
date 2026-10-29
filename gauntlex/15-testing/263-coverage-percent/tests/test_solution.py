import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        assert module.coverage_percent(3,4) == 75.0
        assert module.coverage_percent(0,0) == 100.0
        with pytest.raises(ValueError): module.coverage_percent(5,4)
