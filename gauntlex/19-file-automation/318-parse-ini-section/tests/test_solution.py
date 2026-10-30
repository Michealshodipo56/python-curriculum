import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract(tmp_path):
        text="[app]\nport=8000\n# comment\nname = Demo\n[other]\nport=1\n"
        assert module.parse_ini_section(text,"app") == {"port":"8000","name":"Demo"}
        assert module.parse_ini_section(text,"missing") == {}
