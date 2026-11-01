# Try Again

## Description
Retry an asynchronous operation after ordinary failures without suppressing the final error.

### Behavior contract
Call a zero-argument async function up to attempts times, returning its first successful result. Retry only on Exception; re-raise the final exception. Raise ValueError if attempts < 1. No delays are required.

## Requirements
- Implement `async def retry_async(fn, attempts)` in `starter/solution.py`.
- Use Python's `asyncio` standard library; no external packages or network access.
- Do not print or block the event loop with synchronous sleeps.
- Preserve the specified ordering and error behavior.

## Tips
Every attempt should call the function again; do not reuse a failed coroutine.

No implementation is provided; reason about scheduling and return values.
