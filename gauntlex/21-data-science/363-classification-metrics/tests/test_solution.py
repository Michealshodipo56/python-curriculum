import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        result=module.classification_metrics(3,5,1,1)
        assert result == pytest.approx({"precision":0.75,"recall":0.75,"accuracy":0.8,"f1":0.75})
        assert module.classification_metrics(0,0,0,0) == {"precision":0.0,"recall":0.0,"accuracy":0.0,"f1":0.0}
