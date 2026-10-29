# Expense Ledger CLI

## Project brief
Build a SQLite-backed expense ledger with accurate integer-cent accounting.

## Acceptance contract
Use `EXPENSE_DB` environment variable or default `expenses.db`. Commands: `add CATEGORY AMOUNT_CENTS`, `summary`, `list`. Amount must be a positive integer; invalid input exits 2 without inserting. `add` prints the new integer ID. `list` prints compact sorted-key JSON array of `{id,category,amount_cents}` in ID order. `summary` prints compact sorted-key JSON mapping category to total integer cents. The database persists across process runs. No floating-point currency arithmetic.

## Constraints
- Use Python 3.11+ and the standard library only.
- Do not use external services or third-party dependencies.
- Keep all state local and ensure deterministic JSON response shapes.
- Do not print debugging information to stdout.

## Deliverables
- Implement the complete working project in `starter/main.py` and any additional modules under `starter/`.
- Add your own unit and integration tests beyond the provided acceptance checks.
- Document architecture, failure modes, and how to run the program.

## AI Guide policy
The Guide may ask about architecture, input contracts, and debugging, but must never provide full code or a working answer.

## AI Auditor defense
Explain your architecture, show a passing end-to-end test, and justify how you handle invalid inputs and persistence or service lifecycle.
