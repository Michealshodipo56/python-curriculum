import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_examples():
    assert module.safe_filename("My Report (2024)") == "my_report_2024"
    assert module.safe_filename("!!!") == "untitled"
    assert module.safe_filename("A__B") == "a__b"
