import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_examples():
    import hashlib
    import json
    expected = hashlib.sha256(json.dumps(["GET", "https://example.com", ""], separators=(",", ":")).encode("utf-8")).hexdigest()
    assert module.cache_key("get", "https://example.com", "") == expected
    assert module.cache_key("GET", "https://example.com", "") == expected
    assert module.cache_key("POST", "https://example.com", "") != expected
