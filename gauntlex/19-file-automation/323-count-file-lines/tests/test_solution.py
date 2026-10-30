import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract(tmp_path):
        p=tmp_path/"x.txt"
        p.write_text("a\nb",encoding="utf-8")
        assert module.count_file_lines(p) == 2
        p.write_text("",encoding="utf-8")
        assert module.count_file_lines(p) == 0
