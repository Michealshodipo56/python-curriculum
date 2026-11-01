# Observe Printed Output

## Description
Capture the text produced by a function while preserving its return value.

### Behavior contract
Call zero-argument fn and return [result,stdout_text] with everything printed to stdout during the call. Restore stdout even if fn raises, and propagate its exception.

## Requirements
- Implement `capture_output(fn)` in `starter/solution.py`.
- Return the specified value or raise the specified exception.
- Do not mutate input data, print, or require external packages.
- Use the Python standard library only.

## Tips
Restore the output stream even when the function raises an exception.

Work from the contract and edge cases; do not include a finished implementation.
