# Longest Distinct Window

## Description
Measure the longest contiguous stretch of Unicode text in which no character repeats. A substring must stay contiguous; skipping repeated characters would change the problem.

## Requirements
- Implement `longest_unique_substring(text)` in `starter/solution.py`.
- Return the maximum number of characters in a contiguous substring with no repeated Unicode characters.
- Return `0` for empty text.
- Target O(n) time rather than rechecking every substring.
- Do not print or mutate inputs.
- Use Python's standard library only.

## Design Considerations
Track a contiguous window containing no repeated characters. When a repeated character appears, adjust the left boundary without revisiting every earlier substring.

## Tips
- How can the left edge of a valid window move when a repeated character appears?
- What information about earlier occurrences would avoid rescanning?

## Example Behavior
`longest_unique_substring('abba')` → `2`; `longest_unique_substring('')` → `0`.
