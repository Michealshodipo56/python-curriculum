import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract():
        assert module.dijkstra_distances({"a":[["b",5],["c",1]],"c":[["b",2]],"b":[]},"a") == {"a":0,"b":3,"c":1}
        assert module.dijkstra_distances({},"x") == {"x":0}
        with pytest.raises(ValueError): module.dijkstra_distances({"a":[["b",-1]]},"a")
