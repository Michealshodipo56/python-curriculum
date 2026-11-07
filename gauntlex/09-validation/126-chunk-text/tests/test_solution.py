import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_examples():
    assert module.chunk_text("abcdef", 2) == ["ab", "cd", "ef"]
    assert module.chunk_text("abc", 5) == ["abc"]
    assert module.chunk_text("", 3) == []
    with pytest.raises(ValueError):
        module.chunk_text("a", 0)
