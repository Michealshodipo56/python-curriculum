import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        def work():
            print("hello")
            return 5
        assert module.capture_output(work) == [5,"hello\n"]
        with pytest.raises(ValueError): module.capture_output(lambda: (_ for _ in ()).throw(ValueError()))
