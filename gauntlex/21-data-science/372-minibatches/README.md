# mini_batches

## Challenge
Split a sequence into consecutive lists of at most positive integer batch_size. Preserve order and include the final partial batch. Raise ValueError for nonpositive batch_size.

## Requirements
- Implement `mini_batches(items, batch_size)` in `starter/solution.py`.
- Use only Python's standard library; no NumPy, pandas, or scikit-learn.
- Return the specified values without printing or mutating input data.
- Floating-point answers are checked approximately where appropriate.

## Hint
Step through indices by the batch size.

## Run tests
`python -m pytest tests -q`
