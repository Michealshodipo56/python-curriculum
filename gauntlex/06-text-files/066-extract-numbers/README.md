# Numbers Hidden in Text

## Description
Logs and messages often mix words with numeric identifiers. Extract every consecutive run of ASCII digits and represent each run as an integer.

## Requirements
- Implement `extract_numbers(text)` in `starter/solution.py`.
- Find nonoverlapping runs of ASCII digits `0` through `9` in input order.
- Convert each run to an integer; leading zeros do not survive numeric conversion.
- Return an empty list when no qualifying digit runs occur.
- Use Python's standard library only. Return values without printing or requesting input; do not mutate caller-owned inputs.

## Tips
- What ends one digit run and starts the next?
- Should a leading minus sign be part of a run of digits under this contract?

## Example Behavior
`extract_numbers("a12 b003 c")` → `[12, 3]`

`extract_numbers("no digits")` → `[]`
