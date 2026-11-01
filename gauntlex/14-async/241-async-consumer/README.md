# Consume Exactly N

## Description
Wait for a specified number of queue items and return them in arrival order.

### Behavior contract
Remove exactly n items from an asyncio.Queue, returning them in FIFO order. Assume the queue will eventually receive n items. Raise ValueError for negative n.

## Requirements
- Implement `async def consume_n(queue, n)` in `starter/solution.py`.
- Use Python's `asyncio` standard library; no external packages or network access.
- Do not print or block the event loop with synchronous sleeps.
- Preserve the specified ordering and error behavior.

## Tips
Unlike draining, consuming a fixed count may need to wait for future items.

No implementation is provided; reason about scheduling and return values.
