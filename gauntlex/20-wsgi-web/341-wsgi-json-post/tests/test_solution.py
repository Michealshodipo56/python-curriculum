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
        for raw,code,expected in [(b'{"a":2,"b":3}',"200 OK",b'{"sum":5}'),(b'{"a":2}',"400 Bad Request",b'{"error":"bad request"}')]:
            calls=[]
            got=b"".join(module.application({"PATH_INFO":"/sum","REQUEST_METHOD":"POST","CONTENT_LENGTH":str(len(raw)),"wsgi.input":io.BytesIO(raw)},lambda s,h:calls.append((s,h))))
            assert got == expected and calls[0][0] == code
