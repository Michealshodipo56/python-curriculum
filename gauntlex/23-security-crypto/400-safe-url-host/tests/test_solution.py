import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        assert module.safe_url_host("https://EXAMPLE.com:443/path") == "example.com"
        with pytest.raises(ValueError): module.safe_url_host("file:///etc/passwd")
        with pytest.raises(ValueError): module.safe_url_host("http://user:pass@example.com")
