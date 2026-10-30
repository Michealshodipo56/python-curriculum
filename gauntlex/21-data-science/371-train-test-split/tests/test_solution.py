import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        assert module.train_test_split([1,2,3,4,5],0.4) == [[1,2,3],[4,5]]
        assert module.train_test_split([],0.5) == [[],[]]
        with pytest.raises(ValueError): module.train_test_split([1],1.2)
