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
        conn.execute("INSERT INTO users(id,name,email) VALUES (7,'Ada','a@x')")
        assert module.find_user(conn,7) == [7,"Ada","a@x"]
        assert module.find_user(conn,99) is None
    finally:
        conn.close()
