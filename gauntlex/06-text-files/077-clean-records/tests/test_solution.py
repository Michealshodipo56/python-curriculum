import importlib.util
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_examples():
    assert module.clean_records([{"name": " Ada ", "age": 3}, {"name": " "}, {"age": 4}]) == [{"name": "Ada", "age": 3}]
    assert module.clean_records([]) == []
