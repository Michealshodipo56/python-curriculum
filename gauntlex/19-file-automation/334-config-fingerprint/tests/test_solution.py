import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract(tmp_path):
        assert module.config_fingerprint({"b":2,"a":1}) == module.config_fingerprint({"a":1,"b":2})
        assert len(module.config_fingerprint({})) == 64
