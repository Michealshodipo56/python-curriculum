import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_examples():
    assert module.normalize_url_path("/a//b/./c/../d") == "/a/b/d"
    assert module.normalize_url_path("../../x") == "/x"
    assert module.normalize_url_path("") == "/"
