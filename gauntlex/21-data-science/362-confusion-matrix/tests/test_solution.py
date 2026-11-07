import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        assert module.confusion_matrix([True,False,True,False],[True,True,False,False]) == {"tp":1,"tn":1,"fp":1,"fn":1}
        with pytest.raises(ValueError): module.confusion_matrix([True],[])
