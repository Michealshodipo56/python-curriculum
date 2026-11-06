# Cross-Platform Failures

## Description
A test suite may run on several platforms. Identify any test that failed on at least one platform, regardless of its results elsewhere.

## Requirements
- Implement `test_matrix(results)` in `starter/solution.py`.
- Accept a mapping from platform names to mappings of test names to boolean results.
- Include a test name if any platform records `False` for that test.
- Return unique failing names sorted alphabetically.
- Return `[]` when no failures are recorded.
- Use Python's standard library only; do not print or mutate inputs.

## Tips
- Why does one failure matter even if other platforms pass?

## Example Behavior
`test_matrix({'linux': {'a': True}, 'windows': {'a': False, 'b': True}})` → `['a']`.
