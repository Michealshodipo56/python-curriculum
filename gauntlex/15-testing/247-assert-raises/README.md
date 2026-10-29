# assert_raises

## Challenge
Call zero-argument fn and return the caught exception if it is an instance of expected_exception; otherwise raise AssertionError. If fn returns normally, raise AssertionError.

## Requirements
- Implement `assert_raises(expected_exception, fn)` in `starter/solution.py`.
- Return the specified value or raise the specified exception.
- Do not mutate input data, print, or require external packages.
- Use the Python standard library only.

## Hints
Distinguish the expected exception from an unexpected one.

## Run tests
`python -m pytest tests -q`
