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
            async def delayed(value,delay):
                await asyncio.sleep(delay)
                return value
            assert await module.first_completed([delayed("slow",0.1),delayed("fast",0)]) == "fast"
    asyncio.run(run())
