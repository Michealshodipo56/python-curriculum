# classification_metrics

## Challenge
Given integer tp,tn,fp,fn >=0, return precision, recall, accuracy and f1 as floats in a dictionary. Use 0.0 when any metric denominator is zero, including accuracy on an empty sample. Raise ValueError for negative counts.

## Requirements
- Implement `classification_metrics(tp, tn, fp, fn)` in `starter/solution.py`.
- Use only Python's standard library; no NumPy, pandas, or scikit-learn.
- Return the specified values without printing or mutating input data.
- Floating-point answers are checked approximately where appropriate.

## Hint
Compute precision and recall before their harmonic mean.

## Run tests
`python -m pytest tests -q`
