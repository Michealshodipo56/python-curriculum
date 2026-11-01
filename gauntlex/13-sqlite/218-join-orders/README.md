# Orders and Their Owners

## Description
Combine related tables to show each order alongside its user's name.

### Behavior contract
Return [order_id,user_name,amount] for orders joined to users by user_id, ordered by order_id. Assume tables users(id,name,email), orders(id,user_id,amount). Exclude orphan orders.

## Requirements
- Implement `orders_with_users(conn)` in `starter/solution.py`.
- The `conn` argument is a live `sqlite3.Connection` supplied by the caller.
- Do not open a new database connection or print output.
- Use parameterized SQL for untrusted values and standard-library modules only.
- Preserve the caller's existing data and transaction state except for the documented changes.

## Tips
An order without a matching user must not appear in the joined result.

Implement the database behavior without using solution code from another task.
