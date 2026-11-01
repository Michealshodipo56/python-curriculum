# Smallest Covering Substring

## Description
Find the shortest substring containing all required characters with their multiplicities.

### Behavior contract
Return the shortest substring of text containing all characters in pattern with required multiplicities. If no window exists, return empty string. On equal-length windows, return the leftmost. Empty pattern returns empty string.

## Requirements
- Implement `minimum_window(text, pattern)` in `starter/solution.py`.
- Use Python's standard library only.
- Do not mutate inputs or print.
- Respect the specified asymptotic complexity.

## Tips
Character presence is not enough when a pattern repeats a character.

The task is to design an implementation that meets both behavior and efficiency requirements.
