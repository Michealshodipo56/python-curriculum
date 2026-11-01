# Produce in Sequence

## Description
Place a series of values into an asynchronous queue and report how many were added.

### Behavior contract
Put each element from values into an asyncio.Queue in order and return the number of items enqueued.

## Requirements
- Implement `async def produce_items(queue, values)` in `starter/solution.py`.
- Use Python's `asyncio` standard library; no external packages or network access.
- Do not print or block the event loop with synchronous sleeps.
- Preserve the specified ordering and error behavior.

## Tips
Queue insertion can require waiting when capacity is limited.

No implementation is provided; reason about scheduling and return values.
