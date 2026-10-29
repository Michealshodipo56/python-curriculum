# produce_items

## Challenge
Put each element from values into an asyncio.Queue in order and return the number of items enqueued.

## Requirements
- Implement `async def produce_items(queue, values)` in `starter/solution.py`.
- Use Python's `asyncio` standard library; no external packages or network access.
- Do not print or block the event loop with synchronous sleeps.
- Preserve the specified ordering and error behavior.

## Hints
The queue's put method is awaitable.

## Tests
`python -m pytest tests -q`
