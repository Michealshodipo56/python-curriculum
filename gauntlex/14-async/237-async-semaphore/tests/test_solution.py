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
            active = 0
            peak = 0
            async def worker(x):
                nonlocal active,peak
                active += 1
                peak = max(peak,active)
                await asyncio.sleep(0)
                active -= 1
                return x*3
            assert await module.limited_map(worker,[1,2,3,4],2) == [3,6,9,12]
            assert peak <= 2
            with pytest.raises(ValueError): await module.limited_map(worker,[],0)
    asyncio.run(run())
