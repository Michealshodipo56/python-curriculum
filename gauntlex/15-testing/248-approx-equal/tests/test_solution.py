import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        assert module.approx_equal(1,1.01,0.02) is True
        assert module.approx_equal(1,1.1,0.01) is False
        with pytest.raises(ValueError): module.approx_equal(1,1,-1)
