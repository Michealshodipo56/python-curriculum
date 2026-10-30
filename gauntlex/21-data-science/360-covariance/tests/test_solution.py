import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        assert module.population_covariance([1,2,3],[2,4,6]) == pytest.approx(4/3)
        assert module.population_covariance([1],[5]) == 0
        with pytest.raises(ValueError): module.population_covariance([],[])
