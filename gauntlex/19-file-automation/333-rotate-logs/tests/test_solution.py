import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract(tmp_path):
        assert module.rotation_names("app.log",3) == ["app.log.1","app.log.2","app.log.3"]
        with pytest.raises(ValueError): module.rotation_names("app.log",0)
