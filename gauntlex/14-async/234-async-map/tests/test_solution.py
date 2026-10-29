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
            async def twice(x): return x*2
            assert await module.async_map(twice,[3,1,2]) == [6,2,4]
            assert await module.async_map(twice,[]) == []
    asyncio.run(run())
