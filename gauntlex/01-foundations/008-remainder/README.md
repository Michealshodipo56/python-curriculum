# Share Into Groups

## Description

Suppose a collection of items must be divided into groups of equal size. Some items may remain after forming every possible complete group. Build a program that reports both the number of complete groups and the leftover items.

## Requirements

- Read a nonnegative integer item count on the first line.
- Read a positive integer group size on the second line.
- Display `Groups: N` for the number of complete groups.
- Display `Leftover: N` for the unused items on the next line.
- Print no prompts or additional messages.

## Tips

- Try distributing a small number of objects by hand.
- How can you tell whether another complete group can be formed?
- Consider the cases where the item count is zero or smaller than the group size.

## Example Input

```text
17
5
```

## Example Output

```text
Groups: 3
Leftover: 2
```
