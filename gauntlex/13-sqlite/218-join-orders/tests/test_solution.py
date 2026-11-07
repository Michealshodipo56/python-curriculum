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
        conn.execute("CREATE TABLE orders(id INTEGER PRIMARY KEY,user_id INTEGER,amount INTEGER)")
        conn.execute("INSERT INTO users VALUES (1,'Ada','a')")
        conn.executemany("INSERT INTO orders VALUES (?,?,?)",[(3,1,20),(4,99,40)])
        assert module.orders_with_users(conn) == [[3,"Ada",20]]
    finally:
        conn.close()
