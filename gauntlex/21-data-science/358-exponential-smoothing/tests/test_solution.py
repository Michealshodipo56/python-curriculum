import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        assert module.exponential_smoothing([10,20,30],0.5) == pytest.approx([10,15,22.5])
        assert module.exponential_smoothing([],0.3) == []
        with pytest.raises(ValueError): module.exponential_smoothing([1],0)
