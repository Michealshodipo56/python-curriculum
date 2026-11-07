import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        assert module.encode_cursor(0) == "MA"
        assert module.encode_cursor(15) == "MTU"
        with pytest.raises(ValueError): module.encode_cursor(-1)
