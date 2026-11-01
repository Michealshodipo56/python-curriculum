# Drain the Queue

## Description
Collect all items currently waiting in an asynchronous queue without waiting for future arrivals.

### Behavior contract
Given an asyncio.Queue already containing items, remove and return all currently queued items in FIFO order without blocking.

## Requirements
- Implement `async def queue_drain(queue)` in `starter/solution.py`.
- Use Python's `asyncio` standard library; no external packages or network access.
- Do not print or block the event loop with synchronous sleeps.
- Preserve the specified ordering and error behavior.

## Tips
Draining what is already present differs from waiting for a producer.

No implementation is provided; reason about scheduling and return values.
