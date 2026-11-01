# Set a Deadline

## Description
Wait for an asynchronous operation but fail when it exceeds a specified time limit.

### Behavior contract
Await an awaitable with a timeout in seconds; return its result or propagate asyncio.TimeoutError when exceeded.

## Requirements
- Implement `async def with_timeout(awaitable, seconds)` in `starter/solution.py`.
- Use Python's `asyncio` standard library; no external packages or network access.
- Do not print or block the event loop with synchronous sleeps.
- Preserve the specified ordering and error behavior.

## Tips
A timeout is an observable failure, not a successful result.

No implementation is provided; reason about scheduling and return values.
