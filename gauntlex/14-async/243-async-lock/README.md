# locked_increment

## Challenge
Given a mutable dictionary with integer key `count` and an asyncio.Lock, increment the count once while holding the lock, then return the new count.

## Requirements
- Implement `async def locked_increment(state, lock)` in `starter/solution.py`.
- Use Python's `asyncio` standard library; no external packages or network access.
- Do not print or block the event loop with synchronous sleeps.
- Preserve the specified ordering and error behavior.

## Hints
Use an async context manager to acquire and release the lock.

## Tests
`python -m pytest tests -q`
