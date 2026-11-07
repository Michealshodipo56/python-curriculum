# Sudoku Constraints

## Description

Check whether the currently filled cells in a Sudoku board obey the puzzle's uniqueness rules. Do not attempt to solve the board.

## Requirements

- Implement `valid_sudoku(board)` in `starter/solution.py`.
- Assume a 9-by-9 grid containing digits `'1'` through `'9'` and `'.'` for empty cells.
- Return `True` only if each row, column, and 3-by-3 box contains no repeated filled digit.
- Ignore `'.'` cells; the board need not be complete or solvable.
- Do not modify the board.
- Return the result without printing or reading input. Use Python's standard library only.

## Tips

- Why must each filled cell satisfy three different regions?
- Does an unfinished board necessarily violate the rules?

## Example Behavior

A board containing only `'.'` cells returns `True`; repeating `'5'` in one row returns `False`.
