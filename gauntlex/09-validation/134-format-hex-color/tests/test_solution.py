import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_examples():
    assert module.format_hex_color(255, 128, 0) == "#FF8000"
    assert module.format_hex_color(0, 0, 0) == "#000000"
    with pytest.raises(ValueError):
        module.format_hex_color(256, 0, 0)
