# Concurrent Selection

## Description

Evaluate an asynchronous predicate for every value, then keep only those values whose predicate results are truthy.

## Requirements

- Implement `async def async_filter(predicate, values)` in `starter/solution.py`.
- Accept an async predicate and a sequence of values.
- Evaluate the predicate for each value concurrently.
- Return original input values whose predicate results are truthy.
- Preserve original input order regardless of completion order.
- Return `[]` for empty input.
- Use Python's `asyncio` standard library, with no external packages or network access.
- Do not print output or block the event loop with synchronous sleeps.

## Tips

- Why should filtering retain the original values rather than predicate results?

## Example Behavior

If the predicate accepts even numbers, values `[3, 2, 4]` produce `[2, 4]`.
