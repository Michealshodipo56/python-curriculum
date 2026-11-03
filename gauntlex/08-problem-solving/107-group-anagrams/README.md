# Families of Letters

## Description
Group words with identical character frequencies while preserving both the first appearance of each group and the original order within that group.

## Requirements
- Implement `group_anagrams(words)` in `starter/solution.py`.
- Return a list of lists of anagram strings.
- Treat case and every character as significant.
- Order groups by the first occurrence of any member.
- Preserve input order within each group.
- Return `[]` for empty input; do not mutate the original list.
- Return the result without printing or reading input. Use Python's standard library only.

## Tips
- Why is matching only distinct characters insufficient?
- How do you preserve two different levels of ordering?

## Example Behavior
`group_anagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat'])` → `[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]`.
