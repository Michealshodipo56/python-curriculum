import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract(tmp_path):
        p=tmp_path/"records.jsonl"
        assert module.append_jsonl(p,{"b":2,"a":1}) is None
        module.append_jsonl(p,{"x":3})
        assert p.read_text(encoding="utf-8") == '{"a":1,"b":2}\n{"x":3}\n'
