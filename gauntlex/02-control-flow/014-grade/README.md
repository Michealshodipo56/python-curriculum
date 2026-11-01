# Score Boundaries

## Description
A grading system translates numeric scores into letter categories. Write a program that chooses the correct category, especially at the boundaries between grades.

## Requirements
- Read one integer score from 0 through 100.
- Use A for 90–100, B for 80–89, C for 70–79, D for 60–69, and F for 0–59.
- Display only `Grade: X`, replacing X with the appropriate letter.

## Example
```text
Input:
90

Output:
Grade: A
```

## Tips
Test the values immediately below and above every grade boundary. Each possible score should belong to exactly one category.

The example demonstrates expected behavior; it does not reveal an implementation.
