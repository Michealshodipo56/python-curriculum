# Longest Distinct Window

## Description
Find the longest contiguous region of Unicode text without repeated characters in linear time.

### Behavior contract
Return the length of the longest contiguous substring with no repeated Unicode characters. Empty string returns zero. Target O(n) time.

## Requirements
- Implement `longest_unique_substring(text)` in `starter/solution.py`.
- Use Python's standard library only.
- Do not mutate inputs or print.
- Respect the specified asymptotic complexity.

## Tips
A sliding window can advance without reexamining all earlier characters.

The task is to design an implementation that meets both behavior and efficiency requirements.
