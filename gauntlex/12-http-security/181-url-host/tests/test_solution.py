import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_examples():
    assert module.url_host("https://Example.COM:8443/path") == "example.com"
    assert module.url_host("http://localhost/x") == "localhost"
    with pytest.raises(ValueError):
        module.url_host("ftp://x/a")
