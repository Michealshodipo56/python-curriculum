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
        conn.executemany("INSERT INTO orders VALUES (?,?,?)",[(1,7,10),(2,7,15),(3,8,100)])
        assert module.order_total(conn,7) == 25
        assert module.order_total(conn,99) == 0
    finally:
        conn.close()
