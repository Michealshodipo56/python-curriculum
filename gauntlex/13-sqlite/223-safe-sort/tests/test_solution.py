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
        conn.executemany("INSERT INTO users VALUES (?,?,?)",[(1,"Bob","b"),(2,"Ada","a")])
        assert module.sorted_users(conn,"name","ASC") == [[2,"Ada"],[1,"Bob"]]
        with pytest.raises(ValueError): module.sorted_users(conn,"email; DROP TABLE users","asc")
    finally:
        conn.close()
