# Everyone Else's Product

## Description
For each position, multiply every other value in the list, excluding the value at that position. This challenge requires reasoning about products without division.

## Requirements
- Implement `product_except_self(nums)` in `starter/solution.py`.
- Return a new list of the same length as `nums`.
- At index `i`, include the product of all values except `nums[i]`.
- Do not use division.
- Handle zeros and negative values correctly without modifying the input.
- Return the result without printing or reading input. Use Python's standard library only.

## Tips
- What changes when the list contains one zero or several zeros?
- How can values before and after a position contribute separately?

## Example Behavior
`product_except_self([1, 2, 3, 4])` → `[24, 12, 8, 6]`; `product_except_self([0, 1, 2])` → `[2, 0, 0]`.
