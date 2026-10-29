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
            observed = []
            async def work(x):
                observed.append(x)
                await asyncio.sleep(0)
                return x+1
            assert await module.async_batches(work,[1,2,3,4,5],2) == [2,3,4,5,6]
            assert observed == [1,2,3,4,5]
            with pytest.raises(ValueError): await module.async_batches(work,[],0)
    asyncio.run(run())
