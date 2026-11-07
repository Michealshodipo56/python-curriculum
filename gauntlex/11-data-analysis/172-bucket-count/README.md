# Build a Histogram

## Description
A fixed-width histogram groups observations into adjacent numeric intervals. Count values that fall into each interval and ignore those outside the supported range.

## Requirements
- Implement `bucket_count(values, width, bucket_count)` in `starter/solution.py`.
- Assume `width > 0` and `bucket_count >= 0`.
- Create `bucket_count` half-open buckets beginning at zero, each of width `width`.
- Count values in `[0, width)`, `[width, 2 * width)`, and subsequent intervals.
- Ignore values below zero or at least `width * bucket_count`.
- Return the counts in bucket order.
- Return the result without printing or reading standard input. Use only Python's standard library.

## Tips
- Why does a value exactly on a boundary belong to the bucket on its right?
- What should happen when no buckets are requested?

## Example Behavior
`bucket_count([0, 1, 2, 3, 4, 5], 2, 3)` → `[2, 2, 2]`

`bucket_count([-1, 0, 10], 5, 2)` → `[1, 0]`
