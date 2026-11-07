import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        assert module.caesar_cipher("Abc-XYZ!",2) == "Cde-ZAB!"
        assert module.caesar_cipher("B",-1) == "A"
        assert module.caesar_cipher("123",100) == "123"
