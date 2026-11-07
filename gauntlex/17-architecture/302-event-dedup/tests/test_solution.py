import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        events=[{"id":"a","v":1},{"id":"b","v":2},{"id":"a","v":3}]
        assert module.deduplicate_events(events) == [{"id":"a","v":1},{"id":"b","v":2}]
        assert module.deduplicate_events([]) == []
