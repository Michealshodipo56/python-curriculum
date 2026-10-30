import importlib.util
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_examples():
    assert module.is_prime(2) == True
    assert module.is_prime(17) == True
    assert module.is_prime(1) == False
    assert module.is_prime(21) == False
