# Protected Increment

## Description

Multiple coroutines may share mutable state. Protect a read-modify-write operation so concurrent updates cannot interfere with one another.

## Requirements

- Implement `async def locked_increment(state, lock)` in `starter/solution.py`.
- Accept a dictionary whose string key `count` holds an integer, and an `asyncio.Lock`.
- Acquire the lock while reading and incrementing the count by one.
- Update the dictionary and return the new integer count.
- Release the lock even if the operation cannot complete normally.
- Use Python's `asyncio` standard library, with no external packages or network access.
- Do not print output or block the event loop with synchronous sleeps.

## Tips

- Why must the read and write occur inside the same protected section?

## Example Behavior

With `state = {'count': 4}`, one protected increment returns `5` and updates the stored count to `5`.
