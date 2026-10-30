import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        assert module.top_k_frequent(["b","a","b","a","c"],2) == ["b","a"]
        assert module.top_k_frequent([1,1,2],0) == []
        with pytest.raises(ValueError): module.top_k_frequent([1],-1)
