# async_filter

## Challenge
Given an async predicate and a sequence of values, evaluate predicates concurrently and return the values whose predicate results are truthy, preserving original order.

## Requirements
- Implement `async def async_filter(predicate, values)` in `starter/solution.py`.
- Use Python's `asyncio` standard library; no external packages or network access.
- Do not print or block the event loop with synchronous sleeps.
- Preserve the specified ordering and error behavior.

## Hints
Gather Boolean results, then pair each result with its original value.

## Tests
`python -m pytest tests -q`
