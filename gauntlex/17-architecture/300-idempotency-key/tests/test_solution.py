import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        import hashlib,json
        expected=hashlib.sha256(json.dumps(["POST","/pay","{}"],separators=(",",":")).encode()).hexdigest()
        assert module.idempotency_key("post","/pay","{}") == expected
        assert module.idempotency_key("POST","/pay","{}") == expected
