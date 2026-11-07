import importlib.util
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_examples(tmp_path):
    path = tmp_path / "sample.txt"
    path.write_text("one\ntwo\n", encoding="utf-8")
    assert module.count_file_lines(str(path)) == 2
    path.write_text("", encoding="utf-8")
    assert module.count_file_lines(str(path)) == 0
