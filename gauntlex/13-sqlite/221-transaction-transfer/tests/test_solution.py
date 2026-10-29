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
        conn.execute("CREATE TABLE accounts(id INTEGER PRIMARY KEY,balance INTEGER NOT NULL)")
        conn.executemany("INSERT INTO accounts VALUES (?,?)",[(1,100),(2,20)])
        module.transfer(conn,1,2,30)
        assert conn.execute("SELECT balance FROM accounts ORDER BY id").fetchall() == [(70,),(50,)]
        with pytest.raises(ValueError): module.transfer(conn,1,2,1000)
        assert conn.execute("SELECT balance FROM accounts ORDER BY id").fetchall() == [(70,),(50,)]
    finally:
        conn.close()
