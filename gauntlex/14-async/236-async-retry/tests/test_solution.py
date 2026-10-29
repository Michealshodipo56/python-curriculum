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
            calls = []
            async def flaky():
                calls.append(1)
                if len(calls)<3: raise RuntimeError("retry")
                return 9
            assert await module.retry_async(flaky,3) == 9
            assert len(calls) == 3
            with pytest.raises(ValueError): await module.retry_async(flaky,0)
    asyncio.run(run())
