# exponential_smoothing

## Challenge
Return a list of smoothed values where first output equals first input and each later output is alpha*current+(1-alpha)*previous_smoothed. Require 0<alpha<=1; empty values return [].

## Requirements
- Implement `exponential_smoothing(values, alpha)` in `starter/solution.py`.
- Use only Python's standard library; no NumPy, pandas, or scikit-learn.
- Return the specified values without printing or mutating input data.
- Floating-point answers are checked approximately where appropriate.

## Hint
Each smoothed value depends on the previous smoothed output.

## Run tests
`python -m pytest tests -q`
