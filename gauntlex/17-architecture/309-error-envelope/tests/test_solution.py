import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        d={"field":"email"}
        result=module.error_envelope("bad_request","Invalid",d)
        assert result == {"error":{"code":"bad_request","message":"Invalid","details":{"field":"email"}}}
        d["field"]="changed"
        assert result["error"]["details"]["field"] == "email"
        assert module.error_envelope("x","y",None)["error"]["details"] == {}
