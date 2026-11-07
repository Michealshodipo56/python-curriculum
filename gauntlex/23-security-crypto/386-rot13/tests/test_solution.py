import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        assert module.rot13("Hello, World!") == "Uryyb, Jbeyq!"
        assert module.rot13(module.rot13("Python 3")) == "Python 3"
