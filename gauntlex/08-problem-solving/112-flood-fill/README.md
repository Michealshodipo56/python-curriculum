# Recolor a Region

## Description
Change the color of one connected region in an image without changing disconnected cells.

### Behavior contract
Return a new 2D integer image with the four-directionally connected region starting at (sr,sc) recolored. Do not modify the input. Assume valid coordinates and a nonempty rectangular image.

## Requirements
- Implement `flood_fill(image, sr, sc, color)` in `starter/solution.py`.
- Return the result without printing or reading input.
- Do not mutate input collections.
- Use only Python's standard library.

## Examples
`flood_fill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2)` → `[[2, 2, 2], [2, 2, 0], [2, 0, 1]]`

## Tips
Connectivity uses four directions, not diagonals. Avoid revisiting already processed cells.

The examples define expected behavior; design your own implementation.
