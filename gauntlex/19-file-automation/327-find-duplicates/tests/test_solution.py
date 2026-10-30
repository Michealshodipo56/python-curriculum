import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_contract(tmp_path):
        a=tmp_path/"a";b=tmp_path/"b";c=tmp_path/"c"
        a.write_bytes(b"same");b.write_bytes(b"same");c.write_bytes(b"other")
        import hashlib
        digest=hashlib.sha256(b"same").hexdigest()
        assert module.duplicate_hashes([c,b,a]) == {digest:sorted([str(a),str(b)])}
