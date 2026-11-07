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
        conn.execute("CREATE TABLE documents(id INTEGER PRIMARY KEY,body TEXT)")
        key = module.store_json(conn,{"b":2,"a":1})
        assert conn.execute("SELECT body FROM documents WHERE id=?",(key,)).fetchone()[0] == '{"a":1,"b":2}'
    finally:
        conn.close()
