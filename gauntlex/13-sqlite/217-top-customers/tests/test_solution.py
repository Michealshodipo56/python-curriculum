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
        conn.execute("CREATE TABLE orders(id INTEGER PRIMARY KEY,user_id INTEGER,amount INTEGER)")
        conn.executemany("INSERT INTO orders VALUES (?,?,?)",[(1,2,10),(2,1,5),(3,1,5),(4,3,1)])
        assert module.top_customers(conn,2) == [[1,10],[2,10]]
        assert module.top_customers(conn,0) == []
    finally:
        conn.close()
