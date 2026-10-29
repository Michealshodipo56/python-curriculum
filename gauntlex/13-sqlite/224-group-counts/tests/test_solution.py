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
        conn.execute("CREATE TABLE events(id INTEGER PRIMARY KEY,category TEXT)")
        conn.executemany("INSERT INTO events VALUES (?,?)",[(1,"b"),(2,"a"),(3,"b"),(4,"a"),(5,"c")])
        assert module.group_counts(conn) == [["a",2],["b",2],["c",1]]
    finally:
        conn.close()
