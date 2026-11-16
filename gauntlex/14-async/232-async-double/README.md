# A Coroutine Result

## Description

Implement `async def double_async(value)` in `starter/solution.py`. Return twice the input integer.

## Requirements

- Implement `async def double_async(value)` in `starter/solution.py`.
- Return twice the input integer.
- Do not print, sleep, or block the event loop.
- Use Python's `asyncio` standard library, with no external packages or network access.
- Do not print output or block the event loop with synchronous sleeps.

## Tips

- **Concept to understand:** An asynchronous function can return an ordinary calculated value even when it has no waiting to perform.
- Does an `async def` function need to await something before it can return a value?

## Example Behavior

`await double_async(7)` → `14`
