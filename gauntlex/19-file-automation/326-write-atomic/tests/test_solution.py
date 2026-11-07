import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract(tmp_path):
        p=tmp_path/"state.txt"
        p.write_text("old",encoding="utf-8")
        assert module.write_text_atomic(p,"new") is None
        assert p.read_text(encoding="utf-8") == "new"
        assert sorted(x.name for x in tmp_path.iterdir()) == ["state.txt"]
