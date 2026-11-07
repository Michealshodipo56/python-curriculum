import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_examples():
    assert module.json_response({"b": 2, "a": 1}) == {"status": 200, "headers": {"content-type": "application/json"}, "body": "{\"a\":1,\"b\":2}"}
