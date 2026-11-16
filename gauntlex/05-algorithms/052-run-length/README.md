# Compress Repeated Runs

## Description

Implement `run_length(text)` in `starter/solution.py`. Return a list of two-element lists in the form `[character, count]`.

## Requirements

- Implement `run_length(text)` in `starter/solution.py`.
- Return a list of two-element lists in the form `[character, count]`.
- Create a separate entry for each consecutive run, preserving order.
- Return an empty list for empty input.
- Do not print or execute code on import.

## Tips

- **Concept to understand:** Represent a string as consecutive runs of identical characters. Each run records the character and the number of times it appears without interruption.
- How can you tell when one run ends and the next begins?
- Why must separated runs of the same character remain distinct?

## Example Behavior

`run_length('aaabb')` → `[['a', 3], ['b', 2]]`; `run_length('abc')` → `[['a', 1], ['b', 1], ['c', 1]]`.
