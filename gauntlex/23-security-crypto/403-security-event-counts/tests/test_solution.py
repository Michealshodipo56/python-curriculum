import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        events=[{"type":"login","severity":"low"},{"type":"login","severity":"low"},{"type":"block","severity":"high"}]
        assert module.security_event_counts(events) == {"low":{"login":2},"high":{"block":1}}
        assert module.security_event_counts([]) == {}
