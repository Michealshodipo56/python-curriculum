# moving_average

## Challenge
Return floating-point averages of each consecutive window of positive integer size k. If k exceeds the list length, return []. Raise ValueError for k<1.

## Requirements
- Implement `moving_average(values, k)` in `starter/solution.py`.
- Use only Python's standard library; no NumPy, pandas, or scikit-learn.
- Return the specified values without printing or mutating input data.
- Floating-point answers are checked approximately where appropriate.

## Hint
A sliding sum avoids repeatedly summing each window.

## Run tests
`python -m pytest tests -q`
