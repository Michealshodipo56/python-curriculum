# Revenue by Category

## Description

Summarize sales performance by grouping amounts into categories, then rank the categories by total revenue.

## Requirements

- Implement `revenue_report(conn)` in `starter/solution.py` using the supplied live `sqlite3.Connection`.
- Read `sales(id,category,amount INTEGER)`.
- Sum amounts for each category.
- Return `[category, total]` rows ordered by total descending and category ascending for ties.
- Return `[]` when there are no sales.
- Use parameterized SQL for untrusted values, Python's standard library, and no printed output.
- Do not open another connection or change unrelated data or transaction state.

## Tips

- Why is the category name needed as a secondary sort key?
- How can aggregation reduce many sales rows to one row per category?

## Example Behavior

Two categories with equal revenue are returned in alphabetical category order.
