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
        module.create_users(conn)
        conn.execute("INSERT INTO users(name,email) VALUES (?,?)",("Ada","ada@example.com"))
        assert conn.execute("SELECT name FROM users").fetchone()[0] == "Ada"
        module.create_users(conn)
    finally:
        conn.close()
