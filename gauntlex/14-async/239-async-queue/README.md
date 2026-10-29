# queue_drain

## Challenge
Given an asyncio.Queue already containing items, remove and return all currently queued items in FIFO order without blocking.

## Requirements
- Implement `async def queue_drain(queue)` in `starter/solution.py`.
- Use Python's `asyncio` standard library; no external packages or network access.
- Do not print or block the event loop with synchronous sleeps.
- Preserve the specified ordering and error behavior.

## Hints
Use nonblocking queue operations when draining an existing queue.

## Tests
`python -m pytest tests -q`
