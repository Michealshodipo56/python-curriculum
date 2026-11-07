# Observe Printed Output

## Description

A function's return value and printed output are different observable effects. Capture both while ensuring the global output stream is restored.

## Requirements

- Implement `capture_output(fn)` in `starter/solution.py`.
- Call the supplied zero-argument function once.
- Capture everything it writes to standard output during that call.
- Return `[result, stdout_text]` if the function returns normally.
- Restore standard output even if the function raises, and propagate the exception.
- Use Python's standard library only; do not print or mutate inputs unless the task explicitly requires capturing output.

## Tips

- Why is cleanup necessary even when the callable fails?

## Example Behavior

A callable that prints `Hi` and returns `7` produces `[7, 'Hi\n']`.
