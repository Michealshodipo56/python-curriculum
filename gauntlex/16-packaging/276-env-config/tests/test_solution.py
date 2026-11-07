import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        assert module.read_config({}) == {"debug":False,"port":8000}
        assert module.read_config({"DEBUG":"YES","PORT":"8080"}) == {"debug":True,"port":8080}
        with pytest.raises(ValueError): module.read_config({"PORT":"70000"})
