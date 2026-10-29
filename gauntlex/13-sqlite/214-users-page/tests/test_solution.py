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
        conn.executemany("INSERT INTO users VALUES (?,?,?)",[(1,"A","a"),(2,"B","b"),(3,"C","c")])
        assert module.users_page(conn,2,2) == [[3,"C"]]
        with pytest.raises(ValueError): module.users_page(conn,0,2)
    finally:
        conn.close()
