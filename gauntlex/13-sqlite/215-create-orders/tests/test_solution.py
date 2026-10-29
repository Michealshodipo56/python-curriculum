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
        module.create_orders(conn)
        conn.execute("INSERT INTO orders(user_id,amount) VALUES (?,?)",(1,250))
        assert conn.execute("SELECT amount FROM orders").fetchone()[0] == 250
        with pytest.raises(sqlite3.IntegrityError): conn.execute("INSERT INTO orders(user_id,amount) VALUES (1,-1)")
    finally:
        conn.close()
