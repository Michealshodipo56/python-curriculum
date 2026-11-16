# Train in Batches

## Description

Implement `mini_batches(items, batch_size)` in `starter/solution.py`. Require positive integer `batch_size`; raise `ValueError` otherwise.

## Requirements

- Implement `mini_batches(items, batch_size)` in `starter/solution.py`.
- Require positive integer `batch_size`; raise `ValueError` otherwise.
- Split input into consecutive lists with at most `batch_size` items.
- Preserve original order and include a shorter final batch.
- Return `[]` for empty input.
- Use Python's standard library only; do not use NumPy, pandas, or scikit-learn. Do not print or mutate inputs.
- Floating-point results may be compared approximately.

## Design Considerations

Partition consecutive observations without overlap or omission. Keep the last smaller batch when the input length is not divisible by the requested positive batch size.

## Tips

- **Concept to understand:** Large datasets are often processed in smaller consecutive groups. Preserve all observations, including a final incomplete group.
- Why should a partially filled final batch not be discarded?

## Example Behavior

`mini_batches([1, 2, 3, 4, 5], 2)` → `[[1, 2], [3, 4], [5]]`.
