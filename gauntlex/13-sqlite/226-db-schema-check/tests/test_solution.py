import importlib.util
from pathlib import Path
import sqlite3
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_sqlite_contract():
    conn = sqlite3.connect(":memory:")
    try:
        conn.execute("CREATE TABLE users(id INTEGER)")
        conn.execute("CREATE VIEW user_view AS SELECT * FROM users")
        assert module.table_exists(conn,"users") is True
        assert module.table_exists(conn,"user_view") is False
        assert module.table_exists(conn,"missing") is False
    finally:
        conn.close()
