import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        assert module.assert_subset([1,2],[2,1,3]) is None
        with pytest.raises(AssertionError,match="\[4\]"): module.assert_subset([2,4],[2,3])
