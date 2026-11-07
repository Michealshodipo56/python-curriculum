# Most Frequent Observation

## Description

Find the most frequently observed integer in a dataset. When multiple integers are equally common, choose a deterministic answer.

## Requirements

- Implement `mode(values)` in `starter/solution.py`.
- Assume a nonempty list of integers.
- Return the value with the highest occurrence count.
- When several values tie for the highest count, return the smallest integer.
- Leave the input unchanged.
- Return the result without printing or reading standard input. Use only Python's standard library.

## Tips

- Why is the most frequent value not necessarily the largest?
- What should happen when all observations are distinct?

## Example Behavior

`mode([2, 3, 2, 3])` → `2`

`mode([5, 5, 1])` → `5`
