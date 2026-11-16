# Matching Pairs

## Description

Write a program that reads a line of integers and counts how many pairs of different positions contain the same number. Print the total number of matching pairs; print `0` if there are none.

## Requirements

- Read one line of space-separated integers; the line may be empty.
- Count each pair of distinct positions with equal values exactly once.
- Display the total number of matching pairs on one line.
- If the input is empty or has no matching positions, display `0`.
- Do not print prompts or additional text.

## Tips

- Work through a collection with three copies of the same value.
- When a new copy appears, how many earlier copies could it pair with?
- Be careful not to count the same two positions in both orders.

## Example Input

```text
2 2 2
```

## Example Output

```text
3
```
