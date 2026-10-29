# async_batches

## Challenge
Given an async fn, values, and positive batch_size, process values in consecutive batches. Calls within a batch may run concurrently, but no later batch may start before the prior batch completes. Return all results in input order.

## Requirements
- Implement `async def async_batches(fn, values, batch_size)` in `starter/solution.py`.
- Use Python's `asyncio` standard library; no external packages or network access.
- Do not print or block the event loop with synchronous sleeps.
- Preserve the specified ordering and error behavior.

## Hints
Slice into batches and await each batch before starting the next.

## Tests
`python -m pytest tests -q`
