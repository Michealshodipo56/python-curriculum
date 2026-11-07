import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        assert module.release_notes("1.0.0",["Fix bug","Add docs"]) == "# Release 1.0.0\n\n- Fix bug\n- Add docs\n"
        assert module.release_notes("1.0.0",[]) == "# Release 1.0.0\n"
