# Count the Lines

## Description
Text records can end at a newline or at the end of the string. Count logical lines consistently, without inventing an extra record merely because the text ends in a line break.

## Requirements
- Implement `line_count(text)` in `starter/solution.py`.
- Return the number of logical lines represented by the supplied text.
- Count a final nonempty line even when it has no trailing newline.
- Do not count a phantom extra line after a trailing newline; empty text contains zero lines.
- Use Python's standard library only. Return values without printing or requesting input; do not mutate caller-owned inputs.

## Tips
- Compare an empty string, a single word, and a word followed by a newline.
- Why is counting separators alone not sufficient?

## Example Behavior
`line_count("one\ntwo\n")` → `2`

`line_count("single")` → `1`
