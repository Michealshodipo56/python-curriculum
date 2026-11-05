# Gather in Order

## Description
Several awaitables may finish in an unpredictable order. Collect their results in the original input order, regardless of completion timing.

## Requirements
- Implement `async def gather_results(awaitables)` in `starter/solution.py`.
- Accept a sequence of awaitable objects.
- Run the awaitables concurrently and return a list of results in input order.
- Return `[]` for empty input.
- Use Python's `asyncio` standard library, with no external packages or network access.
- Do not print output or block the event loop with synchronous sleeps.

## Tips
- How can concurrent tasks finish out of order while their results remain ordered?

## Example Behavior
Awaitables returning `3`, `1`, and `2` in that input order produce `[3, 1, 2]` even if they finish in another order.
