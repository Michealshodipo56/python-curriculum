# Concurrent Transformation

## Description
Apply an asynchronous operation to many inputs concurrently while preserving their order.

### Behavior contract
Given an async function fn and a sequence of values, run fn(value) for all values concurrently and return results in input order.

## Requirements
- Implement `async def async_map(fn, values)` in `starter/solution.py`.
- Use Python's `asyncio` standard library; no external packages or network access.
- Do not print or block the event loop with synchronous sleeps.
- Preserve the specified ordering and error behavior.

## Tips
Concurrency need not change the order of the final output.

No implementation is provided; reason about scheduling and return values.
