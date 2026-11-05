# The Middle Value

## Description
The median describes the center of a dataset after its observations are arranged in numeric order. The rule differs depending on whether the dataset has an odd or even number of values.

## Requirements
- Implement `median(values)` in `starter/solution.py`.
- Assume `values` is a nonempty list of numbers.
- Return the middle value for an odd number of observations.
- For an even number of observations, return the arithmetic mean of the two middle values.
- Do not change the input order or mutate the list.
- Return the result without printing or reading standard input. Use only Python's standard library.

## Tips
- Why is the original order irrelevant to the median?
- What happens when there are two central observations?

## Example Behavior
`median([3, 1, 2])` → `2`

`median([4, 1, 3, 2])` → `2.5`
