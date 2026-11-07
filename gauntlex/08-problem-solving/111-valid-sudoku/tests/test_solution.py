import importlib.util
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_examples():
    valid = [["."] * 9 for _ in range(9)]
    valid[0][0] = "5"
    valid[1][1] = "3"
    assert module.valid_sudoku(valid) is True
    bad_row = [row[:] for row in valid]
    bad_row[0][1] = "5"
    assert module.valid_sudoku(bad_row) is False
    bad_box = [row[:] for row in valid]
    bad_box[2][2] = "5"
    assert module.valid_sudoku(bad_box) is False
