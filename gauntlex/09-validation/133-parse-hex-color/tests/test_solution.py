import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_examples():
    assert module.parse_hex_color("#FF8000") == [255, 128, 0]
    assert module.parse_hex_color("#000000") == [0, 0, 0]
    with pytest.raises(ValueError):
        module.parse_hex_color("#FFF")
