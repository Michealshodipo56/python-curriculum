# Compare Secrets Safely

## Description

Compare Unicode strings using a timing-resistant standard-library primitive rather than an ordinary early-exit comparison.

## Requirements

- Implement `constant_time_compare(a, b)` in `starter/solution.py`.
- Return whether the two strings are equal.
- Support Unicode input by using a consistent byte encoding.
- Use the standard library's timing-resistant comparison facility.
- Do not print or expose intermediate comparison results.
- Use Python's standard library without printing or making network requests.

## Tips

- Why can early-exit comparisons reveal information through timing?

## Example Behavior

`constant_time_compare("abc", "abc")` → `True`

`constant_time_compare("abc", "abd")` → `False`
