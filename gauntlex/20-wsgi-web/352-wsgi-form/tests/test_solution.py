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
        raw=b"name=Ada+Lovelace&name=Ignored"
        got=b"".join(module.application({"PATH_INFO":"/form","REQUEST_METHOD":"POST","CONTENT_LENGTH":str(len(raw)),"wsgi.input":io.BytesIO(raw)},lambda s,h:None))
        assert got == b"Ada Lovelace"
