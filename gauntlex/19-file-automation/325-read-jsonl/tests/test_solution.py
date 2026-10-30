import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract(tmp_path):
        p=tmp_path/"data.jsonl"
        p.write_text('{"a":1}\n\n[2,3]\n',encoding="utf-8")
        assert module.read_jsonl(p) == [{"a":1},[2,3]]
