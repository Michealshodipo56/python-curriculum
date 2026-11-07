import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_examples():
    assert module.parse_status_line("HTTP/1.1 200 OK") == {"status": 200, "reason": "OK"}
    assert module.parse_status_line("HTTP/1.1 404 Not Found") == {"status": 404, "reason": "Not Found"}
    assert module.parse_status_line("HTTP/2 200 OK") == None
