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
        conn.execute("CREATE TABLE sales(id INTEGER PRIMARY KEY,category TEXT,amount INTEGER)")
        conn.executemany("INSERT INTO sales VALUES (?,?,?)",[(1,"books",10),(2,"games",20),(3,"books",15)])
        assert module.revenue_report(conn) == [["books",25],["games",20]]
    finally:
        conn.close()
