# async_map

## Challenge
Given an async function fn and a sequence of values, run fn(value) for all values concurrently and return results in input order.

## Requirements
- Implement `async def async_map(fn, values)` in `starter/solution.py`.
- Use Python's `asyncio` standard library; no external packages or network access.
- Do not print or block the event loop with synchronous sleeps.
- Preserve the specified ordering and error behavior.

## Hints
Create one coroutine per input and await them together.

## Tests
`python -m pytest tests -q`
