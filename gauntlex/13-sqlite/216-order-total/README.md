# Sum Customer Orders

## Description
Calculate the total value of orders associated with one user.

### Behavior contract
Return total amount for a given user_id in orders(id,user_id,amount). Return 0 if there are no matching orders.

## Requirements
- Implement `order_total(conn, user_id)` in `starter/solution.py`.
- The `conn` argument is a live `sqlite3.Connection` supplied by the caller.
- Do not open a new database connection or print output.
- Use parameterized SQL for untrusted values and standard-library modules only.
- Preserve the caller's existing data and transaction state except for the documented changes.

## Tips
An aggregate over no matching rows may not return the numeric zero you expect.

Design the database interaction yourself; no SQL solution is provided.
