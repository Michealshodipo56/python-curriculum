# Inside the Boundaries

## Description

Sometimes only the middle part of a sequence is needed. Build a program that excludes the first and last words and displays everything between them in the original order.

## Requirements

- Read one line of space-separated words; the line may be empty.
- Exclude the first and last word.
- Display the remaining words in their original order, separated by single spaces.
- If the input has fewer than three words, display a blank line.
- Do not print prompts or additional text.

## Tips

- Identify the positions that mark the beginning and end of the desired region.
- Consider whether those boundary positions belong in the result.
- What happens when the region contains no elements?

## Example Input

```text
a b c d
```

## Example Output

```text
b c
```
