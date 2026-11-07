# Produce in Sequence

## Description

A producer adds values to a shared asynchronous queue. When the queue has limited capacity, insertion may need to wait for space.

## Requirements

- Implement `async def produce_items(queue, values)` in `starter/solution.py`.
- Accept an `asyncio.Queue` and a sequence of values.
- Enqueue every value in its original order.
- Return the number of values successfully enqueued.
- Return `0` for empty input.
- Use Python's `asyncio` standard library, with no external packages or network access.
- Do not print output or block the event loop with synchronous sleeps.

## Tips

- Why can putting an item into a bounded queue require waiting?

## Example Behavior

Enqueuing three values returns `3`, and the queue receives them in their original order.
