# Try Again

## Description
Transient failures sometimes justify another attempt. Each retry must call the operation again rather than reuse a coroutine that has already failed.

## Requirements
- Implement `async def retry_async(fn, attempts)` in `starter/solution.py`.
- Accept a zero-argument async function and an integer attempt count.
- Raise `ValueError` if attempts is less than one.
- Call the function up to that many times, returning the first successful result.
- Retry only on `Exception` and re-raise the final failure.
- Do not introduce retry delays.
- Use Python's `asyncio` standard library, with no external packages or network access.
- Do not print output or block the event loop with synchronous sleeps.

## Tips
- Why must a fresh coroutine be created for each attempt?|Why should the final error remain visible?

## Example Behavior
If the first call fails and the second succeeds with `9`, the result is `9` and no third call is made.
