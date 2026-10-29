import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        assert module.pytest_nodeid(" tests/test_a.py "," test_ok ") == "tests/test_a.py::test_ok"
        with pytest.raises(ValueError): module.pytest_nodeid("","test_x")
