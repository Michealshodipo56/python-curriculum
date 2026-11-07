# Group by Size

## Description
Organize words into groups according to their lengths. Each group must retain the original encounter order of the words it contains.

## Requirements
- Implement `group_by_length(words)` in `solution.py`.
- Return a dictionary mapping integer word lengths to lists of words.
- Preserve the original order within each length group.
- Include empty strings under length zero; return `{}` for empty input.
- Do not modify input, print, or execute code on import.

## Tips
- Which data structure can associate one length with several words?
- What should happen when another word has a length already seen?

## Example Behavior
`group_by_length(['a', 'cat', 'be', 'dog'])` → `{1: ['a'], 2: ['be'], 3: ['cat', 'dog']}`; `group_by_length([])` → `{}`.
