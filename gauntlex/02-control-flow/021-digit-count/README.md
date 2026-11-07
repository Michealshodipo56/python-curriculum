# Decimal Length

## Description

The number of digits in an integer depends on its size, not on whether it is positive or negative. Build a program that counts the decimal digits in an input value. This challenge encourages careful handling of zero and sign characters.

## Requirements

- Read one integer from standard input.
- Display the number of decimal digits in its absolute value.
- Count zero as a one-digit number.
- Do not count a leading minus sign as a digit.
- Display one integer on one line without prompts or extra output.

## Tips

- Compare the digit counts of 9, 10, 99, and 100.
- What should happen to the sign of a negative number?
- Consider why zero needs special attention.

## Example Input

```text
-1204
```

## Example Output

```text
4
```
