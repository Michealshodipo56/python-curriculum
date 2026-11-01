# Classify the Outcomes

## Description
Summarize binary predictions as true positives, true negatives, false positives, and false negatives.

### Behavior contract
Given equal-length sequences of actual and predicted booleans, return a dictionary with integer keys `tp`, `tn`, `fp`, `fn`. Raise ValueError on mismatched lengths.

## Requirements
- Implement `confusion_matrix(actual, predicted)` in `starter/solution.py`.
- Use only Python's standard library; no NumPy, pandas, or scikit-learn.
- Return the specified values without printing or mutating input data.
- Floating-point answers are checked approximately where appropriate.

## Tips
Each prediction belongs to exactly one of four categories.

Reason about edge cases before designing your implementation.
