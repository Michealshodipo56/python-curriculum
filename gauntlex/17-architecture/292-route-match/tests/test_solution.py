import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        assert module.match_route("/users/{id}/posts/{post}","/users/42/posts/7") == {"id":"42","post":"7"}
        assert module.match_route("/users/{id}","/users") is None
        assert module.match_route("/health","/health") == {}
