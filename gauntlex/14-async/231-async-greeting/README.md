# greet_async

## Challenge
Define an async function that returns `Hello, NAME!` for a string name, without blocking or printing.

## Requirements
- Implement `async def greet_async(name)` in `starter/solution.py`.
- Use Python's `asyncio` standard library; no external packages or network access.
- Do not print or block the event loop with synchronous sleeps.
- Preserve the specified ordering and error behavior.

## Hints
An async def function returns a coroutine when called.

## Tests
`python -m pytest tests -q`
