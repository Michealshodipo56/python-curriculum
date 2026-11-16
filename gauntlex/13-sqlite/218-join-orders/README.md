# Orders and Their Owners

## Description

Implement `orders_with_users(conn)` in `starter/solution.py` using the supplied live `sqlite3.Connection`. Use `users(id,name,email)` and `orders(id,user_id,amount)`.

## Requirements

- Implement `orders_with_users(conn)` in `starter/solution.py` using the supplied live `sqlite3.Connection`.
- Use `users(id,name,email)` and `orders(id,user_id,amount)`.
- Return `[order_id, user_name, amount]` rows sorted by order ID.
- Exclude orders without a matching user.
- Do not modify either table.
- Use parameterized SQL for untrusted values, standard-library modules, and no printed output.
- Do not open a new connection or alter unrelated data or transaction state.

## Tips

- **Concept to understand:** Combine related order and user tables so each order is presented alongside the name of its owner.
- What makes an order an orphan?
- Why is a matching key needed when joining tables?

## Example Behavior

An order whose `user_id` has no matching user does not appear in the result.
