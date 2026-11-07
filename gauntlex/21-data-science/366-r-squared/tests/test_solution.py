import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        assert module.r_squared([1,2,3],[1,2,3]) == pytest.approx(1)
        assert module.r_squared([2,2],[2,3]) == 0.0
        assert module.r_squared([2,2],[2,2]) == 1.0
        with pytest.raises(ValueError): module.r_squared([],[])
