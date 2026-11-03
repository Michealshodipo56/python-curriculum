# Recolor a Region

## Description
Recolor the connected area containing a starting pixel without changing disconnected pixels of the same color.

## Requirements
- Implement `flood_fill(image, sr, sc, color)` in `starter/solution.py`.
- Assume a nonempty rectangular 2D integer image and valid coordinates `(sr, sc)`.
- Find all cells connected to the starting cell in the four cardinal directions that share its original color.
- Return a new image with only that region changed to `color`.
- Do not mutate the input; handle replacement with the original color.
- Return the result without printing or reading input. Use Python's standard library only.

## Tips
- Why does diagonal contact not establish connectivity?
- How can already visited cells be distinguished from unvisited ones?

## Example Behavior
`flood_fill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2)` → `[[2, 2, 2], [2, 2, 0], [2, 0, 1]]`.
