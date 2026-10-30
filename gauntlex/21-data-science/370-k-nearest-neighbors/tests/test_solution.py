import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        assert module.nearest_indices([[1,1],[3,3],[0,0]],[1,0],2) == [0,2]
        assert module.nearest_indices([],[],3) == []
        with pytest.raises(ValueError): module.nearest_indices([[1,2]],[1],1)
