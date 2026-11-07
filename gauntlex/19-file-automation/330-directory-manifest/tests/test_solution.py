import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract(tmp_path):
        (tmp_path/"sub").mkdir()
        (tmp_path/"b.txt").write_text("b")
        (tmp_path/"sub"/"a.txt").write_text("a")
        assert module.directory_manifest(tmp_path) == ["b.txt","sub/a.txt"]
