# Permission Gate

## Description

Write a program that reads a person's age and whether they have a license (`yes` or `no`). Print `allowed` only if they are at least 16 years old **and** the license status is `yes`; otherwise print `denied`.

## Requirements

- Read an integer age on the first line.
- Read a lowercase license status, either `yes` or `no`, on the second line.
- Display `allowed` only when the age is at least 16 and the license status is `yes`.
- Display `denied` in every other case.
- Use lowercase output and do not print prompts or explanations.

## Tips

- Check each condition independently before considering the combined decision.
- What happens when only one requirement is met?
- Think about ages immediately below and at the threshold.

## Example Input

```text
16
yes
```

## Example Output

```text
allowed
```
