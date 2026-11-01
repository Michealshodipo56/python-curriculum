# Backoff with a Ceiling

## Description
Calculate exponentially increasing retry delays that stop growing beyond a cap.

### Behavior contract
Return exponential backoff delay in seconds for nonnegative attempt, positive base, and positive cap: min(cap,base*2**attempt).

## Requirements
- Implement `retry_delay(attempt, base, cap)` in `starter/solution.py`.
- Return the required value; do not print or prompt.
- Use Python's standard library only; do not make real network requests.
- Preserve inputs without mutation.

## Examples
`retry_delay(0, 0.5, 10)` → `0.5`

`retry_delay(3, 0.5, 10)` → `4`

## Tips
The first attempt starts at the base delay; later attempts double it.

Examples describe the contract, not a solution.
