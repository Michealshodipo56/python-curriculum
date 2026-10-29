import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_examples():
    assert module.parse_env("A=1\nB = hello world\n# comment\nA=2") == {"A": "2", "B": "hello world"}
    assert module.parse_env("  \n#x") == {}
    with pytest.raises(ValueError):
        module.parse_env("oops")
