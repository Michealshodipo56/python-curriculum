import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_examples():
    assert module.dedupe_normalized(["  Ada ", "ada", "BOB", "bob", "  "]) == ["ada", "bob"]
    assert module.dedupe_normalized([]) == []
