import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        import base64,re
        token=module.random_token(24)
        assert re.fullmatch(r"[A-Za-z0-9_-]+",token)
        assert len(base64.urlsafe_b64decode(token+"="*((-len(token))%4))) == 24
        with pytest.raises(ValueError): module.random_token(0)
