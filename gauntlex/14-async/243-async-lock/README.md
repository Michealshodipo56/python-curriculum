# Protected Increment

## Description
Update shared mutable state under an asynchronous lock.

### Behavior contract
Given a mutable dictionary with integer key `count` and an asyncio.Lock, increment the count once while holding the lock, then return the new count.

## Requirements
- Implement `async def locked_increment(state, lock)` in `starter/solution.py`.
- Use Python's `asyncio` standard library; no external packages or network access.
- Do not print or block the event loop with synchronous sleeps.
- Preserve the specified ordering and error behavior.

## Tips
A read-modify-write operation needs protection when several coroutines share state.

No implementation is provided; reason about scheduling and return values.
