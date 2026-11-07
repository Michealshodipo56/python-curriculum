# Score Boundaries

## Description

A grading system converts a numeric score into a letter category. Build a program that selects the correct grade for every valid score. This challenge focuses on ordered decisions and boundary values.

## Requirements

- Read one integer score between 0 and 100, inclusive.
- Assign `A` to 90–100, `B` to 80–89, `C` to 70–79, `D` to 60–69, and `F` to 0–59.
- Display the result exactly as `Grade: X`, where `X` is the letter.
- Print one line without prompts or additional output.

## Tips

- List the score ranges and make sure none overlap or leave gaps.
- Consider values immediately above and below each boundary.
- How can the program ensure that exactly one category is chosen?

## Example Input

```text
90
```

## Example Output

```text
Grade: A
```
