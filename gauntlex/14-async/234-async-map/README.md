# Concurrent Transformation

## Description
Apply an asynchronous operation to each item without waiting for one item to finish before beginning the next.

## Requirements
- Implement `async def async_map(fn, values)` in `starter/solution.py`.
- Accept an async function `fn` and a sequence of values.
- Invoke `fn(value)` for every value concurrently.
- Return results in input order, including an empty list for empty input.
- Use Python's `asyncio` standard library, with no external packages or network access.
- Do not print output or block the event loop with synchronous sleeps.

## Tips
- What is the difference between creating concurrent work and ordering its results?

## Example Behavior
For an async doubling function and values `[2, 4]`, the result is `[4, 8]`.
