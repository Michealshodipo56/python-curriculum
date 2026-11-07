# Consume Exactly N

## Description
Unlike draining a queue, consuming a fixed number of items may require waiting for items that have not arrived yet.

## Requirements
- Implement `async def consume_n(queue, n)` in `starter/solution.py`.
- Accept an `asyncio.Queue` and integer `n`.
- Raise `ValueError` when `n` is negative.
- Remove exactly `n` items, awaiting future arrivals when necessary.
- Return the items in FIFO order; return `[]` for `n == 0`.
- Assume the queue will eventually receive enough items.
- Use Python's `asyncio` standard library, with no external packages or network access.
- Do not print output or block the event loop with synchronous sleeps.

## Tips
- Why can a consumer need to wait even when a queue is initially empty?

## Example Behavior
`consume_n(queue, 0)` returns `[]` without removing anything.
