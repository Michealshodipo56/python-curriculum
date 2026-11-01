# Process in Waves

## Description
Run work concurrently within each batch, but wait for a batch to finish before starting the next.

### Behavior contract
Given an async fn, values, and positive batch_size, process values in consecutive batches. Calls within a batch may run concurrently, but no later batch may start before the prior batch completes. Return all results in input order.

## Requirements
- Implement `async def async_batches(fn, values, batch_size)` in `starter/solution.py`.
- Use Python's `asyncio` standard library; no external packages or network access.
- Do not print or block the event loop with synchronous sleeps.
- Preserve the specified ordering and error behavior.

## Tips
Batch boundaries control when new work may begin, not merely how results are grouped.

No implementation is provided; reason about scheduling and return values.
