# cosine_similarity

## Challenge
Return cosine similarity of equal-length numeric vectors. Return 0.0 if either vector has zero magnitude, including empty vectors. Raise ValueError on length mismatch.

## Requirements
- Implement `cosine_similarity(a, b)` in `starter/solution.py`.
- Use only Python's standard library; no NumPy, pandas, or scikit-learn.
- Return the specified values without printing or mutating input data.
- Floating-point answers are checked approximately where appropriate.

## Hint
Normalize the dot product by both vector magnitudes.

## Run tests
`python -m pytest tests -q`
