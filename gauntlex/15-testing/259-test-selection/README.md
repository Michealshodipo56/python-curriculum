# Select by Name

## Description

Large test suites often need a focused subset. Match a search term within test names without changing their original spelling or order.

## Requirements

- Implement `select_tests(names, pattern)` in `starter/solution.py`.
- Accept test names and a substring pattern.
- Match the pattern case-insensitively anywhere in each name.
- Return matching original names in their input order.
- An empty pattern matches every name.
- Use Python's standard library only; do not print or mutate inputs.

## Tips

- Why should the output preserve the original capitalization?

## Example Behavior

`select_tests(['TestLogin', 'testCart', 'LOGIN_FLOW'], 'login')` → `['TestLogin', 'LOGIN_FLOW']`.
