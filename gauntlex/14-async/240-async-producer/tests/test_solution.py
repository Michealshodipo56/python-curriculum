import asyncio
import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1] / "starter" / "solution.py"
spec = importlib.util.spec_from_file_location("learner_solution", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_async_contract():
    async def run():
            q = asyncio.Queue()
            assert await module.produce_items(q,[2,4,6]) == 3
            assert [q.get_nowait() for _ in range(3)] == [2,4,6]
    asyncio.run(run())
