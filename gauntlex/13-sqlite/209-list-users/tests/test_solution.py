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
        conn.executemany("INSERT INTO users(id,name,email) VALUES (?,?,?)",[(3,"C","c@x"),(1,"A","a@x")])
        assert module.list_users(conn) == [[1,"A","a@x"],[3,"C","c@x"]]
    finally:
        conn.close()
