import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        assert module.cidr_network("192.168.1.42/24") == "192.168.1.0/24"
        assert module.cidr_network("10.1.2.3/32") == "10.1.2.3/32"
        with pytest.raises(ValueError): module.cidr_network("10.0.0.1/33")
