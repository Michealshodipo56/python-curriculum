# Find the Secret

## Description
Build a simple interactive guessing process. The program must respond to each attempt and stop as soon as the secret is found.

## Requirements
- Read integer guesses, one per line, until the value 7 is entered.
- Display `low` for guesses below 7 and `high` for guesses above 7.
- Display `correct` when the guess is 7 and stop reading further input. Assume 7 eventually appears.

## Example
```text
Input:
3
9
7

Output:
low
high
correct
```

## Tips
Separate the repeated input step from the condition that ends the game. What happens to guesses that appear after the correct one?

The example demonstrates expected behavior; it does not reveal an implementation.
