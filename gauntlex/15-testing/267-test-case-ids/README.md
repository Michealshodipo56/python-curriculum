# Unique Case Labels

## Description
Give repeated test names distinct identifiers based on their occurrence count.

### Behavior contract
Given a list of test case dictionaries with a `name` string, return IDs `name#N` where N is the 1-based occurrence count for that name.

## Requirements
- Implement `case_ids(cases)` in `starter/solution.py`.
- Return the specified value or raise the specified exception.
- Do not mutate input data, print, or require external packages.
- Use the Python standard library only.

## Tips
Track each name independently; a different name must not change its count.

Work from the contract and edge cases; do not include a finished implementation.
