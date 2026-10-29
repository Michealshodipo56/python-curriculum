import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        assert module.sort_requirements(["Zed==1.0.0","alpha_pkg==2.0.0"]) == ["alpha_pkg==2.0.0","Zed==1.0.0"]
        assert module.sort_requirements([]) == []
