# Expense Ledger

## Description

Build a persistent expense tracker that records amounts as integer cents and summarizes spending by category.

This is a project challenge. Plan the components, define their responsibilities, and implement the application without a provided solution.

## Requirements

- Run `python main.py add CATEGORY AMOUNT_CENTS`, `python main.py summary`, or `python main.py list` from `starter/`.
- Persist expenses in SQLite at `EXPENSE_DB`, defaulting to `expenses.db` in the working directory.
- `AMOUNT_CENTS` must be a positive integer. Invalid amounts exit with status `2` without inserting an expense.
- `add` prints the new integer ID.
- `list` prints a compact JSON array of objects with `id`, `category`, and integer `amount_cents`, ordered by ID.
- `summary` prints a compact JSON object mapping category names to total integer cents.
- Sort JSON object keys. An empty ledger lists as `[]` and summarizes as `{}`. End each printed result with a newline.
- Preserve data between process runs. Use integer cents throughout; do not use floating-point currency arithmetic.

## Constraints

- Use Python 3.11+ and the standard library only.
- Do not use external services or third-party dependencies.
- Keep all state local and ensure deterministic JSON response shapes.
- Do not print debugging information to stdout.

## Deliverables

- Implement the application in `starter/main.py`, with additional modules only when useful.
- Document the program's usage, key design choices, and failure behavior.
- Explain integer-cent storage and category aggregation.

## Design Considerations

Keep monetary values as integer cents through storage and aggregation. Invalid amounts must not create rows or change summaries.

## Example Behavior

After adding 125 and 75 cents in one category, its summary total is 200 cents, not a floating-point approximation.

## Tips

Money values must not be rounded through floating-point arithmetic.

## Guide and Auditor

The Gauntlex Guide should help you reason through decisions and debug issues without supplying finished code. The Auditor may ask you to demonstrate the required behavior and defend your design choices.
