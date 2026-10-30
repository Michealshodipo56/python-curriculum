# longest_unique_substring

## Challenge
Return the length of the longest contiguous substring with no repeated Unicode characters. Empty string returns zero. Target O(n) time.

## Requirements
- Implement `longest_unique_substring(text)` in `starter/solution.py`.
- Use Python's standard library only.
- Do not mutate inputs or print.
- Respect the specified asymptotic complexity.

## Hint
Track each character's most recent position within a sliding window.

## Run tests
`python -m pytest tests -q`
