import importlib.util
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_examples():
    assert module.json_value("{\"a\":1,\"b\":2}", "a") == 1
    assert module.json_value("{\"x\":null}", "x") == None
    assert module.json_value("{}", "z") == None
