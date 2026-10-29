# group_anagrams

## Description
Group strings that are anagrams. Return groups in order of first group appearance, with strings in original input order. Comparison is case-sensitive.

## Requirements
- Implement `group_anagrams(words)` in `starter/solution.py`.
- Return the result without printing or reading input.
- Do not mutate input collections.
- Use only Python's standard library.

## Examples
`group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])` → `[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]`

`group_anagrams([])` → `[]`

## Tips
Use a canonical character signature as a dictionary key.
