# First to Finish

## Description

When several independent operations can provide the same answer, the earliest completed one may be sufficient. Unfinished operations still require cleanup.

## Requirements

- Implement `async def first_completed(awaitables)` in `starter/solution.py`.
- Accept a nonempty sequence of awaitables, none of which raises.
- Return the result of the first completed awaitable.
- Cancel unfinished tasks once a result is available.
- Do not wait for every operation to finish normally.
- Use Python's `asyncio` standard library, with no external packages or network access.
- Do not print output or block the event loop with synchronous sleeps.

## Tips

- Why is cancellation part of correctness rather than just an optimization?

## Example Behavior

If the second operation finishes before the first, return the second result and cancel unfinished work.
