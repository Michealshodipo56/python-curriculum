# A Coroutine Result

## Description
Return a calculated value from a coroutine and observe how callers receive it.

### Behavior contract
Define an async function returning twice its integer input.

## Requirements
- Implement `async def double_async(value)` in `starter/solution.py`.
- Use Python's `asyncio` standard library; no external packages or network access.
- Do not print or block the event loop with synchronous sleeps.
- Preserve the specified ordering and error behavior.

## Tips
An async function can return a value without performing any asynchronous waiting.

No implementation is provided; reason about scheduling and return values.
