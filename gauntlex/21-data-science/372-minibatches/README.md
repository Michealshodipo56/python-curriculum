# Train in Batches

## Description
Partition data into consecutive batches while retaining a final incomplete batch.

### Behavior contract
Split a sequence into consecutive lists of at most positive integer batch_size. Preserve order and include the final partial batch. Raise ValueError for nonpositive batch_size.

## Requirements
- Implement `mini_batches(items, batch_size)` in `starter/solution.py`.
- Use only Python's standard library; no NumPy, pandas, or scikit-learn.
- Return the specified values without printing or mutating input data.
- Floating-point answers are checked approximately where appropriate.

## Tips
A final partial batch still contains useful data.

Reason about edge cases before designing your implementation.
