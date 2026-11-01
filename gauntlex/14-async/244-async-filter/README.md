# Concurrent Selection

## Description
Evaluate an asynchronous predicate for every value and retain only the matching inputs.

### Behavior contract
Given an async predicate and a sequence of values, evaluate predicates concurrently and return the values whose predicate results are truthy, preserving original order.

## Requirements
- Implement `async def async_filter(predicate, values)` in `starter/solution.py`.
- Use Python's `asyncio` standard library; no external packages or network access.
- Do not print or block the event loop with synchronous sleeps.
- Preserve the specified ordering and error behavior.

## Tips
Preserve original input order even if predicate checks finish in a different order.

No implementation is provided; reason about scheduling and return values.
