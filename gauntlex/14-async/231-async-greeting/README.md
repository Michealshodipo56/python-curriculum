# An Awaitable Greeting

## Description

A coroutine is a function whose result can be awaited by an asynchronous caller. Begin with a greeting that returns text rather than printing it.

## Requirements

- Implement `async def greet_async(name)` in `starter/solution.py`.
- Return the exact string `Hello, NAME!`, substituting the supplied name.
- Do not print, sleep, or block the event loop.
- Use Python's `asyncio` standard library, with no external packages or network access.
- Do not print output or block the event loop with synchronous sleeps.

## Tips

- What is the difference between calling a coroutine function and awaiting it?

## Example Behavior

`await greet_async('Ada')` → `'Hello, Ada!'`
