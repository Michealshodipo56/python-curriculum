import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        assert module.mini_batches([1,2,3,4,5],2) == [[1,2],[3,4],[5]]
        assert module.mini_batches([],3) == []
        with pytest.raises(ValueError): module.mini_batches([1],0)
