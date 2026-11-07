# One Space Apart

## Description
A message copied from different sources may contain tabs, newlines, and repeated spaces. Produce a clean single-line representation without losing or rearranging words.

## Requirements
- Implement `normalize_spaces(text)` in `starter/solution.py`.
- Treat consecutive whitespace characters as a single separator between words.
- Remove leading and trailing whitespace; return an empty string when no words remain.
- Preserve the order and spelling of nonwhitespace characters.
- Use Python's standard library only. Return values without printing or requesting input; do not mutate caller-owned inputs.

## Tips
- What happens when the input contains only tabs and spaces?
- Why should a newline between two words become a separator rather than joining the words?

## Example Behavior
`normalize_spaces("  hello   world \n")` → `"hello world"`

`normalize_spaces("\tA \t B\t")` → `"A B"`
