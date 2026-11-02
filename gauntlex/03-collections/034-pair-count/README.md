# Matching Pairs

## Description
Repeated values can form pairs of matching positions. Build a program that counts every pair of distinct positions containing the same integer. A value appearing several times can contribute multiple pairs.

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
