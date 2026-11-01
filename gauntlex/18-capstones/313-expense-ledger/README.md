# Expense Ledger

## Description
Build a persistent expense tracker that records amounts as integer cents and summarizes spending by category.

This is a project challenge. Plan the components, define their responsibilities, and implement the application without a provided solution.

## Requirements
Use `EXPENSE_DB` environment variable or default `expenses.db`. Commands: `add CATEGORY AMOUNT_CENTS`, `summary`, `list`. Amount must be a positive integer; invalid input exits 2 without inserting. `add` prints the new integer ID. `list` prints compact sorted-key JSON array of `{id,category,amount_cents}` in ID order. `summary` prints compact sorted-key JSON mapping category to total integer cents. The database persists across process runs. No floating-point currency arithmetic.

## Constraints
- Use Python 3.11+ and the standard library only.
- Do not use external services or third-party dependencies.
- Keep all state local and ensure deterministic JSON response shapes.
- Do not print debugging information to stdout.

## Deliverables
- Implement the application in `starter/main.py`, with additional modules only when useful.
- Document the program's usage, key design choices, and failure behavior.
- Explain how persistence, input validation, or the service lifecycle works where applicable.

## Tips
Money values must not be rounded through floating-point arithmetic.

## Guide and Auditor
The Gauntlex Guide should help you reason through decisions and debug issues without supplying finished code. The Auditor may ask you to demonstrate the required behavior and defend your design choices.
