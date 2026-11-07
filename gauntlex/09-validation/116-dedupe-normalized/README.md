# Distinct After Normalization

## Description

Clean strings consistently before deciding which values are duplicates. Keep only meaningful normalized values in their original first-appearance order.

## Requirements

- Implement `dedupe_normalized(items)` in `starter/solution.py`.
- Trim surrounding whitespace and apply Unicode casefolding to each string.
- Discard values that become empty after trimming.
- Keep only the first occurrence of each normalized value.
- Return a new list without modifying `items`.
- Return the specified value without printing or reading standard input. Use Python's standard library only.

## Tips

- Why must normalization happen before duplicate detection?
- How can casefolding differ from preserving the original spelling?

## Example Behavior

`dedupe_normalized(['  Ada ', 'ada', 'BOB', 'bob', '  '])` → `['ada', 'bob']`; `dedupe_normalized([])` → `[]`.
