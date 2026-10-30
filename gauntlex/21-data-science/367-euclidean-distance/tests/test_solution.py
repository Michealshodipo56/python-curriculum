import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        assert module.euclidean_distance([0,0],[3,4]) == pytest.approx(5)
        assert module.euclidean_distance([],[]) == 0
        with pytest.raises(ValueError): module.euclidean_distance([1],[1,2])
