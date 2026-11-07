import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_examples():
    assert module.parse_log_line("INFO|2024-02-29|Started|ok") == {"level": "INFO", "date": "2024-02-29", "message": "Started|ok"}
    assert module.parse_log_line("DEBUG|2024-01-01|x") == None
    assert module.parse_log_line("ERROR|2023-02-29|bad") == None
