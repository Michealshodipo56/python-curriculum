import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        assert module.standardize_columns([[1,5],[2,5],[3,5]]) == pytest.approx([[-1.224744871391589,0],[0,0],[1.224744871391589,0]])
        assert module.standardize_columns([]) == []
        with pytest.raises(ValueError): module.standardize_columns([[1,2],[3]])
