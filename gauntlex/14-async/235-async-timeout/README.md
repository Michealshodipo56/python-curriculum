# with_timeout

## Challenge
Await an awaitable with a timeout in seconds; return its result or propagate asyncio.TimeoutError when exceeded.

## Requirements
- Implement `async def with_timeout(awaitable, seconds)` in `starter/solution.py`.
- Use Python's `asyncio` standard library; no external packages or network access.
- Do not print or block the event loop with synchronous sleeps.
- Preserve the specified ordering and error behavior.

## Hints
The asyncio library provides a timeout wrapper.

## Tests
`python -m pytest tests -q`
