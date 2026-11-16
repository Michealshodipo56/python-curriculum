# Rank Customers by Spending

## Description

Implement `top_customers(conn, k)` in `starter/solution.py` using the supplied live `sqlite3.Connection`. Aggregate `orders(id,user_id,amount)` by user ID.

## Requirements

- Implement `top_customers(conn, k)` in `starter/solution.py` using the supplied live `sqlite3.Connection`.
- Aggregate `orders(id,user_id,amount)` by user ID.
- Return `[user_id, total]` rows ordered by total descending, then user ID ascending.
- Return at most `k` rows, assuming `k` is nonnegative.
- Return `[]` when `k` is zero.
- Use parameterized SQL for untrusted values, standard-library modules, and no printed output.
- Do not open a new connection or alter unrelated data or transaction state.

## Tips

- Why does the ranking need a tie-breaker?
- How does grouping differ from sorting?

## Example Behavior

Two customers with the same total appear in ascending user-ID order.
