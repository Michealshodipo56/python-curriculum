import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        import hashlib
        expected=hashlib.pbkdf2_hmac("sha256",b"pass",b"salt",100,dklen=32).hex()
        assert module.derive_key("pass","salt",100) == expected
        with pytest.raises(ValueError): module.derive_key("x","y",0)
