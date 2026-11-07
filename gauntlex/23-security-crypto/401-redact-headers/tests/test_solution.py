import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        h={"Authorization":"Bearer abc","Content-Type":"text/plain","x-api-key":"secret"}
        assert module.redact_headers(h) == {"Authorization":"[REDACTED]","Content-Type":"text/plain","x-api-key":"[REDACTED]"}
        assert h["Authorization"] == "Bearer abc"
