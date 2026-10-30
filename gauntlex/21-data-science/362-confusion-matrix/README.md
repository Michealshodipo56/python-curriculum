# confusion_matrix

## Challenge
Given equal-length sequences of actual and predicted booleans, return a dictionary with integer keys `tp`, `tn`, `fp`, `fn`. Raise ValueError on mismatched lengths.

## Requirements
- Implement `confusion_matrix(actual, predicted)` in `starter/solution.py`.
- Use only Python's standard library; no NumPy, pandas, or scikit-learn.
- Return the specified values without printing or mutating input data.
- Floating-point answers are checked approximately where appropriate.

## Hint
Classify each prediction against its ground truth.

## Run tests
`python -m pytest tests -q`
