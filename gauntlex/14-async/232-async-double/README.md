# A Coroutine Result

## Description
An asynchronous function can return an ordinary calculated value even when it has no waiting to perform.

## Requirements
- Implement `async def double_async(value)` in `starter/solution.py`.
- Define `async def double_async(value)` for an integer.
- Return twice the input integer.
- Do not print, sleep, or block the event loop.
- Use Python's `asyncio` standard library, with no external packages or network access.
- Do not print output or block the event loop with synchronous sleeps.

## Tips
- Does an `async def` function need to await something before it can return a value?

## Example Behavior
`await double_async(7)` → `14`
