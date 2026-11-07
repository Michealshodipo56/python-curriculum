# Require Every Item

## Description
An assertion can check whether all expected items appear in an actual collection. When the check fails, report the missing values in a reproducible order.

## Requirements
- Implement `assert_subset(expected_items, actual_items)` in `starter/solution.py`.
- Accept collections of sortable, hashable elements.
- Return `None` if every expected item is present in the actual collection.
- Otherwise raise `AssertionError` whose message includes a sorted list of missing items.
- Do not mutate either input.
- Use Python's standard library only; do not print or mutate inputs.

## Tips
- Why is sorting useful for reproducible failure messages?

## Example Behavior
`assert_subset([1, 2], [1, 2, 3])` → `None`; missing expected items trigger `AssertionError`.
