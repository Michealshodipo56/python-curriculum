# first_completed

## Challenge
Accept a nonempty sequence of awaitables, return the result of the first to complete successfully, and cancel unfinished tasks. Assume no awaitable raises.

## Requirements
- Implement `async def first_completed(awaitables)` in `starter/solution.py`.
- Use Python's `asyncio` standard library; no external packages or network access.
- Do not print or block the event loop with synchronous sleeps.
- Preserve the specified ordering and error behavior.

## Hints
Wait for the first completed task and cancel pending work.

## Tests
`python -m pytest tests -q`
