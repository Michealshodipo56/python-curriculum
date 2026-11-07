# Drain the Queue

## Description
A queue holds work in first-in, first-out order. Collect what is currently waiting without suspending until future items arrive.

## Requirements
- Implement `async def queue_drain(queue)` in `starter/solution.py`.
- Accept an existing `asyncio.Queue`.
- Remove and return all currently queued items in FIFO order.
- Return `[]` if the queue is empty.
- Do not wait for additional items.
- Use Python's `asyncio` standard library, with no external packages or network access.
- Do not print output or block the event loop with synchronous sleeps.

## Tips
- Why is draining a queue different from waiting for a producer?

## Example Behavior
A queue holding `['a', 'b']` produces `['a', 'b']` and is empty afterward.
