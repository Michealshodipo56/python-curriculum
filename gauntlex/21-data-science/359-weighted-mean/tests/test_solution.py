import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        assert module.weighted_mean([10,20],[1,3]) == pytest.approx(17.5)
        with pytest.raises(ValueError): module.weighted_mean([1,2],[0,0])
        with pytest.raises(ValueError): module.weighted_mean([1],[1,2])
