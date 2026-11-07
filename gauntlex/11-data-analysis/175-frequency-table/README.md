# Observation Counts

## Description

Summarize a collection of integers by recording how many times each distinct value appears.

## Requirements

- Implement `frequency_table(values)` in `starter/solution.py`.
- Return a dictionary mapping each distinct integer to its number of occurrences.
- Include negative, zero, and positive integer keys when present.
- Return `{}` for empty input.
- Do not modify the original observations.
- Return the result without printing or reading standard input. Use only Python's standard library.

## Tips

- How does a repeated value change a frequency count?
- What is the natural representation of an empty dataset?

## Example Behavior

`frequency_table([1, 2, 1])` → `{1: 2, 2: 1}`

`frequency_table([])` → `{}`
