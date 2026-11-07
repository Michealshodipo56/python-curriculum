import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Gradebook = module.Gradebook


def test_behavior():
    g = Gradebook()
    assert g.average("Ada") is None
    g.add_score("Ada",80)
    g.add_score("Ada",100)
    assert g.average("Ada") == 90.0
    with pytest.raises(ValueError): g.add_score("Ada",101)
