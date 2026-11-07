# Smallest Covering Substring

## Description
Find the shortest contiguous part of a string that covers every required character, including repeated requirements. If several shortest windows qualify, choose the earliest.

## Requirements
- Implement `minimum_window(text, pattern)` in `starter/solution.py`.
- The selected substring must contain every character of `pattern` at least as many times as it occurs there.
- Return the shortest qualifying substring; break equal-length ties by leftmost position.
- Return `''` when no qualifying window exists or when the pattern is empty.
- Do not mutate inputs or print.
- Use Python's standard library only.

## Tips
- Why is a set of required characters insufficient for repeated letters?
- When can the left edge of a valid window be advanced safely?

## Example Behavior
`minimum_window('ADOBECODEBANC', 'ABC')` → `'BANC'`; `minimum_window('a', 'aa')` → `''`.
