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
        conn.execute("CREATE TABLE users(id INTEGER PRIMARY KEY,email TEXT)")
        module.ensure_email_index(conn)
        module.ensure_email_index(conn)
        assert conn.execute("SELECT name FROM sqlite_master WHERE type='index' AND name='idx_users_email'").fetchone() is not None
    finally:
        conn.close()
