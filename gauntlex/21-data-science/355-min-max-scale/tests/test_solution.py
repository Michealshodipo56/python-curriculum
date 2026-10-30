import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        assert module.min_max_scale([2,4,6]) == pytest.approx([0,0.5,1])
        assert module.min_max_scale([7,7]) == [0,0]
        assert module.min_max_scale([]) == []
