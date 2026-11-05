# Sum Customer Orders

## Description
Calculate a customer's total order value using the database, even when that customer has no orders.

## Requirements
- Implement `order_total(conn, user_id)` in `starter/solution.py` using the supplied live `sqlite3.Connection`.
- Read amounts from `orders(id,user_id,amount)` for the supplied user ID.
- Return their numeric sum.
- Return `0` when no orders match.
- Do not alter any records.
- Use parameterized SQL for untrusted values, standard-library modules, and no printed output.
- Do not open a new connection or alter unrelated data or transaction state.

## Tips
- Why might a SQL aggregate over zero matching rows need special handling?

## Example Behavior
`order_total(conn, 42)` → `0` when customer 42 has no orders.
