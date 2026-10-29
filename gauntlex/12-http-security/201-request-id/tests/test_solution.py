import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_examples():
    import uuid
    first = module.request_id()
    second = module.request_id()
    assert isinstance(first, str)
    assert str(uuid.UUID(first, version=4)) == first
    assert uuid.UUID(first).version == 4
    assert first != second
