# An Awaitable Greeting

## Description
Create a coroutine that returns a personalized greeting without printing or blocking.

### Behavior contract
Define an async function that returns `Hello, NAME!` for a string name, without blocking or printing.

## Requirements
- Implement `async def greet_async(name)` in `starter/solution.py`.
- Use Python's `asyncio` standard library; no external packages or network access.
- Do not print or block the event loop with synchronous sleeps.
- Preserve the specified ordering and error behavior.

## Tips
Calling an async function and awaiting its result are two distinct steps.

No implementation is provided; reason about scheduling and return values.
