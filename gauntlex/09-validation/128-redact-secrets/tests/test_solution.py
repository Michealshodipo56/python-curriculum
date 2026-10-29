import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_examples():
    assert module.redact_secrets("token=abc password=123") == "token=[REDACTED] password=[REDACTED]"
    assert module.redact_secrets("TOKEN=x") == "TOKEN=[REDACTED]"
    assert module.redact_secrets("no secrets") == "no secrets"
