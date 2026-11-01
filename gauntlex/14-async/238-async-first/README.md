# First to Finish

## Description
Return the earliest completed asynchronous result and cancel unfinished work.

### Behavior contract
Accept a nonempty sequence of awaitables, return the result of the first to complete successfully, and cancel unfinished tasks. Assume no awaitable raises.

## Requirements
- Implement `async def first_completed(awaitables)` in `starter/solution.py`.
- Use Python's `asyncio` standard library; no external packages or network access.
- Do not print or block the event loop with synchronous sleeps.
- Preserve the specified ordering and error behavior.

## Tips
Cancellation is part of correct cleanup, not an optional optimization.

No implementation is provided; reason about scheduling and return values.
