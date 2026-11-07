import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        assert module.file_manifest([["b.txt",3],["a.txt",5]]) == ["a.txt\t5","b.txt\t3"]
        with pytest.raises(ValueError): module.file_manifest([["../secret",1]])
