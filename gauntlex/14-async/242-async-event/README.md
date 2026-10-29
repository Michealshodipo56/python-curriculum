# wait_for_event

## Challenge
Await an asyncio.Event and return True after it is set.

## Requirements
- Implement `async def wait_for_event(event)` in `starter/solution.py`.
- Use Python's `asyncio` standard library; no external packages or network access.
- Do not print or block the event loop with synchronous sleeps.
- Preserve the specified ordering and error behavior.

## Hints
Events let coroutines wait for a signal without busy looping.

## Tests
`python -m pytest tests -q`
