# consume_n

## Challenge
Remove exactly n items from an asyncio.Queue, returning them in FIFO order. Assume the queue will eventually receive n items. Raise ValueError for negative n.

## Requirements
- Implement `async def consume_n(queue, n)` in `starter/solution.py`.
- Use Python's `asyncio` standard library; no external packages or network access.
- Do not print or block the event loop with synchronous sleeps.
- Preserve the specified ordering and error behavior.

## Hints
Await queue.get for each requested item.

## Tests
`python -m pytest tests -q`
