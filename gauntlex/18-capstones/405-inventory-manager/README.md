# Inventory Manager

## Description

Build a persistent stock-management CLI that records quantities and prevents stock from becoming negative.

This is a project challenge. Plan the components, define their responsibilities, and implement the application without a provided solution.

## Requirements

- Run commands from `starter/` as `python main.py add SKU QTY`, `python main.py adjust SKU DELTA`, `python main.py get SKU`, or `python main.py list`.
- Persist inventory in SQLite at the path supplied by `INVENTORY_DB` across separate process runs.
- `add` accepts a nonnegative integer quantity, including zero. It prints `ok` for a new SKU or `exists` without changing an existing SKU.
- `adjust` applies an integer delta. Print `not found` for an unknown SKU, `insufficient` if the result would be negative, or `ok` after a valid update. A rejected update leaves stock unchanged.
- `get` prints compact, sorted-key JSON with `sku` and integer `quantity`, or `null` for an unknown SKU.
- `list` prints a JSON array of the same record shape, sorted by SKU; an empty inventory produces `[]`.
- Reject noninteger quantities and negative initial quantities with exit status `2`, without changing stored data.
- End each printed result with a newline. Never permit negative stock.

## Constraints

- Use Python 3.11+ and the standard library only.
- Do not use network services or print debug messages to standard output.

## Deliverables

- Implement the application in `starter/main.py`, with additional modules only when useful.
- Document the program's usage, key design choices, and failure behavior.
- Explain stock validation and how rejected changes preserve inventory.

## Design Considerations

Guard updates against negative stock before committing changes. Distinguish an unknown SKU from an existing SKU with insufficient quantity.

## Example Behavior

An adjustment that would make stock negative returns `insufficient` and leaves the persisted quantity unchanged.

## Tips

Treat stock updates as guarded state transitions. Invalid quantities and insufficient stock are different failures.

## Guide and Auditor

The Gauntlex Guide should help you reason through decisions and debug issues without supplying finished code. The Auditor may ask you to demonstrate the required behavior and defend your design choices.
