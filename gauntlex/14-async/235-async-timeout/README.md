# Set a Deadline

## Description

An asynchronous operation should not be allowed to wait indefinitely when a caller sets a deadline.

## Requirements

- Implement `async def with_timeout(awaitable, seconds)` in `starter/solution.py`.
- Accept an awaitable and a timeout in seconds.
- Return the awaited result if it finishes before the deadline.
- Propagate `asyncio.TimeoutError` when the timeout expires.
- Do not turn a timeout into a successful result.
- Use Python's `asyncio` standard library, with no external packages or network access.
- Do not print output or block the event loop with synchronous sleeps.

## Tips

- What distinguishes a timeout from a normal return value?

## Example Behavior

An operation that finishes within the limit returns normally; an operation exceeding it raises `asyncio.TimeoutError`.
