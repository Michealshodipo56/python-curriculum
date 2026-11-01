# Gather in Order

## Description
Run several awaitables and return their results in the same order they were supplied.

### Behavior contract
Accept a sequence of awaitable objects and return their results as a list in input order. Empty input returns [].

## Requirements
- Implement `async def gather_results(awaitables)` in `starter/solution.py`.
- Use Python's `asyncio` standard library; no external packages or network access.
- Do not print or block the event loop with synchronous sleeps.
- Preserve the specified ordering and error behavior.

## Tips
Completion order may differ from the order in which results must be returned.

No implementation is provided; reason about scheduling and return values.
