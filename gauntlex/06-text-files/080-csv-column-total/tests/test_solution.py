import importlib.util
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_examples(tmp_path):
    path = tmp_path / "sample.csv"
    path.write_text("name,amount\nAda,4\nLin,-2\n", encoding="utf-8")
    assert module.csv_column_total(str(path), "amount") == 2
