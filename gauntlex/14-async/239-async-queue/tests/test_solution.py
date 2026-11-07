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
            for x in [3,1,2]: q.put_nowait(x)
            assert await module.queue_drain(q) == [3,1,2]
            assert q.empty()
    asyncio.run(run())
