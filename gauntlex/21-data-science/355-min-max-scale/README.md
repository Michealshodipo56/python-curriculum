# min_max_scale

## Challenge
Scale numeric values to [0,1] using (x-min)/(max-min). Return [] for empty input and zeros when all values are equal. Do not mutate input.

## Requirements
- Implement `min_max_scale(values)` in `starter/solution.py`.
- Use only Python's standard library; no NumPy, pandas, or scikit-learn.
- Return the specified values without printing or mutating input data.
- Floating-point answers are checked approximately where appropriate.

## Hint
Find extrema once; handle a zero denominator.

## Run tests
`python -m pytest tests -q`
