# Spot Regressions

## Description

Implement `regressions(baseline, current)` in `starter/solution.py`. Include only names present in both mappings that changed from `True` to `False`.

## Requirements

- Implement `regressions(baseline, current)` in `starter/solution.py`.
- Accept mappings from test names to boolean pass results for baseline and current runs.
- Include only names present in both mappings that changed from `True` to `False`.
- Return matching test names in sorted order.
- Ignore newly added or removed tests.
- Use Python's standard library only; do not print or mutate inputs.

## Tips

- **Concept to understand:** A regression occurs when a previously passing test now fails. Compare two test runs while excluding tests that were not present in both.
- Why is a new failing test not necessarily a regression relative to the baseline?

## Example Behavior

`regressions({'a': True, 'b': False}, {'a': False, 'b': False})` → `['a']`.
