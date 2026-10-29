# double_async

## Challenge
Define an async function returning twice its integer input.

## Requirements
- Implement `async def double_async(value)` in `starter/solution.py`.
- Use Python's `asyncio` standard library; no external packages or network access.
- Do not print or block the event loop with synchronous sleeps.
- Preserve the specified ordering and error behavior.

## Hints
A coroutine may return a value without awaiting anything.

## Tests
`python -m pytest tests -q`
