# Compare Secrets Safely

## Description
Compare text values with a timing-resistant primitive rather than an ordinary character-by-character check.

### Behavior contract
Return whether two strings are equal, using the standard library's timing-resistant comparison primitive. Support Unicode strings.

## Requirements
- Implement `constant_time_compare(a, b)` in `starter/solution.py`.
- Return the required value; do not print or prompt.
- Use Python's standard library only; do not make real network requests.
- Preserve inputs without mutation.

## Examples
`constant_time_compare("abc", "abc")` → `True`

`constant_time_compare("abc", "abd")` → `False`

## Tips
Use a consistent byte encoding before comparing Unicode strings.

Examples describe the contract, not a solution.
