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
        conn.execute("CREATE TABLE scores(student TEXT PRIMARY KEY,score INTEGER)")
        module.upsert_score(conn,"Ada",10)
        module.upsert_score(conn,"Ada",20)
        assert conn.execute("SELECT score FROM scores WHERE student='Ada'").fetchone()[0] == 20
    finally:
        conn.close()
