# Wait for a Signal

## Description
Suspend a coroutine until another part of the program signals that an event occurred.

### Behavior contract
Await an asyncio.Event and return True after it is set.

## Requirements
- Implement `async def wait_for_event(event)` in `starter/solution.py`.
- Use Python's `asyncio` standard library; no external packages or network access.
- Do not print or block the event loop with synchronous sleeps.
- Preserve the specified ordering and error behavior.

## Tips
An event allows waiting without repeatedly checking a flag.

No implementation is provided; reason about scheduling and return values.
