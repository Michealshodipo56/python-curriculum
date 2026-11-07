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
        conn.execute("CREATE TABLE events(id INTEGER PRIMARY KEY,event_date TEXT)")
        conn.executemany("INSERT INTO events VALUES (?,?)",[(1,"2024-01-01"),(2,"2024-02-01"),(3,"2024-02-01")])
        assert module.events_on_or_after(conn,"2024-02-01") == [[2,"2024-02-01"],[3,"2024-02-01"]]
    finally:
        conn.close()
