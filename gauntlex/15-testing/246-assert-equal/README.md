# Explain a Mismatch

## Description

A good assertion does more than say a check failed. Compare actual and expected values and report an unambiguous failure message.

## Requirements

- Implement `assert_equal(actual, expected)` in `starter/solution.py`.
- Return `None` when `actual == expected`.
- Otherwise raise `AssertionError` with exact message `expected EXPECTED, got ACTUAL`, where each placeholder uses `repr()`.
- Do not mutate the values.
- Use Python's standard library only; do not print or mutate inputs.

## Tips

- Why is `repr()` more informative than a plain string conversion?

## Example Behavior

`assert_equal(3, 3)` → `None`; `assert_equal('x', 'y')` raises `AssertionError` with `expected 'y', got 'x'`.
