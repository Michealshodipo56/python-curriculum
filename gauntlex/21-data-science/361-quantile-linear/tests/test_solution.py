import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        assert module.quantile([1,3,5,7],0.25) == pytest.approx(2.5)
        assert module.quantile([5],0.9) == 5
        with pytest.raises(ValueError): module.quantile([],0.5)
