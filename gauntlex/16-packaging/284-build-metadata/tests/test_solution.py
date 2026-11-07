import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        deps = ["requests>=2"]
        result = module.build_metadata("demo","1.0.0",">=3.11",deps)
        assert result == {"name":"demo","version":"1.0.0","requires_python":">=3.11","dependencies":["requests>=2"]}
        deps.append("other")
        assert result["dependencies"] == ["requests>=2"]
