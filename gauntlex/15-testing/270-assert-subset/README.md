# Require Every Item

## Description
Verify that an expected collection is contained in the actual collection, reporting missing items.

### Behavior contract
Return None if every element in expected_items appears in actual_items; otherwise raise AssertionError with a sorted list of missing items in the message. Elements are sortable and hashable.

## Requirements
- Implement `assert_subset(expected_items, actual_items)` in `starter/solution.py`.
- Return the specified value or raise the specified exception.
- Do not mutate input data, print, or require external packages.
- Use the Python standard library only.

## Tips
Sort missing items so failure messages are reproducible.

Work from the contract and edge cases; do not include a finished implementation.
