# Inventory Manager

## Description
Build a persistent stock-management CLI that records quantities and prevents stock from becoming negative.

This is a project challenge. Plan the components, define their responsibilities, and implement the application without a provided solution.

## Requirements
Build a SQLite-backed inventory CLI. INVENTORY_DB specifies database path. Commands: add SKU QTY, adjust SKU DELTA, get SKU, list. add prints ok or exists; adjust prints ok, insufficient, or not found. get prints compact sorted-key JSON {sku,quantity} or null; list prints JSON array sorted by SKU. Reject invalid integers with exit 2; never permit negative stock.

## Constraints
- Use Python 3.11+ and the standard library only.
- Do not use network services or print debug messages to standard output.

## Deliverables
- Implement the application in `starter/main.py`, with additional modules only when useful.
- Document the program's usage, key design choices, and failure behavior.
- Explain how persistence, input validation, or the service lifecycle works where applicable.

## Tips
Treat stock updates as guarded state transitions. Invalid quantities and insufficient stock are different failures.

## Guide and Auditor
The Gauntlex Guide should help you reason through decisions and debug issues without supplying finished code. The Auditor may ask you to demonstrate the required behavior and defend your design choices.
