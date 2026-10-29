# bucket_count

## Challenge
Count numeric values in half-open intervals [0,width), [width,2*width), ... for bucket_count bins. Values below 0 or >=width*bucket_count are ignored. Assume width>0 and bucket_count>=0.

## Requirements
- Implement `bucket_count(values, width, bucket_count)` in `starter/solution.py`.
- Return the result; do not print or read standard input.
- Do not mutate the input lists.
- Use only the Python standard library.

## Examples
`bucket_count([0, 1, 2, 3, 4, 5], 2, 3)` → `[2, 2, 2]`

`bucket_count([-1, 0, 10], 5, 2)` → `[1, 0]`

## Hints
Integer division can identify a bucket index.
