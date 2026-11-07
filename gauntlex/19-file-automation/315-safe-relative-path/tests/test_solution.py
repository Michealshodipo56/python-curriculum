import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract(tmp_path):
        assert module.safe_relative_path("a//./b.txt") == "a/b.txt"
        with pytest.raises(ValueError): module.safe_relative_path("../x")
        with pytest.raises(ValueError): module.safe_relative_path("/etc/passwd")
