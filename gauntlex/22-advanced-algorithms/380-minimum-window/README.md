# minimum_window

## Challenge
Return the shortest substring of text containing all characters in pattern with required multiplicities. If no window exists, return empty string. On equal-length windows, return the leftmost. Empty pattern returns empty string.

## Requirements
- Implement `minimum_window(text, pattern)` in `starter/solution.py`.
- Use Python's standard library only.
- Do not mutate inputs or print.
- Respect the specified asymptotic complexity.

## Hint
Use character frequency requirements and a shrinking window.

## Run tests
`python -m pytest tests -q`
