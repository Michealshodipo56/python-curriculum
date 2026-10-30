# Inventory Manager

## Project brief and acceptance criteria
Build a SQLite-backed inventory CLI. INVENTORY_DB specifies database path. Commands: add SKU QTY, adjust SKU DELTA, get SKU, list. add prints ok or exists; adjust prints ok, insufficient, or not found. get prints compact sorted-key JSON {sku,quantity} or null; list prints JSON array sorted by SKU. Reject invalid integers with exit 2; never permit negative stock.

## Deliverables
Implement in starter/main.py, add unit tests and document architecture. Python 3.11+ standard library only. No network services. Do not print debug output to stdout. Use parameterized SQL where applicable.

## Run
python -m pytest tests -q
