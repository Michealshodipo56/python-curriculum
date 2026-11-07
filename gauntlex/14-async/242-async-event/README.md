# Wait for a Signal

## Description
An event coordinates coroutines by letting one wait until another announces that a condition is ready.

## Requirements
- Implement `async def wait_for_event(event)` in `starter/solution.py`.
- Accept an `asyncio.Event`.
- Suspend until the event is set.
- Return `True` after the signal arrives.
- Return promptly if the event is already set.
- Use Python's `asyncio` standard library, with no external packages or network access.
- Do not print output or block the event loop with synchronous sleeps.

## Tips
- Why is awaiting a signal preferable to repeatedly polling a flag?

## Example Behavior
An already-set event lets `wait_for_event(event)` return `True` without waiting.
