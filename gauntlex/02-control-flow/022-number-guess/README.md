# guess

## Description
Read integer guesses, one per line, until the secret number 7 is entered. Respond to each guess.

## Requirements
For each guess less than 7 print `low`; for each guess greater than 7 print `high`; when 7 is entered print `correct` and stop reading. Assume 7 eventually appears.

## Examples
Input: "3\n9\n7\n" → output: "low\nhigh\ncorrect\n"

Input: "7\n" → output: "correct\n"

## Tips
A loop can keep reading until a stopping condition occurs. `break` can end a loop early.
