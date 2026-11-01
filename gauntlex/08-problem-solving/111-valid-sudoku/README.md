# Sudoku Constraints

## Description
Validate the filled cells of a Sudoku grid without attempting to solve the puzzle.

### Behavior contract
Given a 9x9 grid of characters `1`–`9` or `.`, return whether all nonempty row, column, and 3x3-box entries are unique. The grid need not be solvable.

## Requirements
- Implement `valid_sudoku(board)` in `starter/solution.py`.
- Return the result without printing or reading input.
- Do not mutate input collections.
- Use only Python's standard library.

## Examples
Build tests for the specified graph or grid behavior.

## Tips
A digit can be legal in its row yet illegal in its column or three-by-three region.

The examples define expected behavior; design your own implementation.
