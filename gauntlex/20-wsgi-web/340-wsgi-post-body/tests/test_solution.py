import importlib.util
import json
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        import io
        calls=[]
        body=b"".join(module.application({"PATH_INFO":"/uppercase","REQUEST_METHOD":"POST","CONTENT_LENGTH":"5","wsgi.input":io.BytesIO(b"helloignored")},lambda s,h:calls.append((s,h))))
        assert body == b"HELLO"
        assert calls[0][0] == "200 OK"
