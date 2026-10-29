# gather_results

## Challenge
Accept a sequence of awaitable objects and return their results as a list in input order. Empty input returns [].

## Requirements
- Implement `async def gather_results(awaitables)` in `starter/solution.py`.
- Use Python's `asyncio` standard library; no external packages or network access.
- Do not print or block the event loop with synchronous sleeps.
- Preserve the specified ordering and error behavior.

## Hints
Gather preserves argument order even if tasks complete in a different order.

## Tests
`python -m pytest tests -q`
