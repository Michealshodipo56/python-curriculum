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
        conn.execute("CREATE TABLE users(id INTEGER PRIMARY KEY,name TEXT NOT NULL,email TEXT NOT NULL UNIQUE)")
        key = module.insert_user(conn,"Ada","ada@example.com")
        assert isinstance(key,int)
        assert conn.execute("SELECT name FROM users WHERE id=?",(key,)).fetchone()[0] == "Ada"
    finally:
        conn.close()
