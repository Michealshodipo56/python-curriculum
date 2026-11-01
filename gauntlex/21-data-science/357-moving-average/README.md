# Smooth with Windows

## Description
Compute averages across consecutive windows of a fixed size.

### Behavior contract
Return floating-point averages of each consecutive window of positive integer size k. If k exceeds the list length, return []. Raise ValueError for k<1.

## Requirements
- Implement `moving_average(values, k)` in `starter/solution.py`.
- Use only Python's standard library; no NumPy, pandas, or scikit-learn.
- Return the specified values without printing or mutating input data.
- Floating-point answers are checked approximately where appropriate.

## Tips
Each new window shares most of its observations with the previous one.

Reason about edge cases before designing your implementation.
