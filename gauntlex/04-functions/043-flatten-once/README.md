# One Level Down

## Description

In `starter/solution.py`, write `flatten_once(groups)` to combine a list of smaller lists into one new list, keeping the original element order. For example, `[[1, 2], [3]]` becomes `[1, 2, 3]`. Do not change the original lists.

## Requirements

- Implement `flatten_once(groups)` in `starter/solution.py`.
- Accept a list of lists.
- Return a new list containing the inner elements in their original order.
- Handle empty inner lists and an empty outer list.
- Do not mutate the supplied lists, print, or execute input-handling code on import.

## Tips

- How does combining inner lists differ from recursively flattening arbitrary nesting?
- What should an empty inner list contribute?
- Consider how to preserve element order.

## Example Behavior

`flatten_once([[1, 2], [3], []])` → `[1, 2, 3]`.
