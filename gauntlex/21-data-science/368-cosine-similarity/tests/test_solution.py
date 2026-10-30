import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        assert module.cosine_similarity([1,0],[0,1]) == pytest.approx(0)
        assert module.cosine_similarity([1,2],[1,2]) == pytest.approx(1)
        assert module.cosine_similarity([],[]) == 0.0
