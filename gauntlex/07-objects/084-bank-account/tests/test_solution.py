import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
BankAccount = module.BankAccount


def test_behavior():
    a = BankAccount(10)
    a.deposit(5)
    assert a.balance == 15
    a.withdraw(4)
    assert a.balance == 11
    with pytest.raises(ValueError): a.withdraw(12)
    with pytest.raises(ValueError): a.deposit(0)
