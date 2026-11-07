import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        import hashlib
        expected=int.from_bytes(hashlib.sha256(b"alice").digest(),"big")%8
        assert module.partition_key("alice",8) == expected
        with pytest.raises(ValueError): module.partition_key("alice",0)
