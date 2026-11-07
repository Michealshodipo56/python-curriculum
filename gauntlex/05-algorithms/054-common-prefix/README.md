# Shared Beginning

## Description
Several words may begin with the same sequence of characters. Find the longest prefix shared by every word in the input collection.

## Requirements
- Implement `common_prefix(words)` in `solution.py`.
- Return the longest initial substring shared by all input strings.
- Compare characters exactly, including case.
- Return an empty string for an empty list or when no common prefix exists.
- Do not mutate input, print, or execute code on import.

## Tips
- How does the shortest word limit the possible prefix?
- What happens at the first mismatch?
- Consider a list containing one word.

## Example Behavior
`common_prefix(['flower', 'flow', 'flight'])` → `'fl'`; `common_prefix(['dog', 'cat'])` → `''`.
