import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract(tmp_path):
        assert module.archive_member_safe("dir/file.txt") is True
        assert module.archive_member_safe("../secret") is False
        assert module.archive_member_safe("C:/secret") is False
        assert module.archive_member_safe("dir//file") is False
