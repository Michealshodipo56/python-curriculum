import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        def fail(): raise ValueError("bad")
        assert isinstance(module.assert_raises(ValueError,fail),ValueError)
        with pytest.raises(AssertionError): module.assert_raises(ValueError,lambda: 3)
        with pytest.raises(AssertionError): module.assert_raises(TypeError,fail)
