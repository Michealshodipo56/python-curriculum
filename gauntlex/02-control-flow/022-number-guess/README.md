# Find the Secret

## Description

Write a program that reads guesses, one number per line, until the user guesses the secret number `7`. After each guess, print `low` if it is below `7`, `high` if it is above `7`, or `correct` if it equals `7`. Stop immediately after printing `correct`.

## Requirements

- Read integer guesses from standard input, one per line.
- The secret number is `7`.
- Display `low` when a guess is below 7 and `high` when it is above 7.
- Display `correct` when the guess is 7, then stop reading input.
- Assume the input eventually contains 7.
- Display one feedback line per processed guess, with no prompts or additional text.

## Tips

- What action must repeat, and what event ends that repetition?
- Think about when feedback should be displayed relative to checking the guess.
- Guesses after the correct answer must not affect the output.

## Example Input

```text
3
9
7
```

## Example Output

```text
low
high
correct
```
