import importlib.util
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_examples(tmp_path):
    path = tmp_path / "sample.json"
    path.write_text('{"ok": true, "count": 3}', encoding="utf-8")
    assert module.read_json_file(str(path)) == {"ok": True, "count": 3}
