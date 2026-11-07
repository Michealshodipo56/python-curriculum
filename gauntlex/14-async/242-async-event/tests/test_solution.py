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
            event = asyncio.Event()
            async def trigger():
                await asyncio.sleep(0)
                event.set()
            task = asyncio.create_task(trigger())
            assert await module.wait_for_event(event) is True
            await task
    asyncio.run(run())
