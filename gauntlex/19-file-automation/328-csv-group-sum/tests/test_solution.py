import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract(tmp_path):
        p=tmp_path/"data.csv"
        p.write_text("kind,amount\na,3\nb,5\na,-1\n",encoding="utf-8")
        assert module.csv_group_sum(p,"kind","amount") == {"a":2,"b":5}
