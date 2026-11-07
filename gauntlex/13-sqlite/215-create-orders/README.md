# Define the Orders Table

## Description

Store orders with nonnegative amounts and require the database to enforce that rule, regardless of which caller inserts the record.

## Requirements

- Implement `create_orders(conn)` in `starter/solution.py` using the caller's live `sqlite3.Connection`.
- Create `orders` if absent, with `id INTEGER PRIMARY KEY`, `user_id INTEGER NOT NULL`, and `amount INTEGER NOT NULL CHECK(amount>=0)`.
- Keep an existing table and its data unchanged.
- Make repeated calls safe.
- Use parameterized SQL for untrusted values, Python's standard library, and no printed output.
- Do not open another connection or alter unrelated records or transaction state.

## Tips

- Why should the amount constraint live in the database schema?
- What should happen if the setup function runs twice?

## Example Behavior

Calling `create_orders(conn)` again must not erase existing orders.
