import importlib.util
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_examples():
    assert module.compact_json({"b": 2, "a": 1}) == "{\"a\":1,\"b\":2}"
    assert module.compact_json([1, 2, 3]) == "[1,2,3]"
