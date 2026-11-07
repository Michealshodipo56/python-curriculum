# Process in Waves

## Description
Divide asynchronous work into consecutive batches. Work within a batch may overlap, but later batches must not begin until earlier batches finish.

## Requirements
- Implement `async def async_batches(fn, values, batch_size)` in `starter/solution.py`.
- Accept an async function, values, and a positive batch size.
- Process consecutive groups of at most `batch_size` items.
- Allow calls within one group to run concurrently.
- Do not start any later group before the previous group finishes.
- Return all results in input order; return `[]` for empty input.
- Use Python's `asyncio` standard library, with no external packages or network access.
- Do not print output or block the event loop with synchronous sleeps.

## Tips
- How do batch boundaries differ from a simple concurrency limit?

## Example Behavior
With five inputs and a batch size of two, batches have sizes 2, 2, and 1, executed in sequence.
