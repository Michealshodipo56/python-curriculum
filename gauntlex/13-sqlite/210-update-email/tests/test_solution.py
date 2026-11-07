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
        conn.execute("CREATE TABLE users(id INTEGER PRIMARY KEY,name TEXT,email TEXT)")
        conn.execute("INSERT INTO users VALUES (1,'Ada','old')")
        assert module.update_email(conn,1,"new") is True
        assert conn.execute("SELECT email FROM users WHERE id=1").fetchone()[0] == "new"
        assert module.update_email(conn,99,"x") is False
    finally:
        conn.close()
